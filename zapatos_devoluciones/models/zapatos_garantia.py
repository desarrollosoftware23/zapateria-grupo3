from odoo import models, fields, api
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta

class Garantia(models.Model):
    _name = 'zapateria.garantia'
    _description = 'Garantías'

    codigo = fields.Char(
        string='Código',
        required=True,
        readonly=True,
        default=lambda self: fields.Datetime.now().strftime('GAR%Y%m%d%H%M%S'),
        copy=False)

    zapato_id = fields.Many2one( 'zapatos.zapato', string='Zapato', required=True)

    cliente_id = fields.Many2one('res.partner', string='Cliente')
    
    venta_id = fields.Many2one('sale.order', string='Orden de Venta')

    tipo = fields.Selection([
        ('fabricante', 'Fabricante'),
        ('tienda', 'Tienda'),
        ('extendida', 'Extendida'),
    ], string='Tipo de Garantía', default='tienda')

    fecha_inicio = fields.Date( string='Fecha Inicio', default=fields.Date.today)

    fecha_fin = fields.Date( string='Fecha Fin')

    estado = fields.Selection([
        ('activa', 'Activa'),
        ('vencida', 'Vencida'),
        ('cancelada', 'Cancelada')],
        string='Estado', default='activa')

    dias_restantes = fields.Integer( string='Días Restantes', compute='_compute_dias_restantes', store=True)

    descripcion = fields.Text(string='Descripción')

    _sql_constraints = [
        (
            'codigo_garantia_unico',
            'unique(codigo)',
            'Ya existe una garantía con ese código.'
        )
    ]

    @api.onchange('zapato_id')
    def _onchange_zapato_id(self):
        if self.zapato_id:
            self.fecha_inicio = fields.Date.today()
            meses = self.zapato_id.garantias_meses
            if meses and meses > 0:
                self.fecha_fin = fields.Date.today() + relativedelta(months=meses)
            else:
                self.fecha_fin = False

    @api.depends('fecha_fin')
    def _compute_dias_restantes(self):
        hoy = fields.Date.today()
        for record in self:
            if record.fecha_fin:
                record.dias_restantes = (record.fecha_fin - hoy).days
            else:
                record.dias_restantes = 0
                
    def action_cancelar(self):
        for record in self:
            if record.estado == 'activa':
                record.estado = 'cancelada'

    def action_reactivar(self):
        for record in self:
            if record.estado == 'cancelada':
                hoy = fields.Date.today()
                if record.fecha_fin and record.fecha_fin >= hoy:
                    record.estado = 'activa'
                else:
                    raise ValidationError("No se puede reactivar una garantía cuya fecha fin ya venció.")

    @api.constrains('fecha_inicio', 'fecha_fin')
    def _check_fechas(self):
        for record in self:
            if record.fecha_inicio and record.fecha_fin:
                if record.fecha_fin < record.fecha_inicio:
                    raise ValidationError("La fecha fin no puede ser menor a la fecha inicio.")
                
    @api.onchange('venta_id')
    def _onchange_venta_id(self):
        if self.venta_id:
            self.cliente_id = self.venta_id.partner_id
