/* @odoo-module */

import { ListRenderer } from "@web/views/list/list_renderer";
import { patch } from "@web/core/utils/patch";

patch(ListRenderer.prototype, {
    freezeColumnWidths() {
        const table = this.tableRef.el;
        const headerRow = table.querySelector("thead tr");

        if (headerRow) {
            // Find the first <th> (this is the selector column header if hasSelectors=true)
            const firstTh = headerRow.querySelector("th");
            // Check if our header already exists
            if (firstTh && !headerRow.querySelector(".o_list_row_count_sheliya")) {
                const th = document.createElement("th");
                th.className = "o_list_row_number_header o_list_row_count_sheliya";
                th.style.width = "1%";
                th.textContent = "No.";
                th.style.textAlign = "left";
                // Insert AFTER the first <th> (i.e., after checkbox header)
                const selectorTh = headerRow.querySelector("th.o_list_record_selector");
                console.log('AAA',firstTh)
                console.log('BBBB',selectorTh)
                if(selectorTh){
                    firstTh.after(th);
                }else{
                    firstTh.before(th);
                }

            }
        }

        const footerRow = table.querySelector("tfoot tr");
        if (footerRow) {
            const firstTd = footerRow.querySelector("td");
            if (firstTd && !footerRow.querySelector(".o_list_row_count_sheliya")) {
                const td = document.createElement("td");
                td.className = "o_list_row_count_sheliya";
                td.style.textAlign = "left";
                firstTd.after(td);
            }
        }

        return super.freezeColumnWidths();
    },
});