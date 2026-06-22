from odoo import models, fields, api

class ZapatosZapato(models.Model):
    _inherit = 'zapatos.zapato'

    genero = fields.Selection([
        ('hombre', 'Hombre'),
        ('mujer', 'Mujer'),
        ('unisex', 'Unisex'),
        ('nino', 'Niño'), ], string='Género')
    tipo_calzado = fields.Selection([
        ('deportivo', 'Deportivo'),
        ('formal', 'Formal'),
        ('casual', 'Casual'),
        ('sandalia', 'Sandalia'),
        ('bota', 'Bota'),
    ], string='Tipo de calzado')
    temporada = fields.Selection([
        ('verano', 'Verano'),
        ('invierno', 'Invierno'),
        ('todo_el_anio', 'Todo el año'),
    ], string='Temporada')
    impermeable = fields.Boolean(string='Impermeable', default=False)
    porcentaje_descuento = fields.Float(string='Porcentaje de descuento (%)')
    precio_final = fields.Float(string='Precio final', compute='_compute_precio_final', store=True)
    @api.depends('precio', 'porcentaje_descuento')
    def _compute_precio_final(self):
        for registro in self:
            if registro.porcentaje_descuento:
                registro.precio_final = registro.precio * (1 - registro.porcentaje_descuento / 100)
            else:
                registro.precio_final = registro.precio