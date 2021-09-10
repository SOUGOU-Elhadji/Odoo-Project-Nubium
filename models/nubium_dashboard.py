# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class NubiumDashboard(models.Model):

    _name = 'nubium.dashboard'
    name = fields.Char('Nom')
    image = fields.Binary(string="Image", attachment=True)