# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class NubiumProduction(models.Model):

    _name = 'nubium.production'

    name = fields.Char(string="Nom", required=True)
    activity = fields.Char(string="Nom des activités")
    address = fields.Char(string="Adresse")
    date = fields.Date(string="Date de début")
    time = fields.Char(string="Temps de travail")
    statut = fields.Char(string="Statut")
    etat = fields.Char(string="Etat")
    cible = fields.Char(string="Nom des cibles")
    zone = fields.Char(string="Zone")
    # active = fields.Boolean('Active', default=True)
    activite = fields.Char(string='Activites')
    intervension = fields.Char(string='Intervensions')
    equipement = fields.Char(string='Equipements')
    image = fields.Binary(string="Image", attachment=True)

