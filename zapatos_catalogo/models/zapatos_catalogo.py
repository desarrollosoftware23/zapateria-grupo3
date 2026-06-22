from odoo import models, fields, api


class ZapatosCatalogo(models.Model):
    _inherit = 'zapatos.zapato'

    talla = fields.Selection([
        ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'),
        ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'),
        ('30', '30'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'),
        ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'),
        ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'),
        ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'), ('49', '49'),
        ('50', '50'),
    ], string='Talla')

    tipo_zapato = fields.Selection([
        ('deportivo', 'Deportivo'),
        ('formal', 'Formal'),
        ('casual', 'Casual'),
        ('infantil', 'Infantil'),
        ('sandalia', 'Sandalia'),
    ], string='Tipo de Zapato')

    temporada_recomendada = fields.Char(
        string='Temporada Recomendada',
        compute='_compute_temporada_recomendada',
        store=True,
    )

    @api.depends('tipo_zapato')
    def _compute_temporada_recomendada(self):
        recomendaciones = {
            'deportivo': 'Verano',
            'formal': 'Invierno',
            'casual': 'Primavera / Otoño',
            'infantil': 'Primavera',
            'sandalia': 'Verano',
        }
        for record in self:
            record.temporada_recomendada = recomendaciones.get(record.tipo_zapato, 'Sin recomendación')
