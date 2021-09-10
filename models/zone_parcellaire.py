# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class ZoneParcellaire(models.Model):

    _name = 'zone.parcellaire'

    name = fields.Char('Nom', required=True)
    number = fields.Char('Numéro de travail', required=True)
    system_prod = fields.Selection([
        ('agriculture_bio', 'Agriculture biologique'),
        ('agriculture_conv', 'Agriculture conventionnelle'),
        ('agriculture_cons', 'Agriculture de conservation'),
        ('agriculture_dur', 'Agriculture durable'),
        ('agriculture_ext', 'Agriculture extensive'),
        ('agriculture_rais', 'Agriculture raisonnée'),
        ('biodynamie', 'Biodynamie'),
        ('permaculture', 'Permaculture'),
    ], string="Système de production")
    nature = fields.Selection([
        ('argil', 'Sol argilo-calcaire (Groies)'),
        ('limono', 'Sol argilo-limoneux'),
    ], string="Nature du sol")
    exploitant_id = fields.Many2one('create.prescripteur', string="Exploitant")
    proprietaire_id = fields.Many2one('create.prescripteur', string="Proprietaire")
    description = fields.Text('Description')
    forme = fields.Char('Forme')
    # image = fields.Binary(string="Image", attachment=True)