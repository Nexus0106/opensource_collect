odoo.define('noi_pos_customer_scanner.ProductScreen', function(require){
    'use strict';

    var ProductScreen = require('point_of_sale.ProductScreen');
    var Registries = require('point_of_sale.Registries');
//    const { useBarcodeReader } = require('point_of_sale.custom_hooks');


    const ProductScreenExtend = ProductScreen => class extends ProductScreen{
        constructor() {
            super(...arguments);
        }

        async _barcodeProductAction(code) {
                let product = this.env.pos.db.get_product_by_barcode(code.base_code);
                let partner = this.env.pos.db.get_partner_by_barcode(code.base_code);
                if (!product && !partner) {
                    // find the barcode in the backend
                    let foundProductIds = [];
                    let foundPartnerIds = [];
                    try {
                        foundProductIds = await this.rpc({
                            model: 'product.product',
                            method: 'search',
                            args: [[['barcode', '=', code.base_code]]],
                            context: this.env.session.user_context,
                        });

                        foundPartnerIds = await this.rpc({
                            model: 'res.partner',
                            method: 'search',
                            args: [[['barcode', '=', code.base_code]]],
                            context: this.env.session.user_context,
                        });
                    } catch (error) {
                        if (isConnectionError(error)) {
                            return this.showPopup('OfflineErrorPopup', {
                                title: this.env._t('Network Error'),
                                body: this.env._t("Product is not loaded. Tried loading the product from the server but there is a network error."),
                            });
                        } else {
                            throw error;
                        }
                    }
                    if (foundProductIds.length) {
                        await this.env.pos._addProducts(foundProductIds);
                        // assume that the result is unique.
                        product = this.env.pos.db.get_product_by_id(foundProductIds[0]);
                    }else if (foundPartnerIds){
                        await this.currentOrder.set_client(foundPartnerIds)
                        partner = this.env.pos.db.get_partner_by_id(foundPartnerIds[0]);
                    }
                     else {
                        return this._barcodeErrorAction(code);
                    }
                }
                if(product){
                    const options = await this._getAddProductOptions(product, code);
                    // Do not proceed on adding the product when no options is returned.
                    // This is consistent with _clickProduct.
                    if (!options) return;

                    // update the options depending on the type of the scanned code
                    if (code.type === 'price') {
                        Object.assign(options, {
                            price: code.value,
                            extras: {
                                price_manually_set: true,
                            },
                        });
                    } else if (code.type === 'weight') {
                        Object.assign(options, {
                            quantity: code.value,
                            merge: false,
                        });
                    } else if (code.type === 'discount') {
                        Object.assign(options, {
                            discount: code.value,
                            merge: false,
                        });
                    }
                    await this.currentOrder.add_product(product,  options);
                }
                if(partner){
                        await this.currentOrder.set_client(partner);
                }
            }

        }

        Registries.Component.extend(ProductScreen, ProductScreenExtend);

        return ProductScreenExtend;

});

