openerp.bahmni_sale_discount = function(instance) {

    var QWeb = instance.web.qweb;
    instance.bahmni_sale_discount.print = instance.web.form.FieldChar.extend({
        template: "test_button",
        init: function() {
            this._super.apply(this, arguments);
             this._start = null;
             console.log('INIT');
       },

       start: function() {
             console.log('START');   
             $('button#bstart').click(this.myfunction);  //link button to function  
        },

        myfunction: function() {
            var $ht = $(QWeb.render("Bill"))[0];
            var hiddenFrame = $("#printBillFrame")[0]
    
            var doc = hiddenFrame.contentWindow.document.open("text/html", "replace");

            doc.write($ht.innerHTML);
            doc.close();
            hiddenFrame.contentWindow.print();

            // $ht.print();
        },
    });

    instance.web.form.widgets.add('print', 'instance.bahmni_sale_discount.print');
}