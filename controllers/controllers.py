# -*- coding: utf-8 -*-
# from odoo import http


# class ConduiteChangement(http.Controller):
#     @http.route('/conduite_changement/conduite_changement/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/conduite_changement/conduite_changement/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('conduite_changement.listing', {
#             'root': '/conduite_changement/conduite_changement',
#             'objects': http.request.env['conduite_changement.conduite_changement'].search([]),
#         })

#     @http.route('/conduite_changement/conduite_changement/objects/<model("conduite_changement.conduite_changement"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('conduite_changement.object', {
#             'object': obj
#         })
