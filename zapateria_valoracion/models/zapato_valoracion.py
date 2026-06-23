from odoo import models, fields

class ZapatosValoracion(models.Model):
    _inherit = 'zapatos.zapato'

    puntuacion = fields.Selection([
        ('1','⭐')
        ('2','⭐⭐')
        ('3','⭐⭐⭐')
        ('4','⭐⭐⭐⭐')
        ('5','⭐⭐⭐⭐⭐')
    ], string='Puntuacion')
    comentario = fields.Text(string='Comentario')
    fecha_valoracion = fields.Data(string='Fecha de valoracion')    