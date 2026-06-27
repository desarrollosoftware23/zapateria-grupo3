from odoo import models, fields

class ZapatosValoracion(models.Model):
    _inherit = 'zapatos.zapato'

    puntuacion = fields.Selection([
        ('0', 'Normal')
        ('1', '⭐'),
        ('2', '⭐⭐'),
        ('3', '⭐⭐⭐'),
    ], string='Puntuación'),required=True

    imagen = fields.Image(string='Imagen', max_width=256, max_height=256, required=True)