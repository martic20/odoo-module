# -*- coding: utf-8 -*-
from odoo import http

# class A1(http.Controller):
#     @http.route('/a1/a1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/a1/a1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('a1.listing', {
#             'root': '/a1/a1',
#             'objects': http.request.env['a1.a1'].search([]),
#         })

#     @http.route('/a1/a1/objects/<model("a1.a1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('a1.object', {
#             'object': obj
#         })