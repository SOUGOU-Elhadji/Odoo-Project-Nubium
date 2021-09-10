# -*- coding: utf-8 -*-

from odoo import models, fields


class CreateAdminInter(models.Model):
    _name = 'create.admin.inter'
    _description = 'Create Administratif intervensions'

    #INFORMATIONS GENERALES
    date_debut = fields.Datetime('A partir de ')
    date_fin = fields.Datetime('Au')
    incident_id = fields.Many2one('incidence.qualite', string="Incident")
    vente = fields.Many2one('sale.order', string="Vente")
    description = fields.Text('Description')
    compteur_eau = fields.Integer("Compteur d'eau")
    prescription_id = fields.Many2one('create.prescription', string="Prescription")
    etiquette_id = fields.Many2one('create.etiquette', string="Etiquette")

    #PARAMETRES
    responsable_id = fields.Many2one('create.responsable', string="Responsable")
    consommable_id = fields.Many2one('create.consommable', string="Consommable")
    quantite = fields.Integer('Quantité', required=True, help='Cochez un type')

    #PRESTATION DE SERVICE
    fournisseur = fields.Many2one('res.partner', required=True, help='Cochez un type')
    commande = fields.Many2one('purchase.order', required=True, help='')
    reference = fields.Char('Référence fournisseur')

    intervension_id = fields.Many2one('intervension.production', string="Intervension")


    def create_admin_inter(self):
        vals = {
            'date_debut': self.date_debut,
            'date_fin': self.date_fin,
            'incident_id': self.incident_id.id,
            'description': self.description,
            'compteur_eau': self.compteur_eau,
            'prescription_id': self.prescription_id.id,
            'etiquette_id': self.etiquette_id.id,
            'responsable_id': self.responsable_id.id,
            'consommable_id': self.consommable_id.id,
            'quantite': self.quantite,
            'fournisseur': self.fournisseur,
            'commande': self.commande,
            'reference': self.reference,
        }
        # self.intervension_id.message_post(body="Test string ", subject="Creation intervension")
        # self.name_id.message_post(body="Test string ", subject="Creation name")
        # creating administratifs from the code
        new_admin_inter = self.env['intervension.production'].create(vals)
        context = dict(self.env.context)
        context['form_view_initial_mode'] = 'edit'
        return {'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'intervension.production',
                'res_id': new_admin_inter.id,
                'context': context
                }

