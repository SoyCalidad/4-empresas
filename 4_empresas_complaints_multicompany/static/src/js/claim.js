odoo.define('tu_modulo.complainer_form', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');

    publicWidget.registry.ComplainerForm = publicWidget.Widget.extend({
        selector: '.js_complainer_delivery_type',

        events: {
            'change': '_onChangeDeliveryType',
        },

        _onChangeDeliveryType: function (ev) {
            var value = ev.currentTarget.value;

            var $email = $('#hidden_email');
            var $phone = $('#hidden_phone');

            $email.hide();
            $phone.hide();

            console.log("value", value)

            if (value === 'Quiero recibirla por correo electronico') {
                $email.show();
            } else if (value === 'Quiero recibirla por celular') {
                $phone.show();
            }
        },
    });
});
