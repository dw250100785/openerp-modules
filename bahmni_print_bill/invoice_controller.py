import logging
import simplejson
import os
import openerp

from openerp.modules.registry import RegistryManager
from openerp.addons.web.controllers.main import manifest_list, module_boot, html_template
from openerp import pooler, tools

import openerp.addons.web.http as openerpweb


import logging

l = logging.getLogger(__name__)

class InvoiceController(openerp.addons.web.http.Controller):
    _cp_path = '/invoice'

    @openerpweb.jsonrequest
    def bill(self, req, voucher_id):
        uid = req.session._uid
        dbname = req.session._db
        context = req.session.context
        registry = RegistryManager.get(dbname)
        with registry.cursor() as cr:
            pool = pooler.get_pool(dbname)
            account_voucher_obj = registry.get('account.voucher')
            voucher = account_voucher_obj.browse(cr, uid, voucher_id, context=context)

            voucher_line_ids = sorted(voucher.line_ids, key=lambda v: v.id,reverse=True)
            invoice = None
            for voucher_line in voucher_line_ids:
                if(voucher_line.type == 'cr'):
                    inv_no = voucher_line.name
                    inv_ids = pool.get("account.invoice").search(cr, uid,[('number','=',inv_no)])
                    if(inv_ids and len(inv_ids) > 0):
                        inv_id = inv_ids[0]
                        invoice = pool.get("account.invoice").browse(cr,uid,inv_id,context=context)
                    break
            invoice_line_items = []
            for invoice_line_item in invoice.invoice_line:
                invoice_line_items.append({
                    'product_name': invoice_line_item.product_id.name,
                    'unit_price': invoice_line_item.price_unit,
                    'quantity': invoice_line_item.quantity,
                    'subtotal': invoice_line_item.price_subtotal,
                })
            bill = {
                'voucher_number': voucher.number,
                'voucher_date': voucher.date,
                'invoice_line_items': invoice_line_items,
                'new_charges': invoice.amount_total,
                'discount_head': invoice.discount_acc_id and invoice.discount_acc_id.name or None,
                'discount': invoice.discount,
                'net_amount': voucher.bill_amount,
                'previous_balance': voucher.balance_amount + voucher.amount - voucher.bill_amount,
                'bill_amount': voucher.amount + voucher.balance_amount,
                'paid_amount': voucher.amount,
                'balance_amount': voucher.balance_amount,
                'partner_name': voucher.partner_id.name,
                'partner_ref': voucher.partner_id.ref,
            }
            return bill
        return {}
