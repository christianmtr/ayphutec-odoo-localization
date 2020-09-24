# -*- coding: utf-8 -*-
# from odoo import http


# class Ayphutec-localization(http.Controller):
#     @http.route('/ayphutec-localization/ayphutec-localization/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ayphutec-localization/ayphutec-localization/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ayphutec-localization.listing', {
#             'root': '/ayphutec-localization/ayphutec-localization',
#             'objects': http.request.env['ayphutec-localization.ayphutec-localization'].search([]),
#         })

#     @http.route('/ayphutec-localization/ayphutec-localization/objects/<model("ayphutec-localization.ayphutec-localization"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ayphutec-localization.object', {
#             'object': obj
#         })
