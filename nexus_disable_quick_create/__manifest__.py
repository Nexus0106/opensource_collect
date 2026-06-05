# -*- coding: utf-8 -*-
{
    'name': 'Disable Easy Create',

    'version': '17.0.0.0',

    'summary': 'Disable Easy Create',

    'author': 'ZbyE Solution',
    
    'company': 'ZbyE Solution',
    
    'maintainer': 'Rowan Ember',
    
    'website': 'https://zbye.odoo.com',

    'license': "LGPL-3",

    'email': 'zbye.info@gmail.com',
    'support': 'zbye.info@gmail.com',

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

    'images': ['static/description/banner.png'],
}
