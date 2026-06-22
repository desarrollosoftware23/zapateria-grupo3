from odoo import models, fields, api

class ZapatosPadre(models.Model):
    _inherit = 'zapatos.zapato'

    garantias_meses = fields.Integer(string='Garantías en meses',default=0)

    devolucion_ids = fields.One2many('zapateria.devolucion','zapato_id',string='Devoluciones')

    garantia_ids = fields.One2many('zapateria.garantia','zapato_id',string='Garantías')