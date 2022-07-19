# -*- coding: utf-8 -*-

from email.policy import default
from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE
import string
from tokenize import String
from odoo import models, fields, api, _
from datetime import datetime


class Registre(models.Model):
    _name = 'registre_pp.registre'
    _description = 'registre_pp.registre'

    
    idReg = fields.Char(string="Numéro de registre", default=lambda self: self.env['ir.sequence'].next_by_code('increment_your_field'))
    date = fields.Date(string="Date de création", default=datetime.today())
    dateV = fields.Date(string="Date de la version", default=datetime.today())
    numV = fields.Integer(string="Numéro de la version")
    project_id = fields.Many2one('project.project', string="Nom du projet associé")
    partie_prenante_id = fields.One2many('conduite_changement.gestion_partie_prenante', 'registre_id')

    @api.model
    def create(self, vals):
        if vals.get('idReg', _('New')) == _('New'):
            vals['idReg'] = self.env['ir.sequence'].next_by_code('registre_pp.registre') or _('New')
        res = super(Registre, self).create(vals)
        return res




class partie_prenante(models.Model):
     _name = 'conduite_changement.gestion_partie_prenante'
     _description = 'conduite_changement.gestion_partie_prenante'

     registre_id = fields.Many2one('registre_pp.registre', string="Liste des parties prenantes")
     partner_id = fields.Many2one('res.partner', string="Nom", required=True)
     identifiant = fields.Char(string="ID", default=lambda self: self.env['ir.sequence'].next_by_code('increment_your_field_identifiant'))
     type = fields.Selection([('i','Interne'),('e','Externe')],string="Type", required=True)
     role = fields.Char(string="Role", required=True)
     interet = fields.Selection([('f','Faible'),('el','Elevé')],string="Interet", required=True)
     pouvoir = fields.Selection([('f','Faible'),('el','Elevé')],string="Pouvoir", required=True)
     #strategie = fields.Char(string="Stratégie", required=True)
     strategie = fields.Selection([('ac', 'Acteur clé'), ('gi', 'Garder informé'), ('em', 'Effort minimum'), ('gs', 'Garder satisfait')],string="Stratégie")
     contribution = fields.Char(string="Contribution", required=True)
     attentes = fields.Char(string="Attentes", required=True)
     actions = fields.Text(string="Actions", required=True)
     engagement = fields.Selection([('i', 'Inconscient'), ('r', 'Résistant'), ('n', 'Neutre'), ('s', 'Supporteur'), ('l', 'Leader')], string="Engagement")
     email = fields.Char(string="Email", compute="_compute_email")

     @api.depends("partner_id.email")
     def _compute_email(self):
         for record in self:
                record.email = record.partner_id.email
           


     @api.onchange("pouvoir","interet") # if these fields are changed, call method
     def check_change(self):
        for rec in self:
            if (rec.pouvoir == "f" and rec.interet == "f") :
                rec.strategie = "em"
            elif (rec.pouvoir == "el" and rec.interet == "f"):
                rec.strategie = "gs" 
            elif (rec.pouvoir == "f" and rec.interet == "el"):
                rec.strategie = "gi" 
            else:
                rec.strategie = "ac" 