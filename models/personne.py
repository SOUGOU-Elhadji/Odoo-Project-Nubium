# -*- coding: utf-8 -*-

from odoo import models, fields


class CreatePersonne(models.Model):
    _name = 'create.personne'
    _description = 'Create personne'

    #NOUVEAU CONTACT
    #INFORMATIONS GENERALES

    titre = fields.Char('Titre')
    prenom = fields.Char('Prénom')
    nom_famille = fields.Char('Nom de famille', required=True)
    numero_siret = fields.Char('N° SIRET')
    numero = fields.Char('Numéro', placeholder="000000071")
    secteur_geo = fields.Text('Secteur géographique')
    langue = fields.Selection([
        ('francais', 'francais'),
        ('anglais', 'anglais'),
        ('allemand', 'allemand'),
    ], default="francais", string="Langue", required=True)
    active = fields.Boolean('Active')
    date_naissance = fields.Date('Date de naissance')
    date_dece = fields.Datetime('Date de décès')
    description = fields.Text('Description')
    photo = fields.Binary('Choisir un fichier')
    # prescripteur_id = fields.Many2one('create.prescripteur', string="Prescripteur", required=True)
    email = fields.Char('Email', required=True)
    nom_societe = fields.Char('Nom ou Société')
    destinataire_service = fields.Char('Destinataire - Service')
    bat_res_zl = fields.Char('Bat - Res - Zl')
    numero_libelle = fields.Char('Numéro et libellé de la voie')
    mention_speciale = fields.Char('Mention spéciale - Lieu dit')
    code_postal = fields.Char('Code postal ET ville')
    pays = fields.Selection([
        ('senegal', 'Sénégal'),
        ('france', 'France'),
    ], default="senegal", string="Pays")
    numero_fix = fields.Char('Téléphone Fixe', required=True)
    numero_portable = fields.Char('Téléphone portable', required=True)
    fax = fields.Char('Fax', required=True)
    site_web = fields.Char('Site Web', required=True)

    #INFORMATION CLIENT
    prospect = fields.Boolean('Prospect')
    client = fields.Boolean('Client')
    origine_rencontre = fields.Char('Origine de la rencontre')
    date_rencontre = fields.Datetime('Date de la première rencontre')
    parrain_id = fields.Many2one('create.parrain', string="Parrain")
    responsable_id = fields.Many2one('create.responsable', string="Responsable")
    assujetti_tva = fields.Boolean('Assujetti à la TVA')
    relance = fields.Boolean('Soumis à la relance')
    nombre_encaissement = fields.Integer("Nombre d'encaissements autorisé")
    condition_livr = fields.Text('Condition de livraison')
    compte_client_id = fields.Many2one('create.compte', string="Compte client associé")

    #INFORMATIONS FOURNISSEUR
    fournisseur = fields.Boolean('Fournisseur')
    compte_fournisseur_id = fields.Many2one('create.compte', string="Compte fournisseur associé")
    delais = fields.Selection([
        ('reception', 'à réception'),
        ('30jour', '30 jours'),
        ('30jourfinmois', '30 jours du mois'),
        ('60jour', '60 jours'),
        ('60jourfinmois', '60 jours du mois'),
    ], default="francais", string="Délai de paiement fournisseur")
    paiement_id = fields.Many2one('create.paiement', string="Mode de paiement")
    transporteur = fields.Boolean('Transporteur')

    #COMPTE BANCAIRE
    titulaire = fields.Char('Titulaire du compte')
    bic = fields.Char('BIC')
    iban = fields.Char('IBAN')

    #INFORMATIONS SOCIALES
    employe_associe = fields.Boolean('Employé / Associé')
    compte_employe_associe = fields.Many2one('create.compte', string="Compte employé / associé")

    #PIECES JOINTES
    piece_j = fields.Binary('Choisir un fichier')


