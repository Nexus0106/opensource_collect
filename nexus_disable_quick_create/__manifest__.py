# -*- coding: utf-8 -*-
{
    'name': 'Disable Easy Create',

    'version': '17.1.1.0',

    'summary': 'Disable Easy Create',

    'author': 'Nexus',

    'license': "LGPL-3",

    'email': 'nexus.innovatech.yours@gmail.com',

    'category': 'Technichal/Settings',

    'depends': [
        'web',
    ],

    'description': """
        Disable Create and Edit, Disable Quick Create, Disable Create for Many2manyfields, Many2onefields
               (Remark: You can management with manual open this options)
    """,

    "assets": {
        "web.assets_backend": [
            "nexus_disable_quick_create/static/src/js/fields.esm.js",
        ]
    },

    'installable': True,

    'application': True,

    'auto_install': False,

    'images': ['static/description/icon.png'],
}
