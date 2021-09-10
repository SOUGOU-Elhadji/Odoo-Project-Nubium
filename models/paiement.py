# -*- coding: utf-8 -*-

from odoo import models, fields


class CreatePaiement(models.Model):
    _name = 'create.paiement'
    _description = 'Create PAIEMENT'

    #NOUVEAU MODE DE PAIEMENT
    #INFORMATIONS GENERALES

    nom = fields.Char('Nom', required=True)
    tresorerie_id = fields.Many2one('create.tresorerie', string="Trésorerie", required=True)
    comptabilite = fields.Boolean('Passer en comptabilité')
    sepa = fields.Boolean('SEPA')



