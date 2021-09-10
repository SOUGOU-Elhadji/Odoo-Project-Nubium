# -*- coding: utf-8 -*-

from odoo import models, fields


class CreateResponsable(models.Model):
    _name = 'create.responsable'
    _description = 'Create responsable'

    #NOUVEL UTILISATEUR
    #INFORMATIONS GENERALE

    nom_famille = fields.Char('Nom de famille', required=True)
    prenom = fields.Char('Prénom', required=True)
    langue = fields.Selection([
        ('francais', 'francais'),
        ('anglais', 'anglais'),
    ], default="francais", string="Langue", required=True)
    email = fields.Char('Email', required=True)
    password = fields.Char('Nouveau mot de passe', required=True)
    password_confirm = fields.Char('Confirmation mot de passe', required=True)

    # FONCTION
    personne_id = fields.Many2one('create.personne', string="Personne")
    travaillant = fields.Boolean('Travaillant pour la socièté')
    emploi_role = fields.Char('Emploi / Role')
    equipe_id = fields.Many2one('create.equipe', string="Equipe")

    #ACCES
    admin_systeme = fields.Boolean('Administrateur Système')
    role_id = fields.Many2one('create.role', string="Role de base")
