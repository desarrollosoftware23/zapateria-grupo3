from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class Garantia(models.Model):
    _name = 'zapateria.garantia'
    _description = 'Garantías'

    codigo = fields.Char(string='Código', required=True, readonly=True, default=lambda self: datetime.now().strftime('Garanta%Y%m%d%H%M%S'), copy=False)

    fecha_inicio = fields.Date(string='Fecha Inicio')

    fecha_fin = fields.Date(string='Fecha Fin'
    )

    descripcion = fields.Text(string='Descripción')

    estado = fields.Selection([
        ('activa', 'Activa'),
        ('vencida', 'Vencida')], 
        string='Estado')

    zapato_id = fields.Many2one('zapatos.zapato', string='Zapato',required=True)

    _sql_constraints = [
        (
            'codigo_garantia_unico',
            'unique(codigo)',
            'Ya existe una garantía con ese código.'
        )
    ]


    @api.constrains('fecha_inicio', 'fecha_fin')
    def _check_fechas(self):
        for record in self:
            if record.fecha_fin and record.fecha_inicio:
                if record.fecha_fin < record.fecha_inicio:
                    raise ValidationError("La fecha final no puede ser menor a la fecha inicial")
    @api.constrains('descripcion')
    def _check_descripcion(self):
        for record in self:
            if not record.descripcion or len(record.descripcion.strip()) < 10:
                raise ValidationError("La descripción debe tener al menos 10 caracteres.")