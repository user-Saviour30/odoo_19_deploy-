{
    'name': 'My New App',
    'version': '19.0.1.0.0',
    'summary': 'New Custom Module for Odoo 19',
    'author': 'Developer',
    'category': 'Uncategorized',
    'depends': ['base','mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/my_app_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}