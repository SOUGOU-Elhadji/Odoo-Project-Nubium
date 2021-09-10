# -*- coding: utf-8 -*-

from odoo import models, fields


class CreateTresorerie(models.Model):
    _name = 'create.journal'
    _description = 'Create tresorerie'

    #NOUVEAU JOURNAL
    #INFORMATIONS GENERALES

    name = fields.Char('Nom', required=True)
    code = fields.Char('Code')
    devise = fields.Selection([
        ('fcfa', 'Franc FCFA'),
        ('euro', 'Euro'),
        ('dollar', 'Dollar'),
    ], default="fcfa", string="Devise", required=True)
    ventes = fields.Boolean('Ventes')
    achat = fields.Boolean('Achats')
    immobilisation = fields.Boolean('Immobilisations')
    banque = fields.Boolean('Banque')
    report = fields.Boolean('Report à nouveau')
    operation = fields.Boolean('Opérations diverses')
    caisse = fields.Boolean("Caisse")
    reserve = fields.Boolean('Réserves')
    cloture = fields.Boolean('Clotures')
    resultat = fields.Boolean('Résultat')
    comptable_id = fields.Many2one('create.prescripteur', string="Propriétaire")
    ecart = fields.Boolean("Utilisé pour les écarts")
    inventaire = fields.Boolean("Utilisé pour l'inventaire de stock")
    facture = fields.Boolean("Utilisé pour factures non parvenues")
    code_isacompta = fields.Char('Code isacompta')
    libelle_isacompta = fields.Char('Libellé isacompta')
