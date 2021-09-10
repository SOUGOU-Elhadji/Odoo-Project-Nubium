# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class ComptageQualite(models.Model):

    _name = 'comptage.qualite'

    name = fields.Char('Nom')
    test = fields.Char('Test')
    image = fields.Binary(string="Image", attachment=True)