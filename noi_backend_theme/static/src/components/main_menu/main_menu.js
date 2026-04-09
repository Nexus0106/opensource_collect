/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { Component, onWillStart, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { WidgetHour } from "@noi_backend_theme/components/widget_hour/widget_hour";
import { WidgetAnnouncement } from "@noi_backend_theme/components/widget_announcement/widget_announcement";
import { standardActionServiceProps } from "@web/webclient/actions/action_service";

function isDarkTheme() {
    return document.documentElement.classList.contains("o_main_menu_dark");
}

class MenuAction extends Component {
    static components = { WidgetHour, WidgetAnnouncement };
    static props = {...standardActionServiceProps};
    static template = "noi_backend_theme.MainMenu";

    setup(){
        this.state = useState({ search: "" });
        this.action = useService("action");
        this.rpc = useService("rpc");
        this.menuService = useService("menu");
        this.company = useService("company").currentCompany.id
        this.searchPlaceholder = _t("Search menus");
        this.noMenusFound = _t("No menus found");

        this.apps = this.menuService.getApps()
                        .filter(app => app.xmlid != "noi_backend_theme.main_menu_root")
                        .sort((a, b) => a.name.localeCompare(b.name));
        const rootMenus = this.menuService.getMenuAsTree("root");
        this.allMenus = this.flattenMenus(rootMenus.childrenTree || rootMenus.children)
            .filter(menu => menu.xmlid != "noi_backend_theme.main_menu_root")
            .sort((a, b) => a.searchPath.localeCompare(b.searchPath));

        onWillStart(async () => {
            try {
                const {showWidgets, announcement, userIsAdmin} = await this.rpc("/noi_backend_theme/announcement", {company_id: this.company});
                this.showWidgets = showWidgets;
                this.announcement = announcement;
                this.userIsAdmin = userIsAdmin;
            } catch (error){
                console.error("Error loading data:", error);
            }
        });
    }

    flattenMenus(menus, parentNames = []) {
        return (menus || []).flatMap(menu => {
            const searchPath = [...parentNames, menu.name].filter(Boolean).join(" / ");
            return [
                {
                    ...menu,
                    searchPath,
                },
                ...this.flattenMenus(menu.childrenTree || menu.children, [...parentNames, menu.name]),
            ];
        });
    }

    onClickModule(menu){
        if (menu){
            if (!menu.actionID) {
                this.action.doAction("noi_backend_theme.main_menu_action", { clearBreadcrumbs: true });
                return;
            }
            this.menuService.selectMenu(menu);
        }
    }

    get visibleMenus() {
        const search = this.state.search.trim().toLowerCase();
        if (!search) {
            return this.apps;
        }

        return this.allMenus.filter(menu => {
            const name = (menu.name || "").toLowerCase();
            const path = (menu.searchPath || "").toLowerCase();
            const xmlid = (menu.xmlid || "").toLowerCase();
            return name.includes(search) || path.includes(search) || xmlid.includes(search);
        });
    }

    get backgroundStyle() {
        return `background: var(--mm-main-menu-background, ${isDarkTheme() ? "#1f202b" : "linear-gradient(135deg, #f7f8fc 0%, #ebe7f6 48%, #f3f5fb 100%)"})`;
    }

    get cornerAngle(){
        const angle = 90 + 180 * Math.atan(window.innerHeight / window.innerWidth) / Math.PI;
        return `${angle}deg`;
    }
}

registry.category("actions").add("noi_backend_theme.action_open_main_menu", MenuAction);
