# -*- coding: utf-8 -*-
{
    'name': 'Qweb Report Elements',

    'version': '17.0.0.0',

    'summary': 'Qweb Report Elements',

    'description': """
        New elements for pdf class
        ** first-page
        ** last-page
    """,

    'category': 'Reports',

    'author': 'ZbyE Solution',
    
    'company': 'ZbyE Solution',
    
    'maintainer': 'Rowan Ember',
    
    'website': 'https://nexorionis.odoo.com',

    'license': "LGPL-3",

    'email': 'zbye.info@gmail.com',
    'support': 'zbye.info@gmail.com',

    'depends': [
        'web',
    ],

    'data': [
        'views/layouts.xml',
    ],

    'installable': True,

    'application': False,

    'auto_install': False,

    'images': ['static/description/banner.png'],
}
