import logging
import simplejson
import os
import openerp

from openerp.addons.web.controllers.main import manifest_list, module_boot, html_template

import openerp.addons.web.http as openerpweb


import logging

l = logging.getLogger(__name__)

class InvoiceController(openerp.addons.web.http.Controller):
    _cp_path = '/invoice'

    @openerpweb.jsonrequest
    def bill(self, req, **params):
        return {'title': "test"}
