# -*- coding: utf-8 -*-
{
    'name': 'Myanmar NRC Format',
    'version': '15.0.1.0.0',
    'summary': 'Myanmar National Registration Card (NRC) Format for Odoo',
    'description': """
Myanmar National Registration Card (NRC) Format
================================================

This module provides Myanmar NRC (National Registration Card) format support for Odoo.

The Myanmar NRC format follows the pattern: PREFIX/TOWNSHIP(TYPE)NUMBER

Components:
-----------
* **State/Region Code (1-14)**: Represents the 14 states and regions of Myanmar
* **Township Code**: Unique code for each township within a state/region
* **Citizenship Type**: N (Citizen), P (Associate Citizen), A (Naturalized Citizen), T (Temporary)
* **Registration Number**: 6-digit unique number

Example: 7/PAMANA(N)123456
- 7: Chin State
- PAMANA: Township code
- N: Citizen
- 123456: Registration number

Features:
---------
* Complete list of 14 Myanmar states/regions
* Township codes for all regions
* Four citizenship types (N, P, A, T)
* NRC field integration with Sale Order
* Easy-to-use dropdown selection
* Automatic NRC format composition

This module is essential for businesses operating in Myanmar that need to record
customer NRC information in their sales transactions.
    """,
    'category': 'Localization',
    "author": "NexOrioins Techsphere",
    "maintainer": "Rowan Ember",
    "website": "nexorionis.odoo.com",
    "support": "nexorionis.info@gmail.com",
    'license': 'LGPL-3',
    'depends': [
        'base',
        'contacts'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/nrc_prefix_data.xml',
        'data/nrc_type_data.xml',
        'data/nrc_township_code_data.xml',
        'views/nrc_prefix_views.xml',
        'views/nrc_township_code_views.xml',
        'views/nrc_type_views.xml',
        'views/menu_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
