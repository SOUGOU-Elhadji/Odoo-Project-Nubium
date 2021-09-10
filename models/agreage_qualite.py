# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class AgreageQualite(models.Model):

    _name = 'agreage.qualite'
    _rec_name = 'preleve'

    preleve = fields.Datetime('Prélevé le', required=True)
    produit_id = fields.Many2one('create.produit', required=True)
    largeur = fields.Integer("Largeur de l'outil de semis ou de plantation (Mètre)", required=True)
    nombre = fields.Integer("Nombre de rangs lors de l'implantation", required=True)
    distance = fields.Integer('Distance de prélèvement (Mètre)', required=True)
    surface = fields.Float('Surface Totale')
    mesure = fields.Selection([
        ('acre', 'Acre'),
        ('are', 'are'),
        ('centiare', 'Centiare'),
        ('centimetre', 'Centimètre carré'),
        ('hectare', 'Hectare'),
        ('metre', 'Mètre carré'),
    ])
    semaine = fields.Integer('Semaine de récolte prévisionnelle')
    commentaire = fields.Text('Commentaire')
    piece_jointe = fields.Binary('Ajouter une pièce-jointe')

    image = fields.Binary(string="Image", attachment=True)