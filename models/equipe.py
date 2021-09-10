# -*- coding: utf-8 -*-

from odoo import models, fields


class CreateEquipe(models.Model):
    _name = 'create.equipe'
    _description = 'Create équipe'

    #NOUVELLE EQUIPE
    #INFORMATIONS GENERALE

    nom = fields.Char('Nom ', required=True)
    description = fields.Text('Description')