# -*- coding: utf-8 -*-
{
    'name': 'Lots Expiration Dashbard',
    'version': '17.0.0.0',
    'summary': 'Expired lots in inventory dashboard.',
    'sequence': 100,
    'category': 'Inventory',
    'author': 'ZbyE Solution',

    'company': 'ZbyE Solution',

    'maintainer': 'Rowan Ember',

    'website': 'https://zbye.odoo.com',
    'support': 'zbye.info@gmail.com',
    'depends': [
        'web',
        'stock',
        'product_expiry',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/expired_lots_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'assets': {

        'web.assets_backend': [
            'noi_expired_lots/static/src/css/styles.css',
            'noi_expired_lots/static/src/js/control_panel.js',
            'noi_expired_lots/static/src/xml/ExpiredLotsDashboard.xml',
            'noi_expired_lots/static/src/js/ExpiredLotsDashboard.js',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'images': ['static/description/banner.gif'],
}
