{
    'name': 'zapatos_detalle',
    'version': '1.2',
    'summary': 'Detalles, validaciones y proveedor del calzado',
    'description': 'Agrega características, precio con descuento, validaciones y vínculo con Contactos al módulo de zapatos',
    'author': 'Chriss',
    'category': 'Sales',
    'license': 'LGPL-3',
    'depends': ['zapatos', 'contacts'],
    'data': [
        'views/zapato_detalle_views.xml',
    ],
    'installable': True,
    'application': True,
}
