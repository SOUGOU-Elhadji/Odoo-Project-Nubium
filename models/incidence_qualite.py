# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class IncidenceQualite(models.Model):

    _name = 'incidence.qualite'
    _rec_name = 'type'

    type = fields.Selection([
        ('acarien', 'Acarien ajune'),
        ('accident', 'Accident matériel'),
        ('alternaria', 'Alternaria'),
    ], string="Type", required=True)
    date = fields.Datetime('Observé à', required=True)
    photo = fields.Binary('Photo')
    description = fields.Text('Description')
    priorite = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    ], string="Priorité")
    gravite = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    ], string="Gravité")
    geolocalisation = fields.Char('Géolocalisation')
    piece_jointe = fields.Binary('Ajouter une pièce jointe')
    image = fields.Binary(string="Image", attachment=True)
