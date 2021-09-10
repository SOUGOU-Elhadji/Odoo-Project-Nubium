# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class EquipementProduction(models.Model):

    _name = 'equipement.production'
    _rec_name = 'nom'

    # INFORMATIONS GENERALES

    nom = fields.Char('Nom', required=True)
    numero_travail = fields.Char('Numéro de travail')
    type = fields.Selection([
        ('outil', 'Outil attelé')
    ], string="Type")
    date_mis_service = fields.Datetime('Mis en service le')
    date_mis_robut = fields.Datetime('Mis au rebut le')
    libelle_id = fields.Many2one('create.etiquette', required=True, string="Libellé")
    proprietaire_initial_id = fields.Many2one('create.prescripteur', string="Propriétaire initial")
    # lieu_stockage_id = fields.Many2one('create.lieu', string="Lieu de stockage")
    geolocalisation = fields.Char('Géolocalisation')
    piece_jointe = fields.Binary('Ajouter une pièce jointe')

    # IDENTIFICATION
    photo = fields.Binary('Photo')
    description = fields.Text('Description')

    # INDICATEURS
    largeur = fields.Char('Largeur de travail')
    mesure = fields.Selection([
        ('metre', 'Mètre'),
        ('centimetre', 'Centimètre'),
        ('kilometre', 'Kilomètre'),
        ('millimetre', 'Millimètre'),
    ], default="metre", string="Mesure")
    # image = fields.Binary(string="Image", attachment=True)