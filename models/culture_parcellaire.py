# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class CultureParcellaire(models.Model):

    _name = 'culture.parcellaire'
    _rec_name = 'name'

    name = fields.Char('Nom')
    numero_travail = fields.Char('Numéro de travail')
    date_debut = fields.Datetime('A partir')
    date_fin = fields.Date('Au')
    incident = fields.Many2one('incidence.qualite', string="Incident")
    description = fields.Text('Description')
    probleme = fields.Boolean("Problème durant l'intervension")
    description_probleme = fields.Char('Description du problème')
    intrui = fields.Char()
    compteur = fields.Char("Compteur d'eau")
    # prescription = fields.Many2one('create.prescription', string="Prescription")
    # libelle = fields.Many2one('create.etiquette', string="Libellé", required=True)
    parcelle = fields.Many2one('parcelle.parcellaire', string="Parcelle", required=True)
    zone_travaille = fields.Char('Zone Travaillée')
    image = fields.Binary(string="Image", attachment=True)
