{
    'name': 'zapatos_valoracion',
    'version': '1.0',
    'summary': 'Valoración de zapatos',
    'description': 'Agrega puntuación, comentario y fecha de valoración al módulo de zapatos.',
    'author': 'Jorge',
    'category': 'Sales',
    'license': 'LGPL-3',
    'depends': ['zapatos'],
    'data': [
        'security/ir.model.access.csv',
        'views/zapato_valoracion_views.xml',
    ],
    'installable': True,
    'application': True,
}