# -*- coding: utf-8 -*-

from odoo import models, fields


class CreateCompte(models.Model):
    _name = 'create.compte'
    _description = 'Create compte'

    #NOUVELLE COMPTE
    #INFORMATIONS GENERALE

    general = fields.Boolean('Général')
    auxiliaire = fields.Boolean('Auxiliaire')
    numero_c = fields.Char('Numéro', required=True)
    compte_contralisateur = fields.Selection([
        ('reception', 'à réception'),
        ('30jour', '30 jours'),
    ], string="Compte centralisateur")
    numero_auxiliaire = fields.Char('Numéro auxiliaire', required=True)
    nom = fields.Char('Nom', required=True)
    description = fields.Text('Description')
    usager = fields.Selection([
        ('1comptecap', '1 - Comptes des capitaux'),
        ('101capital', '101 - Capital'),
    ], string="Usagers")