# -*- coding: utf-8 -*-
from odoo import http

# class Discoteca(http.Controller):
#     @http.route('/discoteca/discoteca/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/discoteca/discoteca/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('discoteca.listing', {
#             'root': '/discoteca/discoteca',
#             'objects': http.request.env['discoteca.discoteca'].search([]),
#         })

#     @http.route('/discoteca/discoteca/objects/<model("discoteca.discoteca"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('discoteca.object', {
#             'object': obj
#         })