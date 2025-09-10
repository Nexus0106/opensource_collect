# -*- coding: utf-8 -*-
{
    'name': "Hide Action Delete",

    'summary': """Hide Delete Button from Action""",

    'description': """
        Hide Delete Button from Action With Groups Access Right For ALl models from tree and form views
    """,

    'author': "Sura",

    'maintainer': 'Sura',

    'company':"NexOrionis Techsphere",

    'email': 'nexorionis.info@gmail.com',

    'website': 'https://nexorionis.odoo.com',

    'license': 'LGPL-3',

    'category': 'Security',

    'version': '1.0',

    'depends': [
        'web'
    ],

    'images': ['static/description/banner.jpg'],

    'data': [
        'security/hide_menu_access.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'noi_hide_delete_action/static/src/js/hide_delete_action.js',
        ]
    },
}