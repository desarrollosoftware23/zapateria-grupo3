{
    'name': 'zapatos_devoluciones_garantias',
    'version': '1.0',
    'summary': 'Es una extension de  zapateria',
    'description': 'Completa y agrega funcionalidades a zapateria.',
    'author': 'Dario Guayasamin',
    'category': 'Sales',
    'license': 'LGPL-3',
    'depends': ['zapatos','sale'],
    'data': [
        
        'views/zapato_extension_views.xml',
        'views/devolucion_views.xml',
        'views/garantia_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
