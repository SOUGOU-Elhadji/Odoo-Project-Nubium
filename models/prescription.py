# -*- coding: utf-8 -*-

from odoo import models, fields


class CreatePrescription(models.Model):
    _name = 'create.prescription'
    _description = 'Create prescription'

    numero = fields.Char('N° référence')
    date = fields.Datetime('Reçu le')
    prescripteur_id = fields.Many2one('create.prescripteur', string="Prescripteur", required=True)
    description = fields.Text('Description')
    piece_jointe = fields.Binary('Choisir un fichier')


