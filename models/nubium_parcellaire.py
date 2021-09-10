# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class NubiumParcellaire(models.Model):

    _name = 'nubium.parcellaire'

    name = fields.Char('Nom', required=True)
    activity = fields.Char('Nom activity')
    date = fields.Char('Date')
    code = fields.Char('Code')
    zone = fields.Char(string='Zones Cultivables')
    parcelle = fields.Char(string='Parcelles')
    culture = fields.Char(string='Cultures')
    image = fields.Binary(string="Image", attachment=True)