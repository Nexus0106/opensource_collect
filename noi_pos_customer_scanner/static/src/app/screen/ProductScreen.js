/** @odoo-module **/
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { patch } from "@web/core/utils/patch";

patch(ProductScreen.prototype, {
    setup() {
        super.setup(...arguments);
    },
    async _barcodeProductAction(code) {
        const product = await this._getProductByBarcode(code);
        if (!product) {
            const partner = await this._getPartnerByBarcode(code);
            if (partner) {
                if (this.currentOrder.get_partner() !== partner) {
                    this.currentOrder.set_partner(partner);
                }
                return;
            }
            return this.popup.add(ErrorBarcodePopup, { code: code.base_code });
        }

        const options = await product.getAddProductOptions(code);
        // Do not proceed on adding the product when no options is returned.
        // This is consistent with clickProduct.
        if (!options) {
            return;
        }

        // update the options depending on the type of the scanned code
        if (code.type === "price") {
            Object.assign(options, {
                price: code.value,
                extras: {
                    price_type: "manual",
                },
            });
        } else if (code.type === "weight" || code.type === "quantity") {
            Object.assign(options, {
                quantity: code.value,
                merge: false,
            });
        } else if (code.type === "discount") {
            Object.assign(options, {
                discount: code.value,
                merge: false,
            });
        }
        this.currentOrder.add_product(product, options);
        this.numberBuffer.reset();



    },
});
