{
    "name": "Main Menu",
    "version": "17.0.1.2.0",
    "summary": "Odoo Enterprise-style main menu and navigation module.",
    "description": """
        This module brings an enterprise-inspired backend experience to Odoo Community Edition.
        It provides a centralized main menu for fast access to core modules, a clean dark-mode layout,
        widget support for date and announcements, and bookmark shortcuts for internal menus or external links.
    """,
    "author": "NexOrionis Techsphere",
    "maintainer": "NexOrionis Techsphere",
    "website": "https://nexorionis.odoo.com/",
    "support": "nexorionis.info@gmail.com",
    "license": "LGPL-3",
    "category": "Technical/Technical",
    "currency": "USD",
    "price": 5.0,
    "depends": [
        "mail",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/main_menu_views.xml",
        "views/dark_mode_views.xml",
        "views/menu_bookmark_views.xml",
        "views/res_config_setting_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "noi_backend_theme/static/src/components/**/*",
        ],
        "web.report_assets_common": [
            "noi_backend_theme/static/src/js/report_dark_mode.js",
            "noi_backend_theme/static/src/scss/dark_mode_backend/theme.scss",
        ],
        "web.report_assets_pdf": [
            "noi_backend_theme/static/src/js/report_dark_mode.js",
            "noi_backend_theme/static/src/scss/dark_mode_backend/theme.scss",
        ],
        "web.assets_web_dark": [
            "noi_backend_theme/static/src/scss/dark_mode_backend/theme_accent.scss",
            "noi_backend_theme/static/src/scss/dark_mode_backend/datetimepicker.scss",
            "noi_backend_theme/static/src/scss/dark_mode_backend/noi_dark_theme.scss",
        ],
    },
    "images": [
        "static/description/banner.png",
        "static/description/icon.png",
        "static/description/dark_mode_icon_place.png",
        "static/description/after_change_dark_mode.png",
        "static/description/white_theme_search_bar.png",
        "static/description/white_theme_search_bar_useage.png",
        "static/description/dark_mode_view.png",
        "static/description/dark_mode_story.gif",
    ],
    "auto_install": False,
}
