from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ZapatosZapato(models.Model):
    _inherit = 'zapatos.zapato'
    genero = fields.Selection([
        ('hombre', 'Hombre'),
        ('mujer', 'Mujer'),
        ('unisex', 'Unisex'),
        ('nino', 'Niño'),
    ], string='Género', required=True)
    tipo_calzado = fields.Selection([
        ('deportivo', 'Deportivo'),
        ('formal', 'Formal'),
        ('casual', 'Casual'),
        ('sandalia', 'Sandalia'),
        ('bota', 'Bota'),
    ], string='Tipo de calzado', required=True)
    temporada = fields.Selection([
        ('verano', 'Verano'),
        ('invierno', 'Invierno'),
        ('todo_el_anio', 'Todo el año'),
    ], string='Temporada')
    impermeable = fields.Boolean(string='Impermeable', default=False, help='Marca si el calzado resiste el agua')
    porcentaje_descuento = fields.Float(string='Porcentaje de descuento (%)',  help='Valor entre 0 y 100 que se descuenta del precio')
    precio_final = fields.Float(string='Precio final', compute='_compute_precio_final', store=True, help='Se calcula automáticamente según el precio y el descuento')

    @api.depends('precio', 'porcentaje_descuento')
    def _compute_precio_final(self):
        for registro in self:
            if registro.porcentaje_descuento:
                registro.precio_final = registro.precio * (1 - registro.porcentaje_descuento / 100)
            else:
                registro.precio_final = registro.precio

    @api.constrains('porcentaje_descuento', 'precio')
    def _check_porcentaje_descuento(self):
        for registro in self:
            if registro.porcentaje_descuento < 0 or registro.porcentaje_descuento > 100:
                raise ValidationError('El porcentaje de descuento debe estar entre 0 y 100')
            if registro.porcentaje_descuento > 0 and registro.precio <= 0:
                raise ValidationError('No puedes aplicar un descuento si el precio no es mayor a cero')

    @api.constrains('precio')
    def _check_precio(self):
        for registro in self:
            if registro.precio < 0:
                raise ValidationError('El precio no puede ser negativo')

    @api.constrains('stock')
    def _check_stock(self):
        for registro in self:
            if registro.stock < 0:
                raise ValidationError('El stock no puede ser negativo')

    @api.constrains('talla')
    def _check_talla(self):
        for registro in self:
            if registro.talla and (registro.talla < 15 or registro.talla > 50):
                raise ValidationError('La talla debe estar entre 15 y 50')
