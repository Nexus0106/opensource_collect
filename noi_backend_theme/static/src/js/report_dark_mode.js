/** @odoo-module **/

const DARK_CLASS = "o_main_menu_dark";

function getCookie(name) {
    const match = document.cookie.match(new RegExp(`(?:^|;\\s*)${name}=([^;]*)`));
    return match ? decodeURIComponent(match[1]) : "";
}

function isDarkScheme() {
    const configured = getCookie("color_scheme") || getCookie("configured_color_scheme");
    return configured === "dark";
}

function applySchemeClass() {
    const isDark = isDarkScheme();
    document.documentElement.classList.toggle(DARK_CLASS, isDark);
    document.body?.classList?.toggle(DARK_CLASS, isDark);
    document.documentElement.dataset.bsTheme = isDark ? "dark" : "light";
    if (document.body) {
        document.body.dataset.bsTheme = isDark ? "dark" : "light";
    }
    document.documentElement.style.colorScheme = isDark ? "dark" : "light";
    if (document.body) {
        document.body.style.colorScheme = isDark ? "dark" : "light";
    }
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", applySchemeClass, { once: true });
} else {
    applySchemeClass();
}

window.addEventListener("load", applySchemeClass);
window.addEventListener("pageshow", applySchemeClass);
