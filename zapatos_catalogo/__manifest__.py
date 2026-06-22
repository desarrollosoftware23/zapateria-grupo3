{
    'name': 'zapatos_catalogo',
    'version': '1.0',
    'summary': 'Catálogo de zapatos por talla y temporada',
    'description': 'Extiende zapatos_extension con tallas ampliadas y recomendación de temporada según tipo de zapato.',
    'author': 'Jennifer',
    'category': 'Sales',
    'license': 'LGPL-3',
    'depends': ['zapatos_extension'],
    'data': [
        'security/ir.model.access.csv',
        'views/zapatos_catalogo_views.xml',
    ],
    'installable': True,
    'application': True,
}
