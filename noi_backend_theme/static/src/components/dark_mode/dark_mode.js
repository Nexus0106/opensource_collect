/** @odoo-module **/

import { markup } from "@odoo/owl";
import { _t } from "@web/core/l10n/translation";
import { cookie as cookieManager } from "@web/core/browser/cookie";
import { browser } from "@web/core/browser/browser";
import { escape } from "@web/core/utils/strings";
import { registry } from "@web/core/registry";

const DARK_CLASS = "o_main_menu_dark";

function getCurrentScheme(env) {
    return cookieManager.get("color_scheme") || env?.services?.color_scheme?.activeColorScheme || "light";
}

function applySchemeClass(scheme) {
    const isDark = scheme === "dark";
    document.documentElement.classList.toggle(DARK_CLASS, isDark);
    document.body?.classList?.toggle(DARK_CLASS, isDark);
    document.documentElement.dataset.bsTheme = isDark ? "dark" : "light";
    if (document.body) {
        document.body.dataset.bsTheme = isDark ? "dark" : "light";
    }
    document.documentElement.style.colorScheme = isDark ? "dark" : "light";
}

applySchemeClass(getCurrentScheme());

function toggleColorScheme(env) {
    const currentScheme = getCurrentScheme(env);
    const nextScheme = currentScheme === "dark" ? "light" : "dark";

    if (env?.services?.color_scheme?.switchToColorScheme) {
        env.services.color_scheme.switchToColorScheme(nextScheme);
        applySchemeClass(nextScheme);
        return;
    }

    cookieManager.set("configured_color_scheme", nextScheme);
    cookieManager.set("color_scheme", nextScheme);
    applySchemeClass(nextScheme);
    browser.location.reload();
}

function darkModeItem(env) {
    const isDark = getCurrentScheme(env) === "dark";
    const iconClass = isDark ? "fa fa-sun-o" : "fa fa-moon-o";
    const label = isDark ? _t("Light Mode") : _t("Dark Mode");

    return {
        type: "item",
        id: "noi_backend_theme.dark_mode",
        description: markup(
            `<div class="d-flex align-items-center">
                <i class="${iconClass} me-2"></i>
                <span>${escape(label)}</span>
            </div>`
        ),
        callback: () => toggleColorScheme(env),
        sequence: 35,
    };
}

registry.category("user_menuitems").add("noi_backend_theme.dark_mode", darkModeItem);
