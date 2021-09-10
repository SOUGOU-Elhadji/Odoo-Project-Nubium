# -*- coding: utf-8 -*-

from odoo import models, fields


class CreateEtiquette(models.Model):
    _name = 'create.etiquette'
    _description = 'Create étiquette'

    name = fields.Char('Nom étiquette', required=True)


