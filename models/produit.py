# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class CreateProduit(models.Model):

    _name = 'create.produit'
    _rec_name = 'nom'

    nom = fields.Char(string="Variante", required=True)
    numero = fields.Char('Numéro', required="True")
    actif = fields.Boolean('Actif')
    variete = fields.Selection([
        ('abeille', 'Abeille'),
        ('abiu', 'Abiu'),
        ('abricotier', 'Abricotier Abricot Muscat de Clairac'),
        ('nancy', 'Abricotier Abricot Nancy de Clairac'),
        ('peche', 'Abricotier Abricot Pêche de Nancy'),
        ('commun', 'Abricotier Abricot commun de Clairac'),
    ], string="Variété", required=True)

    unitaire = fields.Boolean('Unitaire')
    entier = fields.Boolean('Entier')
    decimal = fields.Boolean('Décimal')
    photo = fields.Binary('Photo')
    abonnement = fields.Boolean('Abonnement')
    type_id = fields.Many2one('create.type', string="Type d'abonnement")
    nombre_annee = fields.Char("Nombre d'années d'abonnement")
    nombre_mois = fields.Char("Nombre de mois d'abonnement")
    nombre_jour = fields.Char("Nombre de jours d'abonnement")
    description = fields.Text('Description')

    #DEFINITION
    liste_competence = fields.Selection([
        ('acidifier', 'Acidifier'),
        ('administrer', 'Administrer des inséminations'),
        ('soins', 'Administrer des soins'),
        ('alcaliniser', 'Alcaliniser'),
        ('attacher', 'Attacher'),
        ('atteler', 'Atteler'),
        ('biner', 'Biner'),
        ('boteller', 'Boteller'),
    ], string="Liste des compétences")

    #liste des indicateurs fixes
    acidite = fields.Boolean('Acidité totale')
    appelation_certi = fields.Boolean('Appellation / Certification')
    avortement = fields.Boolean('Avortement')
    bonne_sante = fields.Boolean('Bonne santé')
    calibre = fields.Boolean('Calibre')

    # liste des indicateurs variables
    a_totale = fields.Boolean('Acidité totale')
    appelation_cert = fields.Boolean('Appellation / Certification')
    avorte = fields.Boolean('Avortement')
    bonne_sant = fields.Boolean('Bonne santé')
    calibr = fields.Boolean('Calibre')

    #Points d’attache
    arriere = fields.Boolean('Arrière')
    avant = fields.Boolean('Avant')

class new_variable(models.Model):
    _name = 'new.variable'
    _rec_name = 'type_new_id'

    type_new_id = fields.Many2one('create.produit', required=True, string="Type")

class type(models.Model):
    _name = 'create.type'
    _rec_name = 'nom'

    nom = fields.Char('Nom', required=True)
    description = fields.Text('Description')

    # def name_get(self):
    #     result = []
    #     for rec in self:
    #         name = rec.variant + ' ' + rec.type
    #         result.append(rec.id, name)
    #         return result

