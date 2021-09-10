# -*- coding: utf-8 -*-

from odoo import models, fields


class CreateEquipement(models.AbstractModel):
    _name = 'create.equipement'
    _description = 'Create Equipement'

    #INFORMATIONS GENERALES

    nom = fields.Char('Nom', required=True)
    numero_travail = fields.Char('Numéro de travail')
    type = fields.Selection([
        ('outil', 'Outil attelé')
    ], string="Type")
    date_mis_service = fields.Datetime('Mis en service le')
    date_mis_robut = fields.Datetime('Mis au rebut le')
    libelle_id = fields.Many2one('create.etiquette', required=True, string="Libellé")
    proprietaire_initial_id = fields.Many2one('create.prescripteur', string="Propriétaire initial")
    lieu_stockage_id = fields.Many2one('create.lieu', string="Lieu de stockage")
    geolocalisation = fields.Char('Géolocalisation')
    piece_jointe = fields.Binary('Ajouter une pièce jointe')

    #IDENTIFICATION
    photo = fields.Binary('Photo')
    description = fields.Text('Description')

    #INDICATEURS
    largeur = fields.Char('Largeur de travail')
    mesure = fields.Selection([
        ('metre', 'Mètre'),
        ('centimetre', 'Centimètre'),
        ('kilometre', 'Kilomètre'),
        ('millimetre', 'Millimètre'),
    ], default="metre", string="Mesure")


    def create_equipement(self):
        vals = {
            'nom': self.nom,
            'numero_travail': self.numero_travail,
            'type': self.type,
            'date_mis_service': self.date_mis_service,
            'date_mis_robut': self.date_mis_robut,
            'libelle_id': self.libelle_id.id,
            'proprietaire_initial_id': self.proprietaire_initial_id.id,
            'lieu_stockage_id': self.lieu_stockage_id.id,
            'geolocalisation': self.geolocalisation,
            'piece_jointe': self.piece_jointe,
            'photo': self.photo,
            'description': self.description,
            'largeur': self.largeur,
            'mesure': self.mesure,
        }
        # self.intervension_id.message_post(body="Test string ", subject="Creation intervension")
        # self.name_id.message_post(body="Test string ", subject="Creation name")
        # creating administratifs from the code
        new_equipement = self.env['equipement.production'].create(vals)
        context = dict(self.env.context)
        context['form_view_initial_mode'] = 'edit'
        return {'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'equipement.production',
                'res_id': new_equipement.id,
                'context': context
                }

