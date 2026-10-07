{
    'name': 'Hotel Management',
    'version': '19.0.1.0.0',
    'summary': 'Hotel Room and Booking Management System',
    'category': 'Industry',
    'author': 'Developer',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/hotel_room_views.xml',
        'views/hotel_booking_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}