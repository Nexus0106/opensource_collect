# -*- coding: utf-8 -*-
{
    'name': 'Disable Easy Create',

    'version': '17.1.1.0',

    'summary': 'Disable Easy Create',

    'category': 'Technichal/Settings',

    'website': 'https://www.asiamatrixsoftware.com',

    'depends': [
        'web',
    ],

    'description': """
        V1.0 - Disable Create and Edit, Disable Quick Create, Disable Create
               (Remark: You can management with manual open this options)
        V1.1 - Add Many2manyfields
    """,

    "maintainers": ["dhongu"],

    "assets": {
        "web.assets_backend": [
            "disable_quick_create/static/src/js/fields.esm.js",
        ]
    },

    'installable': True,

    'application': True,

    'auto_install': False,

    'license': 'LGPL-3',

    'images': ['static/description/icon.png'],
}
