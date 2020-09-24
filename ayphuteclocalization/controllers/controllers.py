# -*- coding: utf-8 -*-
# from odoo import http


# class Ayphuteclocalization(http.Controller):
#     @http.route('/ayphuteclocalization/ayphuteclocalization/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ayphuteclocalization/ayphuteclocalization/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ayphuteclocalization.listing', {
#             'root': '/ayphuteclocalization/ayphuteclocalization',
#             'objects': http.request.env['ayphuteclocalization.ayphuteclocalization'].search([]),
#         })

#     @http.route('/ayphuteclocalization/ayphuteclocalization/objects/<model("ayphuteclocalization.ayphuteclocalization"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ayphuteclocalization.object', {
#             'object': obj
#         })
