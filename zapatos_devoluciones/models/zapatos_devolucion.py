from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


class Devolucion(models.Model):
    _name = 'zapateria.devolucion'
    _description = 'Devoluciones'


    codigo = fields.Char(string='Código', required=True, readonly=True, default=lambda self: datetime.now().strftime('Devoluciones%Y%m%d%H%M%S'), copy=False)

    fecha = fields.Date(string='Fecha')

    motivo = fields.Text(string='Motivo',required=True)

    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada') ], string='Estado')

    zapato_id = fields.Many2one('zapatos.zapato',string='Zapato',required=True)

    _sql_constraints = [
        (
            'codigo_unico',
            'unique(codigo)',
            'Ya existe una devolución con ese código.'
        )
    ]

    @api.constrains('motivo')
    def _check_motivo(self):
        for record in self:
            if not record.motivo or len(record.motivo.strip()) < 10:
                raise ValidationError("El motivo debe tener al menos 10 caracteres.")
        
    @api.constrains('fecha')
    def _check_fecha(self):
        for record in self:
            if record.fecha and record.fecha > fields.Date.today():
                raise ValidationError("La fecha de devolución no puede ser futura.")
