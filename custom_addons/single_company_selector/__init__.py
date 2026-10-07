from . import models

{
    'name': 'Single Company Selector',
    'version': '19.0.1.0.0',
    'category': 'Customization',
    'summary': 'Prevent auto-selecting child companies when choosing a parent company',
    'author': 'Custom Developer',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}