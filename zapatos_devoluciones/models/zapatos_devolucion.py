from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Devolucion(models.Model):
    _name = 'zapateria.devolucion'
    _description = 'Devoluciones'

    codigo = fields.Char(
        string='Código',
        required=True,
        readonly=True,
        default=lambda self: fields.Datetime.now().strftime('DEV%Y%m%d%H%M%S'),
        copy=False)

    zapato_id = fields.Many2one( 'zapatos.zapato', string='Zapato', required=True)

    cliente = fields.Char( string='Cliente', required=True)

    tipo = fields.Selection([
        ('cambio', 'Cambio de producto'),
        ('reembolso', 'Reembolso'),
        ('garantia', 'Por garantía'),
    ], string='Tipo de Devolución', default='cambio')

    fecha = fields.Date( string='Fecha', default=fields.Date.today)

    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada')],
        string='Estado', default='pendiente')

    motivo = fields.Text( string='Motivo', required=True)

    observaciones = fields.Text( string='Observaciones')

    _sql_constraints = [
        (
            'codigo_unico',
            'unique(codigo)',
            'Ya existe una devolución con ese código.'
        )
    ]

    def action_aprobar(self):
        for record in self:
            if record.estado == 'pendiente':
                record.estado = 'aprobada'

    def action_rechazar(self):
        for record in self:
            if record.estado == 'pendiente':
                record.estado = 'rechazada'

    def action_restablecer(self):
        for record in self:
            if record.estado in ('aprobada', 'rechazada'):
                record.estado = 'pendiente'

    @api.constrains('motivo')
    def _check_motivo(self):
        for record in self:
            if not record.motivo or len(record.motivo.strip()) < 10:
                raise ValidationError( "El motivo debe tener al menos 10 caracteres." )

    @api.constrains('fecha')
    def _check_fecha(self):
        for record in self:
            if record.fecha and record.fecha > fields.Date.today():
                raise ValidationError( "La fecha de devolución no puede ser futura.")