odoo.define('noi_hide_delete_action.HideAction', function (require) {
    "use strict";

    const BasicModel = require('web.BasicModel');
    const FormController = require('web.FormController');
    const ListController = require('web.ListController');
    var core = require('web.core');
    var _t = core._t;

    BasicModel.include({
        _load: function() {
            var self = this;
            var defs = []
            defs.push(this._super(...arguments));
            defs.push(this.getSession().user_has_group('noi_hide_delete_action.group_hide_delete_button').then(
                result => self.hide_delete_button = result
            ));
            return $.when(...defs);
        }
    })

    FormController.include({
        _getActionMenuItems: function (state) {
            let values = this._super.apply(this, arguments);
            let deleteString = _t("Delete");
            if(values && this.model.hide_delete_button) {
                let deleteMenuItem =values.items.other.find(item => {return (item.description === deleteString)});
                if(deleteMenuItem){
                    deleteMenuItem.separator = true; // Add this line to hide the menu item
                    deleteMenuItem.class += ' o_hidden'; // Add this line to hide the menu item
                     // Remove the deleteMenuItem from the values.items.other array
                    values.items.other = values.items.other.filter(item => item.description !== deleteString);
                }
            }
            return values;
        }
    });

    ListController.include({
        _getActionMenuItems: function (state) {
            let values = this._super.apply(this, arguments);
            if (!this.hasActionMenus || !this.selectedRecords.length) {
                return values;
            }
            let deleteString = _t("Delete");

            if(this.model.hide_delete_button) {
                let deleteMenuItem =values.items.other.find(item => {return (item.description === deleteString)});
                if(deleteMenuItem){
                    deleteMenuItem.separator = true; // Add this line to hide the menu item
                    deleteMenuItem.class += ' o_hidden'; // Add this line to hide the menu item
                     // Remove the deleteMenuItem from the values.items.other array
                    values.items.other = values.items.other.filter(item => item.description !== deleteString);
                }

            }
            return values;
        }
    });

});
