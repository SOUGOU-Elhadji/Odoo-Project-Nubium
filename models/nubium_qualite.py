# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class NubiumQualite(models.Model):

    _name = 'nubium.qualite'

    name = fields.Char('Nom')
    activity = fields.Char('Nom activité')
    test = fields.Char('Test')
    analyse = fields.Char(string='Analyses')
    incident = fields.Char(string='Incidents')
    agreage = fields.Char(string='Agreages')
    comptage = fields.Char(string='Comptages')
    image = fields.Binary(string="Image", attachment=True)