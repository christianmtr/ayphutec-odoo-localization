# -*- coding: utf-8 -*-
# from odoo import http


# class Ayphu-contable(http.Controller):
#     @http.route('/ayphu-contable/ayphu-contable/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ayphu-contable/ayphu-contable/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ayphu-contable.listing', {
#             'root': '/ayphu-contable/ayphu-contable',
#             'objects': http.request.env['ayphu-contable.ayphu-contable'].search([]),
#         })

#     @http.route('/ayphu-contable/ayphu-contable/objects/<model("ayphu-contable.ayphu-contable"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ayphu-contable.object', {
#             'object': obj
#         })
