/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, useRef } from "@odoo/owl";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

export class NoiColorPickerField extends Component {
    static template = "noi_color_picker.ColorPickerField";
    static props = {
        ...standardFieldProps,
    };

    setup() {
        this.inputRef = useRef("colorInput");
    }

    get colorValue() {
        return this.props.record.data[this.props.name] || "#000000";
    }

    get isReadonly() {
        return this.props.readonly;
    }

    onColorChange(ev) {
        const color = ev.target.value;
        this.props.record.update({ [this.props.name]: color });
    }
}

export const noiColorPickerField = {
    component: NoiColorPickerField,
    supportedTypes: ["char"],
    extractProps: ({ attrs }) => ({}),
};

registry.category("fields").add("noi_color_picker", noiColorPickerField);
