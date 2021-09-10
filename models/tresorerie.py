# -*- coding: utf-8 -*-

from odoo import models, fields


class CreateTresorerie(models.Model):
    _name = 'create.tresorerie'
    _description = 'Create tresorerie'

    #ENREGISTRER UNE NOUVELLE TRESORERIE
    #INFORMATIONS GENERALES

    name = fields.Char('Nom', required=True)
    devise = fields.Selection([
        ('fcfa', 'Franc FCFA'),
        ('euro', 'Euro'),
        ('dollar', 'Dollar'),
    ], default="fcfa", string="Devise", required=True)
    compte_bancaire = fields.Boolean('Compte banciaire')
    caisse = fields.Boolean('Caisse')
    compte_courant = fields.Boolean("Compte courant d'associé")
    defaut = fields.Boolean('Par défaut')
    proprietaire_id = fields.Many2one('create.prescripteur', string="Propriétaire")

    #COMPTE BANCAIRE

    titulaire = fields.Char('Titulaire du compte')
    name_bank = fields.Char('Nom de la banque')
    address = fields.Text("Adresse de l'agence bancaire")
    iban_check = fields.Boolean('IBAN')
    releve = fields.Boolean("Relevé d'identité bancaire (RIB)")
    iban = fields.Char('IBAN')
    bic = fields.Char('BIC')
    pays = fields.Selection([
        ('senegal', 'Sénégal'),
        ('france', 'France'),
    ], default="senegal", string="Pays")
    code_b = fields.Char('Code banque')
    code_g = fields.Char('Code guichet')
    numero_co = fields.Char('Numéro compte bancaire')
    cle_rib = fields.Char('Clé RIB')

    #COMPTABILITE
    compte_principal = fields.Many2one('create.compte', string="Compte principal", required=True)
    journal = fields.Many2one('create.journal', string="Journal", required=True)
    reconciliation = fields.Boolean("Suspendre jusqu'à réconciliation")
    compte_attente = fields.Many2one('create.compte', string="Compte d'attente bancaire")
    compta_detail = fields.Boolean('Comptabiliser le détail du relevé')

    #PIECES JOINTES
    piece_j = fields.Binary('Choisir un fichier')


