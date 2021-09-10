# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class AnalyseQualite(models.Model):

    _name = 'analyse.qualite'
    _rec_name = 'type'

    type = fields.Selection([
        ('lait_vache', 'Analyse de lait de vache'),
        ('grain', 'Analyse de grain'),
        ('meteorologique', 'Analyse météorologique'),
        ('culture', "Analyse d'une culture"),
        ('capteur', 'Analyse capteur'),
        ('ensilage', "Analyse d'ensilage"),
        ('sol', 'Analyse de sol'),
        ('control', "Analyse d'un controle laitier"),
        ('vendange', 'Analyse de vendange'),
        ('eau', "Analyse d'eau"),
    ], string="Nouveau")
    number = fields.Char('Numéro', required=True)
    number_ref = fields.Char('Numéro référence')
    date = fields.Datetime('Prélevé le', required=True)
    geolocalisation = fields.Char('Géolocalisation')
    # preleveur = fields.Many2one('create.prescripteur', string="Préleveur")
    date_analyse = fields.Datetime('Analysé le')
    # analyseur = fields.Many2one('create.prescripteur', string="Analyseur")
    produit = fields.Many2one('create.produit', string="Produit")

    #ELEMENTS
    code_pays = fields.Char("Code pays d'origine")
    element = fields.Selection([
        ('lait_vache', 'Analyse de lait de vache'),
        ('grain', 'Analyse de grain'),
        ('meteorologique', 'Analyse météorologique'),
        ('culture', "Analyse d'une culture"),
        ('capteur', 'Analyse capteur'),
        ('ensilage', "Analyse d'ensilage"),
        ('sol', 'Analyse de sol'),
        ('control', "Analyse d'un controle laitier"),
        ('vendange', 'Analyse de vendange'),
        ('eau', "Analyse d'eau"),
    ], string="Ajouter un élément")

    #PIECE JOINTE
    piece_jointe = fields.Binary('Ajouter une pièce jointe')

    image = fields.Binary(string="Image", attachment=True)