# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class ParcelleParcellaire(models.Model):
    _name = 'parcelle.parcellaire'
    _rec_name = 'date_debut_travaux'

    date_debut_travaux = fields.Date('Début des travaux sur la parcelle', required=True)
    a_partir = fields.Selection([
        ('2020', '2020'),
        ('2021', '2021'),
        ('2022', '2022'),
        ('2023', '2023'),
        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026'),
        ('2027', '2027'),
        ('2028', '2028'),
        ('2029', '2029'),
        ('2030', '2030'),
        ('2031', '2031'),
        ('2032', '2032'),
    ], default="2020", string='A partir de', required=True)
    end_date = fields.Date("Jusqu'au", required=True)
    prod_ref = fields.Char('Production de référence')
    utilisation = fields.Selection([
        ('Bois', 'Bois'),
        ('Ensilage', 'Ensilage'),
        ('Fibre', 'Fibre'),
        ('Fleur', 'Fleur'),
        ('Foin', 'Foin'),
        ('Fourrage', 'Fourrage'),
        ('Fruit', 'Fruit'),
        ('Grain', 'Grain'),
        ('Jachere', 'Jachère'),
        ('Legume', 'Légume'),
        ('Paille', 'Paille'),
        ('Plant', 'Plant'),
        ('Prairie', 'Prairie'),
        ('Racine', 'Racine'),
        ('Sel', 'Sel'),
        ('Semence', 'Semence'),
    ], default="Fruit", string="Utilisation", required=True)
    aucun = fields.Boolean('Aucun')
    bordure = fields.Boolean('Bordure')
    culture = fields.Boolean('Culture')
    jachere = fields.Boolean('Jachère')
    zone_tampon = fields.Boolean('Zone tampon')
    zone_cultivable = fields.Many2one('zone.parcellaire', string="Zone cultivable")
    irrigue = fields.Boolean('Irrigué')
    piege_nitrates = fields.Boolean('Piège à nitrates')
    piece_jointe = fields.Binary('Ajouter une pièce jointe')

    # name = fields.Char('Nom')
    # number = fields.Char('Numéro de travail')
    # number_iden = fields.Char("Numéro d'identification")
    # surface = fields.Char('Surface')
    # date_cree = fields.Datetime('Date de Création', help="")
    # date_deces = fields.Datetime('Date de décès')
    # stat = fields.Boolean('State', help='')
    # image = fields.Binary(string="Image", attachment=True)