from odoo import models, fields

class ZapatosValoracion(models.Model):
    _inherit = 'zapatos.zapato'

    puntuacion = fields.Selection([
        ('1', '⭐'),
        ('2', '⭐⭐'),
        ('3', '⭐⭐⭐'),
        ('4', '⭐⭐⭐⭐'),
        ('5', '⭐⭐⭐⭐⭐'),
    ], string='Puntuación')

    imagen = fields.Image(string='Imagen')