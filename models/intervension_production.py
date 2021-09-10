# -*- coding: utf-8 -*-

# import pytz
from odoo import api, fields, models, _
# from odoo.exceptions import  ValidationError


class IntervensionProduction(models.Model):
    _name = 'intervension.production'

    # INFORMATIONS GENERALES
    date_debut = fields.Datetime('A partir de ')
    date_fin = fields.Datetime('Au')
    incident_id = fields.Many2one('incidence.qualite', string="Incident")
    vente = fields.Many2one('sale.order', string="Vente")
    description = fields.Text('Description')
    compteur_eau = fields.Integer("Compteur d'eau")
    prescription_id = fields.Many2one('create.prescription', string="Prescription")
    etiquette_id = fields.Many2one('create.etiquette', string="Etiquette")
    # state = fields.Selection([
    #     ('draft', 'Draft'),
    #     ('confirm', 'Confirm'),
    #     ('done', 'Done'),
    #     ('cancel', 'Cancelled'),
    # ], string='Status', readonly=True, default='draft')

    # Prestation de service
    fournisseur = fields.Many2one('res.partner', required=True, help='Cochez un type')
    commande = fields.Many2one('purchase.order', required=True, help='')
    reference = fields.Char('Référence fournisseur')

    # PRODUCTION VITICOLE
    vignoble_id = fields.One2many('activite.vignoble', 'intervension_id', string="Vignoble")
    fertilisation_id = fields.One2many('activite.fertilisation', 'intervension_id', string="Fertilisation")
    protection_vignoble_id = fields.One2many('activite.protection', 'intervension_id', string="Protection vignoble")
    entretien_id = fields.One2many('activite.entretien', 'intervension_id', string="Entretien du sol")
    implantation_id = fields.One2many('activite.implantation', 'intervension_id', string="Implantation")
    palissage_id = fields.One2many('activite.palissage', 'intervension_id', string="Palissage")
    irrigation_id = fields.One2many('activite.irrigation', 'intervension_id', string="Irrigation")

    # PRODUCTION VEGETALE
    travail_sol_id = fields.One2many('activite.travail', 'intervension_id', string="Travail du sol")
    implantation_culture_id = fields.One2many('activite.implantation_culture', 'intervension_id', string="Implantation des cultures")
    fertilisation_vegetale_id = fields.One2many('activite.fertilisation_vegetale', 'intervension_id', string="Fertilisation")
    irrigation_vegetale_id = fields.One2many('activite.irrigation_vegetale', 'intervension_id', string="Irrigation")
    protection_culture_id = fields.One2many('activite.protection_culture', 'intervension_id', string="Protection des cultures")
    entretien_culture_id = fields.One2many('activite.entretien_culture', 'intervension_id', string="Entretien des cultures")
    recolte_id = fields.One2many('activite.recolte', 'intervension_id', string="Récolte")
    travaux_fonciers_id = fields.One2many('activite.travaux_fonciers', 'intervension_id', string="Travaux fonçiers sur installations")

    # PRODUCTION ANIMALE
    reproduction_id = fields.One2many('activite.reproduction', 'intervension_id', string="Production animale")
    identification_id = fields.One2many('activite.identification', 'intervension_id', string="Identification")
    alimentation_id = fields.One2many('activite.alimentation', 'intervension_id', string="Alimentation et abreuvage")
    produit_animal_id = fields.One2many('activite.produit_animal', 'intervension_id', string="Produits animaux")
    traitement_id = fields.One2many('activite.traitement', 'intervension_id', string="Traitement et soins")
    entretien_habitat_id = fields.One2many('activite.entretien_habitat', 'intervension_id', string="Entretien de l'habitat")
    travaux_ani_id = fields.One2many('activite.travaux_ani', 'intervension_id', string="Travaux fonçiers sur installations")

    # TRANSFORMATION
    transformation_id = fields.One2many('activite.transformation_prod', 'intervension_id', string="Transformation produits végétaux")
    conditionnement_id = fields.One2many('activite.conditionnement', 'intervension_id', string="Conditionnement")
    viniTrans_id = fields.One2many('activite.vini', 'intervension_id', string="Vinification")

    # MAINTENANCE
    alimentation_materiel_id = fields.One2many('activite.alimentation_materiel', 'intervension_id', string="Alimentation matériel")
    reparation_id = fields.One2many('activite.reparation', 'intervension_id', string="Réparation et maintenance")
    manutention_id = fields.One2many('activite.manutention', 'intervension_id', string="Manutention")
    travaux_maintenance_id = fields.One2many('activite.travaux_maintenance', 'intervension_id', string="Travaux fonçiers sur installation")

    # ADMINISTRATIF
    admin_id = fields.One2many('create.admin.inter', 'intervension_id', string="Admin")

    # def delete_lines(self):
    #     for rec in self:
    #         user_tz = pytz.timezone(self.env.context.get('tz') or self.env.user.tz)
    #         time_in_timezone = pytz.utc.localize(rec.appointment_datetime).astimezone(user_tz)
    #         # print("Time in UTC -->", rec.appointment_datetime)
    #         # print("Time in Users Timezone -->", time_in_timezone)
    #         rec.appointment_lines = [(5, 0, 0)]
    #
    # # Moving the State Of the Record To Confirm State in Button Click
    # # How to Add States/Statusbar for Records in Odoo
    # # https://www.youtube.com/watch?v=lPHWsw3Iclk&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=21
    # def action_confirm(self):
    #     for rec in self:
    #         rec.state = 'confirm'
    #         return {
    #             'effect': {
    #                 'fadeout': 'slow',
    #                 'message': 'Appointment Confirmed... Thanks You',
    #                 'type': 'rainbow_man',
    #             }
    #         }
    #
    # def action_done(self):
    #     for rec in self:
    #         rec.state = 'draft'

    # -------------- DEBUT PRODUCTION VITICOLE ----------------
    # VIGNOBLE CLASS
class Vignoble(models.Model):
    _name = 'activite.vignoble'

    # Parametres
    intervension_id = fields.Many2one('intervension.production', string="Intervension", readonly="1")
    culture_id = fields.Many2one('culture.parcellaire', string="Culture", required=True)
    conducteur_id = fields.Many2one('culture.parcellaire', string="Conducteur", required=True)
    tracteur_id = fields.Many2one('culture.parcellaire', string="Tracteur", required=True)
    outils_id = fields.Many2one('culture.parcellaire', string="Outil de taille", required=True)


    # FERTILISATION CLASS
class Fertilisation(models.Model):
    _name = 'activite.fertilisation'

    intervension_id = fields.Many2one('intervension.production', string="Intervension")
    epandage_engrais = fields.Boolean('Epandage engrais | Amendement')
    fertilisation_foliaire = fields.Boolean('Fertilisation foliaire')
    biostimulant = fields.Boolean('Biostimulant')
    fert_organique = fields.Boolean('Fertilisation organique')
    fert_minerale = fields.Boolean('Fertilisation minimale')
    apport = fields.Boolean('Apport en oligo-éléments')
    chaulage = fields.Boolean('Chaulage')
    # Paramètre
    culture = fields.Boolean('Culture')
    parcelle = fields.Boolean('Parcelle')
    parcelle_culture_id = fields.Many2one('create.parcelle_culture', string="Parcelle / Culture", required=True)
    angrais_id = fields.Many2one('create.angrais', string="Angrais", required=True)
    quantite = fields.Char('Quantité (Unité)', required=True)
    conducteur_id = fields.Many2one('culture.parcellaire', string="Conducteur", required=True)
    tracteur_id = fields.Many2one('culture.parcellaire', string="Tracteur", required=True)
    epandeur_id = fields.Many2one('culture.epandeur', string="Epandeur", required=True)
    outils_id = fields.Many2one('culture.parcellaire', string="Outil de taille", required=True)


    #PROTECTION VIGNOBLE CLASS
class ProtectionVignoble(models.Model):
    _name = 'activite.protection'

    intervension_id = fields.Many2one('intervension.production', string="Intervension")
    herbicide = fields.Boolean('Herbicide')
    fongicide = fields.Boolean('Fongicide')
    insecticide = fields.Boolean('Insecticide')
    molluscicide = fields.Boolean('Molluscicide')
    nematicide = fields.Boolean('Nématicide')
    acaricide = fields.Boolean('Acaricide')
    bactericide = fields.Boolean('Bactéricide')
    antigibier = fields.Boolean('Anti-gibier')
    virucide = fields.Boolean('Virucide')
    biostimulant = fields.Boolean('Biostimulant')
    regulateur = fields.Boolean('Régulateur de croissance')
    # Parametres
    culture_id = fields.Many2one('create.culture', string="Culture", required=True)
    produit_phytosanitaire = fields.Many2one('create.produit_phytosanitaire', string="Produit phytosanitaire", required=True)
    usage = fields.Many2one('create.usage', string="Usage")
    quantite = fields.Integer(string="Quantité (Unité)", required=True)
    conducteur_id = fields.Many2one('culture.parcellaire', string="Conducteur", required=True)
    tracteur_id = fields.Many2one('culture.parcellaire', string="Tracteur", required=True)
    pulverisateur = fields.Many2one('create.pulverisateur', string="Pulvérisateur", required=True)


    #ENTRETIEN SOL
class EntretienSol(models.Model):
    _name = 'activite.entretien'

    intervension_id = fields.Many2one('intervension.production', string="Intervension")
    # Parametres
    culture_id = fields.Many2one('create.culture', string="Culture", required=True)
    conducteur_id = fields.Many2one('create.conducteur', string="Conducteur", required=True)
    tracteur_id = fields.Many2one('create.tracteur', string="Tracteur", required=True)
    outils_id = fields.Many2one('create.outil', string="Outil de tracté", required=True)



    #IMPLANTATION VIGNE
class ImplantationVigne(models.Model):
    _name = 'activite.implantation'

    intervension_id = fields.Many2one('intervension.production', string="Intervension", readonly="1")
    # Parametres
    parcelle_id = fields.Many2one('create.parcelle', string="Parcelle", required=True)
    culture = fields.Many2one('create.produit', string="Culture", required=True)
    cepage = fields.Char('Cépage')
    num_lot = fields.Char('N° de lot')
    app_cert = fields.Char('Appelation / Certification')
    intervalle = fields.Integer('')
    select = fields.Selection([
        ('create.produit', 'Culture'),
        ('pret.conducteur', 'Conducteur'),
    ], string="Référence")


    #PALISSAGE
class Palissage(models.Model):
    _name = 'activite.palissage'

    intervension_id = fields.Many2one('intervension.production', string="Intervension")
    # Parametres
    culture = fields.Many2one('create.produit', string="Culture", required=True)
    piquet = fields.Many2one('create.piquet', string="Piquets", required=True)
    quantite = fields.Integer('Quantité (Unité)', required=True)
    operateur = fields.Many2one('create.personne', string="Opération", required=True)

    #IRRIGATION
class Irrigation(models.Model):
    _name = 'activite.irrigation'

    intervension_id = fields.Many2one('intervension.production', string="Intervension")
    # Parametres
    culture = fields.Many2one('create.produit', string="Culture", required=True)
    eau = fields.Many2one('create.eau', string="Eau (Unité)", required=True)
    quantite = fields.Integer('Quantité (Unité)', required=True)
    operateur = fields.Many2one('create.personne', string="Opération", required=True)
    tracteur = fields.Many2one('create.tracteur', string="Tracteur", required=True)
    equipement = fields.Many2one('equipement.production', string="Equipement", required=True)

    #-------------- FIN PRODUCTION VITICOLE ----------------


    #-------------- DEBUT PRODUCTION VEGETALE ----------------
    #TRAVAIL DU SOL
class TravailSol(models.Model):
    _name = 'activite.travail'

    intervension_id = fields.Many2one('intervension.production', string="Intervension", readonly="1")
    # Parametres
    parcelle = fields.Many2one('parcelle.parcellaire', string="Parcelle", required=True)
    conducteur_id = fields.Many2one('create.conducteur', string="Conducteur", required=True)
    tracteur_id = fields.Many2one('create.tracteur', string="Tracteur", required=True)
    tamiseuse_id = fields.Many2one('create.tamiseuse', string="Tamiseuse", required=True)
    remorque_id = fields.Many2one('create.remorque', string="Remorque", required=True)


    # IMPLANTATION DES CULTURES
class ImplantationCulture(models.Model):
    _name ='activite.implantation_culture'

    intervension_id = fields.Many2one('intervension.production', string="Intervension", readonly="1")
    # Parametres
    parcelle = fields.Many2one('parcelle.parcellaire', string="Parcelle", required=True)
    culture = fields.Many2one('create.produit', string="Culture", required=True)
    variete = fields.Char('Variété')
    num_lot = fields.Integer('N° de lot')
    semences = fields.Many2one('create.semence', string="Semences", required=True)
    quantite = fields.Integer('Quantité (Unité)', required=True)
    conducteur_id = fields.Many2one('create.conducteur', string="Conducteur", required=True)
    operateur = fields.Many2one('create.personne', string="Opération", required=True)
    tracteur = fields.Many2one('create.tracteur', string="Tracteur", required=True)
    semoir = fields.Many2one('create.semoir', string="Semoir", required=True)

    # Fertilisation
class FertilisationCulture(models.Model):
    _name = 'activite.fertilisation_vegetale'

    intervension_id = fields.Many2one('intervension.production', string="Intervension", readonly="1")

    biostimulant = fields.Boolean('Biostimulation')
    fert_org = fields.Boolean('Fertilisation organique')
    fert_mine = fields.Boolean('Fertilisation minérale')
    apport_oli = fields.Boolean('Apport en oligo-éléments')
    chaulage = fields.Boolean('Chaulage')
    # Parametres
    culture = fields.Boolean('Culture')
    parcelle = fields.Boolean('Parcelle')
    parcelle_culture = fields.Char('Parcelle / Culture', required=True)
    engrais = fields.Many2one('create.produit', required=True)
    quantite = fields.Integer('Quantité (Unité)', required=True)
    conducteur_id = fields.Many2one('create.conducteur', string="Conducteur", required=True)
    tracteur = fields.Many2one('create.tracteur', string="Tracteur", required=True)
    epandeur = fields.Many2one('create.epandeur', string="Epandeur", required=True)
    outil_tracte = fields.Many2one('create.outil', string="Outils tracté", required=True)

    # IRRIGATION
class IrrigationVegatal(models.Model):
    _name = 'activite.irrigation_vegetale'

    intervension_id = fields.Many2one('intervension.production', string="Intervension", readonly="1")
    # Parametres
    zone = fields.Many2one('zone.parcellaire', string="Zone", required=True)
    operateur = fields.Many2one('create.personne', string="Opération", required=True)
    epandeur = fields.Many2one('create.epandeur', string="Epandeur", required=True)
    equipement = fields.Many2one('equipement.production', string="Equipement", required=True)


    # PROTECTION CULTURE
class ProtectionCulture(models.Model):
    _name = 'activite.protection_culture'

    intervension_id = fields.Many2one('intervension.production', string="Intervension", readonly="1")
    # Parametres
    culture = fields.Boolean('Culture')
    parcelle = fields.Boolean('Parcelle')
    parcelle_culture = fields.Char('Parcelle / Culture', required=True)
    semences = fields.Many2one('create.semence', string="Semences", required=True)
    quantite = fields.Integer('Quantité (Unité)', required=True)
    conducteur_id = fields.Many2one('create.conducteur', string="Conducteur", required=True)
    operateur = fields.Many2one('create.personne', string="Opération", required=True)
    tracteur = fields.Many2one('create.tracteur', string="Tracteur", required=True)
    outil = fields.Many2one('create.outil', string="Outil", required=True)

    # ENTRETIEN CULTURE
class EntretienCulture(models.Model):
    _name = 'activite.entretien_culture'

    intervension_id = fields.Many2one('intervension.production', string="Intervension", readonly="1")

    desherbage = fields.Boolean('Désherbage')
    ameublissement = fields.Boolean('Ameublissement')
    # Parametres
    culture = fields.Many2one('culture.parcellaire', string="Culture", required=True)
    conducteur_id = fields.Many2one('create.conducteur', string="Conducteur", required=True)
    tracteur = fields.Many2one('create.tracteur', string="Tracteur", required=True)
    bineuse = fields.Many2one('create.bineuse', string="Bineuse", required=True)

    # RECOLTE
class Recolte(models.Model):
    _name = 'activite.recolte'

    intervension_id = fields.Many2one('intervension.production', string="Intervension", readonly="1")
    # Parametres
    culture = fields.Many2one('culture.parcellaire', string="Culture", required=True)
    oui = fields.Boolean('Oui')
    non = fields.Boolean('Non')
    matiere = fields.Many2one('create.matiere', string="Matière", required=True)
    quantite = fields.Integer('Quantité (Unité)', required=True)
    nouveau_nom = fields.Char('Nouveau nom')
    conducteur_id = fields.Many2one('create.conducteur', string="Conducteur", required=True)
    operateur = fields.Many2one('create.personne', string="Opération", required=True)
    tracteur = fields.Many2one('create.tracteur', string="Tracteur", required=True)
    outil_recolte = fields.Many2one('create.outil_recolte', string="Outil de récolte", required=True)
    outil = fields.Many2one('create.outil', string="Outil", required=True)

    # TRAVAUX FONCIER
class TravauxFoncier(models.Model):
    _name = 'activite.travaux_fonciers'

    intervension_id = fields.Many2one('intervension.production', string="Intervension", readonly="1")
    # Parametres
    zone = fields.Many2one('zone.parcellaire', string="Zone", required=True)
    consommable = fields.Many2one('create.consommable', string="Consommable", required=True)
    quantite = fields.Integer('Quantité (Unité)', required=True)
    conducteur_id = fields.Many2one('create.conducteur', string="Conducteur", required=True)
    operateur = fields.Many2one('create.personne', string="Opération", required=True)
    tracteur = fields.Many2one('create.tracteur', string="Tracteur", required=True)
    equipement = fields.Many2one('equipement.production', string="Equipement", required=True)

    # -------------- FIN PRODUCTION VEGETALE ----------------


    # -------------- DEBUT PRODUCTION ANIMALE ----------------
    # REPRODUCTION ANIMAL
class ReproductionAnimal(models.Model):
    _name = 'activite.reproduction'

    intervension_id = fields.Many2one('intervension.production', string="Intervension", readonly="1")

    # Parametres
    mere = fields.Many2one('create.mere', string="Mère", required=True)
    nouveau_ne = fields.Many2one('create.nouveau_ne', string="Nouveau né", required=True)
    nouveau_nom = fields.Char('Nouveau nom')
    num_ident = fields.Char("Numéro d'identification", required=True)
    sexe = fields.Selection([
        ('femelle', 'Femelle'),
        ('hermaphrodite', 'Hermaphrodite'),
        ('male', 'Male'),
        ('indefini', 'Indéfini'),
    ], string="Sexe")
    masse_net = fields.Integer('Masse nette')
    select_masse = fields.Selection([
        ('kilo', 'Kilogramme'),
        ('gramme', 'Gramme'),
        ('microgramme', 'Microgramme'),
        ('miligramme', 'Miligramme'),
        ('quintal', 'Quintal'),
        ('tonne', 'Tonne'),
    ], default="kilo")
    bonne_sante = fields.Boolean('Bonne santé')
    condition = fields.Selection([
        ('', 'Par césarienne'),
        ('', "Avec un peu d'aide"),
        ('', 'Avec recours à un tiers ou moyen mécanique'),
        ('', 'Embryotomie'),
        ('', 'Sans aide'),
    ], string="Condition de mise bas")
    soigneur = fields.Many2one('create.personne', string="Soigneur", required=True)

    #IDENTIFICATION
class Identification(models.Model):
    _name = 'activite.identification'

    intervension_id = fields.Many2one('intervension.production', string="Intervension", readonly="1")

    # Parametres
    animal = fields.Many2one('create.animal', string="Animal", required=True)
    num_ident = fields.Char("Numéro d'identification", required=True)
    operateur = fields.Many2one('create.personne', string="Opération", required=True)

    #ALIMENTATION
class Alimentation(models.Model):
    _name = 'activite.alimentation'

    intervension_id = fields.Many2one('intervension.production', string="Intervension", readonly="1")

    # Parametres
    culture = fields.Boolean('Culture')
    parcelle = fields.Boolean('Parcelle')
    parcelle_culture = fields.Char('Parcelle / Culture', required=True)
    troupeau_id = fields.Many2one('create.troupeau', string="Troupeau", required=True)
    operateur = fields.Many2one('create.personne', string="Opération", required=True)

    # PRODUITS ANIMAUX
class ProduitAnimaux(models.Model):
    _name = 'activite.produit_animal'

    intervension_id = fields.Many2one('intervension.production', string="Intervension", readonly="1")

    # Parametres
    volailles = fields.Many2one('create.volaille', string="Volailles", required=True)
    oeuf = fields.Many2one('create.produit', string="Oeufs", required=True)
    quantite = fields.Integer('Quantité (Unité)', required=True)
    nouveau_nom = fields.Char('Nouveau nom')
    operateur = fields.Many2one('create.personne', string="Opération", required=True)

    #TRAITEMENT ET SOINS
class TraitementSoins(models.Model):
    _name = 'activite.traitement'

    intervension_id = fields.Many2one('intervension.production', string="Intervension", readonly="1")

    # Parametres
    animal_id = fields.Many2one('create.animal', string="Animal", required=True)
    new_emplacement = fields.Many2one('create.emplacement', string="Nouveau emplcement")
    new_group = fields.Many2one('create.group', string="Nouveau groupe")
    new_variant = fields.Many2one('create.variant', string="Nouveau variant")
    conducteur_id = fields.Many2one('create.conducteur', string="Conducteur", required=True)
    operateur = fields.Many2one('create.personne', string="Opération", required=True)
    vehicule_id = fields.Many2one('create.vehicule', string="Véhicule", required=True)
    remorque_id = fields.Many2one('create.remorque', string="Remorque", required=True)

    #ENTRETIEN DE L'HABITAT
class EntretienHabitat(models.Model):
    _name = 'activite.entretien_habitat'

    intervension_id = fields.Many2one('intervension.production', string="Intervension", readonly="1")
    zone_heberg = fields.Many2one('zone.parcellaire', string="Zone d'hébergement de l'animal", required=True)
    desinfectant = fields.Many2one('create.desinfectant', string="Désinfectant", required=True)
    quantite_desinfectant = fields.Integer('Quantité (Unité)')
    produit_nett = fields.Many2one('create.produit_nettoyant', string="Produit de nettoyage", required=True)
    quantite_produit = fields.Integer('Quantité (Unité)')
    conducteur_id = fields.Many2one('create.conducteur', string="Conducteur", required=True)
    operateur = fields.Many2one('create.personne', string="Opération", required=True)
    outil_nettoi = fields.Many2one('create.outil_nettoyant', string="Outil de nettoyage", required=True)
    tracteur = fields.Many2one('create.tracteur', string="Tracteur", required=True)

    #TRAVAUX FONCIERS SUR INSTALLATION
class TravauxFoncierInstall(models.Model):
    _name = 'activite.travaux_ani'

    intervension_id = fields.Many2one('intervension.production', string="Intervension", readonly="1")
    nettoyage = fields.Boolean('Nettoyage')
    reparation = fields.Boolean('Réparation')
    construction = fields.Boolean('Contruction')
    renovation = fields.Boolean('Rénovation')
    #Parametre
    zone = fields.Many2one('zone.parcellaire', string="Zone", required=True)
    consommable = fields.Many2one('create.consommable', string="Consommable", required=True)
    quantite = fields.Integer('Quantité (Unité)', required=True)
    conducteur_id = fields.Many2one('create.conducteur', string="Conducteur", required=True)
    operateur = fields.Many2one('create.personne', string="Opération", required=True)
    tracteur = fields.Many2one('create.tracteur', string="Tracteur", required=True)
    equipement = fields.Many2one('equipement.production', string="Equipement", required=True)

    #-------------- FIN PRODUCTION ANIMALE ----------------

    #-------------- DEBUT TRANSFORMATION ----------------
    #TRANSFORMATION PRODUITS VEGETAUX
class TransformationProd(models.Model):
    _name = 'activite.transformation_prod'

    intervension_id = fields.Many2one('intervension.production', string="Intervension", readonly="1")
#     #Parametre
    culture = fields.Boolean('Culture')
    parcelle = fields.Boolean('Parcelle')
    parcelle_culture = fields.Many2one('culture.parcellaire', string="Parcelle / Culture", required=True)
    produit_a_trier = fields.Many2one('create.produit', string="Produits à trier", required=True)
    quantite = fields.Integer('Quantité', required=True)
    unite_tri = fields.Selection([
        ('unite', 'Unité'),
        ('kg', 'kg (Masse nette en kilogrammes)'),
        ('t', 'T (Masse nette en tonnes)'),
    ], default="unite", string="Unité")

    produit_tries = fields.Many2one('create.produit', string="Produit triés", required=True)
    quantite_prod = fields.Integer('Quantité', required=True)
    unite_prod_tries = fields.Selection([
        ('unite', 'Unité'),
        ('kg', 'kg (Masse nette en kilogrammes)'),
        ('t', 'T (Masse nette en tonnes)'),
    ], default="unite", string="Unité")
    new_name = fields.Char('Nouveau nom')

    ecart_tri = fields.Many2one('create.produit', string="Ecart de tri", required=True)
    quantite_ecart = fields.Integer('Quantité', required=True)
    unite_ecart = fields.Selection([
        ('unite', 'Unité'),
        ('kg', 'kg (Masse nette en kilogrammes)'),
        ('t', 'T (Masse nette en tonnes)'),
    ], default="unite", string="Unité")
    new_name_ecart = fields.Char('Nouveau nom')

    produit_phyto = fields.Many2one('create.produit', string="Produit phytosanitaire", required=True)
    usage = fields.Many2one('create.usage', string="Usage")
    quantite_phyto = fields.Integer('Quantité', required=True)
    unite = fields.Selection([
        ('unite', 'Unité'),
        ('kg', 'kg (Masse nette en kilogrammes)'),
        ('t', 'T (Masse nette en tonnes)'),
    ], default="unite", string="Unité")

    equipement = fields.Many2one('equipement.production', string="Equipement", required=True)
    operateur = fields.Many2one('create.personne', string="Opération", required=True)

    # CONDITIONNEMENT
class Conditionnement(models.Model):
    _name = 'activite.conditionnement'

    intervension_id = fields.Many2one('intervension.production', string="Intervension", readonly="1")
    # Parametre
    produit_a_preparer = fields.Many2one('create.produit', string="Produit à préparer", required=True)
    quantite = fields.Integer('Quantité', required=True)
    unite = fields.Selection([
        ('unite', 'Unité'),
        ('kg', 'kg (Masse nette en kilogrammes)'),
        ('t', 'T (Masse nette en tonnes)'),
        ('l', 'L (Volume)'),
    ], default="unite", string="Unité")

    materiel = fields.Many2one('create.produit', string="Matériel d'emballage", required=True)
    quantite_mat = fields.Integer('Quantité', required=True)
    unite_mat = fields.Selection([
        ('unite', 'Unité'),
        ('kg', 'kg (Masse nette en kilogrammes)'),
        ('t', 'T (Masse nette en tonnes)'),
        ('l', 'L (Volume)'),
    ], default="unite", string="Unité")

    produit_preparer = fields.Many2one('create.produit', string="Produit préparé", required=True)
    quantite_prod = fields.Integer('Quantité', required=True)
    unite_prod = fields.Selection([
        ('unite', 'Unité'),
        ('kg', 'kg (Masse nette en kilogrammes)'),
        ('t', 'T (Masse nette en tonnes)'),
        ('l', 'L (Volume)'),
    ], default="unite", string="Unité")
    new_name = fields.Char('Nouveau nom')
    operateur = fields.Many2one('create.personne', string="Opération", required=True)
    equipement = fields.Many2one('equipement.production', string="Equipement", required=True)

#     #VINIFICATION
class ViniTrans(models.Model):
    _name = 'activite.vini'

    intervension_id = fields.Many2one('intervension.production', string="Intervension", readonly="1")
    # Parametre
    cuve = fields.Many2one('create.cuve', string="Cuve", required=True)
    jus_fermente = fields.Many2one('create.produit', string="Jus à fermenter")
    produit_oenologique = fields.Many2one('create.produit', string="Produit oenologique", required=True)
    quantite = fields.Integer('Quantité', required=True)
    unite = fields.Selection([
        ('unite', 'Unité'),
        ('kg', 'kg (Masse nette en kilogrammes)'),
        ('t', 'T (Masse nette en tonnes)'),
        ('l', 'L (Volume)'),
    ], default="unite", string="Unité")
    operateur_chai = fields.Many2one('create.personne', string="Opérateur de chai")
    jus_ferm = fields.Many2one('create.produit', string="Jus fermenté", required=True)

    # -------------- FIN TRANSFORMATION ----------------

    # -------------- DEBUT MAINTENANCE ----------------
    # ALIMENTATION MATERIEL
class AlimentationMateriel(models.Model):
    _name = 'activite.alimentation_materiel'

    intervension_id = fields.Many2one('intervension.production', string="Intervension", readonly="1")
    # Parametre
    equipement = fields.Many2one('equipement.production', string="Equipement", required=True)
    carburant = fields.Char('Carburant', required=True)
    quantite = fields.Integer('Quantité', required=True)
    unite = fields.Selection([
        ('unite', 'Unité'),
        ('kg', 'kg (Masse nette en kilogrammes)'),
        ('t', 'T (Masse nette en tonnes)'),
        ('l', 'L (Volume)'),
    ], default="unite", string="Unité")
    mecanicien = fields.Many2one('create.personne', string="Mécanicien", required=True)

    # REPARATION ET MAINTENANCE
class ReparationMaintenance(models.Model):
    _name = 'activite.reparation'

    intervension_id = fields.Many2one('intervension.production', string="Intervension", readonly="1")
    preventice = fields.Boolean('Maintenance préventive')
    curative = fields.Boolean('Maintenance curative')
    amelioration = fields.Boolean('Maintenance améliorative')
    # Parametre
    equipement = fields.Many2one('equipement.production', string="Equipement", required=True)
    composant = fields.Char('Composant')
    piece_rempl = fields.Many2one('', string="Pièce de remplacement", required=True)
    quantite = fields.Integer('Quantité', required=True)
    unite = fields.Selection([
        ('unite', 'Unité'),
        ('kg', 'kg (Masse nette en kilogrammes)'),
        ('t', 'T (Masse nette en tonnes)'),
        ('l', 'L (Volume)'),
    ], default="unite", string="Unité")
    composant_piece = fields.Char('Composant')
    consommable = fields.Char('Consommable', required=True)
    quantite_cons = fields.Integer('Quantité', required=True)
    unite_cons = fields.Selection([
        ('unite', 'Unité'),
        ('kg', 'kg (Masse nette en kilogrammes)'),
        ('t', 'T (Masse nette en tonnes)'),
        ('l', 'L (Volume)'),
    ], default="unite", string="Unité")
    mecanicien = fields.Many2one('create.personne', string="Mécanicien", required=True)
    outil = fields.Char('Outil',required=True)

    # MANUTENTION
class Manutention(models.Model):
    _name = 'activite.manutention'

    intervension_id = fields.Many2one('intervension.production', string="Intervension", readonly="1")
    operateur = fields.Many2one('create.personne', string="Opération", required=True)
    parcelle = fields.Many2one('parcelle.parcellaire', string="Parcelle", required=True)
    equipement = fields.Many2one('equipement.production', string="Equipement", required=True)

    # TRAVAUX FONCIER SUR INSTALLATION
class TravauxFoncierInst(models.Model):
    _name = 'activite.travaux_maintenance'

    intervension_id = fields.Many2one('intervension.production', string="Intervension", readonly="1")
    nettoyage = fields.Boolean('Nettoyage')
    reparation = fields.Boolean('Réparation')
    construction = fields.Boolean('Construction')
    renovation = fields.Boolean('Rénovation')
    zone = fields.Many2one('zone.parcellaire', string="Zone", required=True)
    consommable = fields.Char('Consommable', required=True)
    quantite = fields.Integer('Quantité', required=True)
    unite = fields.Selection([
        ('unite', 'Unité'),
        ('kg', 'kg (Masse nette en kilogrammes)'),
        ('t', 'T (Masse nette en tonnes)'),
        ('l', 'L (Volume)'),
    ], default="unite", string="Unité")
    conducteur = fields.Many2one('create.personne', string="Conducteur", required=True)
    operateur = fields.Many2one('create.personne', string="Opérateur", required=True)
    tracteur = fields.Many2one('equipement.production', string="Tracteur", required=True)
    equipement = fields.Many2one('equipement.production', string="Equipement", required=True)

    # -------------- FIN MAINTENANCE ----------------





# class AlimentationMat(models.Model):
#     _name = 'alimentation.materiel'
#     _rec_name = ''
#
#     # INFORMATIONS GENERALES
#     date_debut = fields.Datetime('A partir de ')
#     date_fin = fields.Datetime('Au')
#     incident_id = fields.Many2one('incidence.qualite', string="Incident")
#     description = fields.Text('Description')
#     compteur_eau = fields.Integer("Compteur d'eau")
#     prescription_id = fields.Many2one('create.prescription', string="Prescription")
#     etiquette_id = fields.Many2one('create.etiquette', string="Etiquette")
#
#     #PARAMETRES
#     equipement_id = fields.Many2one('create.equipement', string="Equipement")
#     carburant = fields.Selection([
#         ('gasoil', 'GASOIL_2004 Gasoil (P00000000345 - Zone Outils (4475.0 litre)'),
#     ], string="Carburant", required=True)
#     quantite = fields.Integer('Quantité (Unité)')
#     mecanicien_id = fields.Many2one('create.mecanicien', string="Mécanicien", required=True)
#
#     #PRESTATION DE SERVICE
#     fournisseur_id = fields.Many2one('create.fournisseur', string="Fournisseur", required=True)
#     # commande_id = fields.Many2one('create.commande',)
#







    # @api.constrains('probleme')
    # def chexk_blem(self):
    #     for rec in self:
    #         if rec.probleme == 5:
    #             raise ValidationError(_('Erreur de saisie'))
    #
    # def create_admin_inter_intervensions(self):
    #     return {
    #         'name': _('Administratifs intervensions'),
    #         'domain': [('administratif_id', '=', self.id)],
    #         'view_type': 'form',
    #         'res_model': 'create.admin.inter',
    #         'view_id': False,
    #         'view_mode': 'form,kanban',
    #         'type': 'ir.actions.act_window',
    #     }