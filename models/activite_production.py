# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class ActiviteProduction(models.Model):

    _name = 'activite.production'
    _rec_name = 'name'

    #PARTIE GESTION ADMINISTRATION

    name = fields.Char(required=True)
    independante = fields.Boolean('Indépendante', required=True, help='Cochez un type')
    auxiliaire = fields.Boolean('Auxiliaire', required=True, help='Cochez un type')
    principal = fields.Boolean('Principal', required=True, help='')
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
    famille = fields.Selection([
        ('administratif', 'Administratif'),
        ('maintenance', 'Maintenance'),
        ('prestation_service', 'Prestation de service'),
        ('production_animale', 'Production animale'),
        ('production_viticole', 'Production viticole'),
        ('production_vegetale', 'Production végétale'),
        ('transformation', 'Transformation'),
        ('vinification', 'Vinification'),
    ], default='administratif', string="Famille", required=True)
    annuelle = fields.Boolean('Annuelle', required=True, help='')
    perenne = fields.Boolean('Pérenne', required=True, help='')
    autrui = fields.Boolean('autrui', required=True, help='')
    description = fields.Text('Description')
    date_debut = fields.Datetime('Début Campagne')
    date_fin = fields.Datetime('Fin Campagne')
    distribution_activite = fields.Integer("Distribution entre activité")
    image = fields.Binary(string="Image", attachment=True)

    administratif_id = fields.One2many('activite.administratif', 'admin_id', string="Ligne administratif")
    transformation_id = fields.One2many('activite.transformation', 'admin_id', string="Ligne transformation")
    vinification_id = fields.One2many('activite.vinification', 'admin_id', string="Vinification")
    viticol_id = fields.One2many('activite.viticol', 'admin_id', string="Production viticole")
    animal_id = fields.One2many('activite.animal', 'admin_id', string="Production animale")
    vegetale_id = fields.One2many('activite.vegetale', 'admin_id', string="Production végétale")
    prestation_id = fields.One2many('activite.prestation', 'admin_id', string="Prestation de service")


    #PRESTATION DE SERVICE
class PrestationService(models.Model):
    _name = 'activite.prestation'
    _rec_name = 'nom'

    # AGREAGES
    admin_id = fields.Many2one('activite.production', string="Admin ID")
    agreage = fields.Boolean('Utiliser les agréages', help='Cochez un type')
    piece = fields.Boolean("Mesurer le nombre de pièces de l'échantillon", help='Cochez un type')
    masse_nette = fields.Boolean("Mesurer la masse nette de l'échantillon", help='Cochez un type')
    unite = fields.Selection([
        ('microgramme', 'Microgramme'),
        ('milligramme', 'Milligramme'),
        ('gramme', 'Gramme'),
        ('kilogramme', 'Kilogramme'),
        ('quintal', 'Quintal'),
        ('tonne', 'Tonne'),
    ], string="Unité utilisée pour la masse nette")
    echantillon = fields.Boolean("Mesurer les extremas de l'échantillon", help='Cochez un type')
    indicateur = fields.Selection([
        ('calibre', 'Calibre'),
        ('cumul', 'Cumul des participations'),
        ('diametre', 'Diamètre'),
        ('hauteur', 'Hauteur'),
        ('intervalle', 'Intervalle inter-rangs'),
        ('intervalle', 'Intervalle inter-pieds'),
        ('largeur', 'Largeur'),
        ('largeur', 'Largeur de travail'),
        ('longueur', 'Longueur'),
        ('longueur', 'Longueur nette'),
        ('profondeur', 'Profondeur du sol'),
        ('zone', 'Zone non traitée(ZNT)'),
    ], string="Indicateur utilisé pour la mesure des extremas")
    unite_extrema = fields.Selection([
        ('centimetre', 'Centimètre'),
        ('kilometre', 'Kilomètre'),
        ('metre', 'Mètre'),
        ('millimetre', 'Millimètre'),
    ], string="Unité utilisée pour la mesure des extremas")
    indicateur_taille = fields.Selection([
        ('calibre', 'Calibre'),
        ('capacite', 'Capacité de stockage massique maximale'),
        ('capacite', 'Capacité de stockage massique minimale'),
        ('cumul', 'Cumul des participations'),
        ('diametre', 'Diamètre'),
        ('hauteur', 'Hauteur'),
        ('intervalle', 'Intervalle inter-rangs'),
        ('intervalle', 'Intervalle inter-pieds'),
        ('largeur', 'Largeur'),
        ('largeur', 'Largeur de travail'),
        ('longueur', 'Longueur'),
        ('longueur', 'Longueur nette'),
        ('masse', 'Masse nette'),
        ('poids', 'Poids de mille grains'),
        ('poids', 'Poids frais'),
    ], string="Indicateur de taille", required=True)
    unite_taille = fields.Selection([
        ('centimetre', 'Centimètre'),
        ('gramme', 'Gramme'),
        ('kilogramme', 'Kilogramme'),
        ('kilometre', 'Kilomètre'),
        ('metre', 'mètre'),
        ('millimetre', 'Millimètre'),
        ('microgramme', 'Microgramme'),
        ('milligramme', 'Milligramme'),
        ('quintal', 'Quintal'),
        ('tonne', 'Tonne'),
    ], string="Unité de taille", required=True)
    valeur_min = fields.Integer(string="Valeur minimale", required=True)
    valeur_max = fields.Integer(string="Valeur maximale", required=True)
    commercialisable = fields.Boolean('Commercialisable', help='Cochez un type')
    nom = fields.Char('Nom qualité', required=True)
    maladie = fields.Boolean('Maladie', required=True, help='')
    malformation = fields.Boolean('Malformation', required=True, help='')
    aucune = fields.Boolean('Aucune', required=True, help='')

    # COMPTAGES
    comptage = fields.Boolean('Utiliser les comptages', help='Cochez un type')
    nom_comptage = fields.Char('Nom comptage', required=True)
    unite_densite = fields.Selection([
        ('millier', 'Millier par hectare'),
        ('million', 'Million par hectare'),
        ('thousand', 'Thousand per square meter '),
        ('unite', 'Unité par hectare'),
        ('unite', 'Unité par mètre carré'),
    ], default="millier", string="Unité de densité de semis", required=True)
    unite_longueur = fields.Selection([
        ('centimetre', 'Centimètre'),
        ('kilometre', 'Kilomètre'),
        ('metre', 'Mètre'),
        ('millimetre', 'Millimètre'),
    ], string="Unité de longueur d'échantillonnage", required=True)
    pourcentage = fields.Integer('Pourcentage de germination attendu', required=True)
    densite_theorique = fields.Integer('Densité théorique de semis', required=True)
    nombre_theorique = fields.Integer('Nombre théorique de graines', required=True)

    # SAISONNALITE
    saisonnalite = fields.Boolean('Utiliser les saisonnalites', help='Cochez un type')
    nom_saisonnalite = fields.Char('Nom Saison', required=True)

    # ITINERAIRE CULTURAUX
    itineraire = fields.Boolean('Utiliser les itineraires techniques', help='Cochez un type')
    nom_itineraire = fields.Char('Nom', required=True)
    date_semis = fields.Boolean('Date de semis prévisionnelle', help='')
    date_recolte = fields.Boolean('Date de récolte prévisionnelle', help='')
    intrui = fields.Boolean('intrui', help='')
    date_itineraire = fields.Datetime('Date')
    jour = fields.Integer('Nombre de Jour')


#PRODUCTION VEGETALE
class ProdVegetal(models.Model):
    _name = 'activite.vegetale'
    _rec_name = 'piece'

    # AGREAGES
    admin_id = fields.Many2one('activite.production', string="Admin ID")
    agreage = fields.Boolean('Utiliser les agréages', help='Cochez un type')
    piece = fields.Boolean("Mesurer le nombre de pièces de l'échantillon", help='Cochez un type')
    masse_nette = fields.Boolean("Mesurer la masse nette de l'échantillon", help='Cochez un type')
    unite = fields.Selection([
        ('microgramme', 'Microgramme'),
        ('milligramme', 'Milligramme'),
        ('gramme', 'Gramme'),
        ('kilogramme', 'Kilogramme'),
        ('quintal', 'Quintal'),
        ('tonne', 'Tonne'),
    ], string="Unité utilisée pour la masse nette")
    echantillon = fields.Boolean("Mesurer les extremas de l'échantillon", help='Cochez un type')
    indicateur = fields.Selection([
        ('calibre', 'Calibre'),
        ('cumul', 'Cumul des participations'),
        ('diametre', 'Diamètre'),
        ('hauteur', 'Hauteur'),
        ('intervalle', 'Intervalle inter-rangs'),
        ('intervalle', 'Intervalle inter-pieds'),
        ('largeur', 'Largeur'),
        ('largeur', 'Largeur de travail'),
        ('longueur', 'Longueur'),
        ('longueur', 'Longueur nette'),
        ('profondeur', 'Profondeur du sol'),
        ('zone', 'Zone non traitée(ZNT)'),
    ], string="Indicateur utilisé pour la mesure des extremas")
    unite_extrema = fields.Selection([
        ('centimetre', 'Centimètre'),
        ('kilometre', 'Kilomètre'),
        ('metre', 'Mètre'),
        ('millimetre', 'Millimètre'),
    ], string="Unité utilisée pour la mesure des extremas")
    indicateur_taille = fields.Selection([
        ('calibre', 'Calibre'),
        ('capacite', 'Capacité de stockage massique maximale'),
        ('capacite', 'Capacité de stockage massique minimale'),
        ('cumul', 'Cumul des participations'),
        ('diametre', 'Diamètre'),
        ('hauteur', 'Hauteur'),
        ('intervalle', 'Intervalle inter-rangs'),
        ('intervalle', 'Intervalle inter-pieds'),
        ('largeur', 'Largeur'),
        ('largeur', 'Largeur de travail'),
        ('longueur', 'Longueur'),
        ('longueur', 'Longueur nette'),
        ('masse', 'Masse nette'),
        ('poids', 'Poids de mille grains'),
        ('poids', 'Poids frais'),
    ], string="Indicateur de taille", required=True)
    unite_taille = fields.Selection([
        ('centimetre', 'Centimètre'),
        ('gramme', 'Gramme'),
        ('kilogramme', 'Kilogramme'),
        ('kilometre', 'Kilomètre'),
        ('metre', 'mètre'),
        ('millimetre', 'Millimètre'),
        ('microgramme', 'Microgramme'),
        ('milligramme', 'Milligramme'),
        ('quintal', 'Quintal'),
        ('tonne', 'Tonne'),
    ], string="Unité de taille", required=True)
    valeur_min = fields.Integer(string="Valeur minimale", required=True)
    valeur_max = fields.Integer(string="Valeur maximale", required=True)
    commercialisable = fields.Boolean('Commercialisable', help='Cochez un type')
    nom = fields.Char('Nom qualité', required=True)
    maladie = fields.Boolean('Maladie', required=True, help='')
    malformation = fields.Boolean('Malformation', required=True, help='')
    aucune = fields.Boolean('Aucune', required=True, help='')

    # COMPTAGES
    comptage = fields.Boolean('Utiliser les comptages', help='Cochez un type')
    nom_comptage = fields.Char('Nom comptage', required=True)
    unite_densite = fields.Selection([
        ('millier', 'Millier par hectare'),
        ('million', 'Million par hectare'),
        ('thousand', 'Thousand per square meter '),
        ('unite', 'Unité par hectare'),
        ('unite', 'Unité par mètre carré'),
    ], default="millier", string="Unité de densité de semis", required=True)
    unite_longueur = fields.Selection([
        ('centimetre', 'Centimètre'),
        ('kilometre', 'Kilomètre'),
        ('metre', 'Mètre'),
        ('millimetre', 'Millimètre'),
    ], string="Unité de longueur d'échantillonnage", required=True)
    pourcentage = fields.Integer('Pourcentage de germination attendu', required=True)
    densite_theorique = fields.Integer('Densité théorique de semis', required=True)
    nombre_theorique = fields.Integer('Nombre théorique de graines', required=True)

    # SAISONNALITE
    saisonnalite = fields.Boolean('Utiliser les saisonnalites', help='Cochez un type')
    nom_saisonnalite = fields.Char('Nom Saison', required=True)

    # ITINERAIRE CULTURAUX
    itineraire = fields.Boolean('Utiliser les itineraires techniques', help='Cochez un type')
    nom_itineraire = fields.Char('Nom', required=True)
    date_semis = fields.Boolean('Date de semis prévisionnelle', help='')
    date_recolte = fields.Boolean('Date de récolte prévisionnelle', help='')
    intrui = fields.Boolean('intrui', help='')
    date_itineraire = fields.Datetime('Date')
    jour = fields.Integer('Nombre de Jour')

    prod_reference = fields.Selection([
        ('ananas', 'Agriculture biologique'),
        ('abricotier', 'Agriculture conventionnelle'),
        ('ail', 'Agriculture de conservation'),
        ('agnelique', 'Agriculture durable'),
    ], string="Production de référence")
    annee_production = fields.Selection([
        ('n+1', 'N+1'),
        ('n+2', 'N+2'),
        ('n+3', 'N+3'),
        ('n+4', 'N+4'),
        ('n+5', 'N+5'),
    ], string="1ére année de production (année N)")


 # PRODUCTION VITICOLE
class ProdViticole(models.Model):
    _name = 'activite.viticol'
    _rec_name = 'espece'

    admin_id = fields.Many2one('activite.production', string="Admin ID")
    agreage = fields.Boolean('Utiliser les agréages', help='Cochez un type')
    piece = fields.Boolean("Mesurer le nombre de pièces de l'échantillon", help='Cochez un type')
    masse_nette = fields.Boolean("Mesurer la masse nette de l'échantillon", help='Cochez un type')
    unite = fields.Selection([
        ('microgramme', 'Microgramme'),
        ('milligramme', 'Milligramme'),
        ('gramme', 'Gramme'),
        ('kilogramme', 'Kilogramme'),
        ('quintal', 'Quintal'),
        ('tonne', 'Tonne'),
    ], string="Unité utilisée pour la masse nette")
    echantillon = fields.Boolean("Mesurer les extremas de l'échantillon", help='Cochez un type')
    indicateur = fields.Selection([
        ('calibre', 'Calibre'),
        ('cumul', 'Cumul des participations'),
        ('diametre', 'Diamètre'),
        ('hauteur', 'Hauteur'),
        ('intervalle', 'Intervalle inter-rangs'),
        ('intervalle', 'Intervalle inter-pieds'),
        ('largeur', 'Largeur'),
        ('largeur', 'Largeur de travail'),
        ('longueur', 'Longueur'),
        ('longueur', 'Longueur nette'),
        ('profondeur', 'Profondeur du sol'),
        ('zone', 'Zone non traitée(ZNT)'),
    ], string="Indicateur utilisé pour la mesure des extremas")
    unite_extrema = fields.Selection([
        ('centimetre', 'Centimètre'),
        ('kilometre', 'Kilomètre'),
        ('metre', 'Mètre'),
        ('millimetre', 'Millimètre'),
    ], string="Unité utilisée pour la mesure des extremas")
    indicateur_taille = fields.Selection([
        ('calibre', 'Calibre'),
        ('capacite', 'Capacité de stockage massique maximale'),
        ('capacite', 'Capacité de stockage massique minimale'),
        ('cumul', 'Cumul des participations'),
        ('diametre', 'Diamètre'),
        ('hauteur', 'Hauteur'),
        ('intervalle', 'Intervalle inter-rangs'),
        ('intervalle', 'Intervalle inter-pieds'),
        ('largeur', 'Largeur'),
        ('largeur', 'Largeur de travail'),
        ('longueur', 'Longueur'),
        ('longueur', 'Longueur nette'),
        ('masse', 'Masse nette'),
        ('poids', 'Poids de mille grains'),
        ('poids', 'Poids frais'),
    ], string="Indicateur de taille", required=True)
    unite_taille = fields.Selection([
        ('centimetre', 'Centimètre'),
        ('gramme', 'Gramme'),
        ('kilogramme', 'Kilogramme'),
        ('kilometre', 'Kilomètre'),
        ('metre', 'mètre'),
        ('millimetre', 'Millimètre'),
        ('microgramme', 'Microgramme'),
        ('milligramme', 'Milligramme'),
        ('quintal', 'Quintal'),
        ('tonne', 'Tonne'),
    ], string="Unité de taille", required=True)
    valeur_min = fields.Integer(string="Valeur minimale", required=True)
    valeur_max = fields.Integer(string="Valeur maximale", required=True)
    commercialisable = fields.Boolean('Commercialisable', help='Cochez un type')
    nom = fields.Char('Nom qualité', required=True)
    maladie = fields.Boolean('Maladie', required=True, help='')
    malformation = fields.Boolean('Malformation', required=True, help='')
    aucune = fields.Boolean('Aucune', required=True, help='')

    # COMPTAGES
    comptage = fields.Boolean('Utiliser les comptages', help='Cochez un type')
    nom_comptage = fields.Char('Nom comptage', required=True)
    unite_densite = fields.Selection([
        ('millier', 'Millier par hectare'),
        ('million', 'Million par hectare'),
        ('thousand', 'Thousand per square meter '),
        ('unite', 'Unité par hectare'),
        ('unite', 'Unité par mètre carré'),
    ], default="millier", string="Unité de densité de semis", required=True)
    unite_longueur = fields.Selection([
        ('centimetre', 'Centimètre'),
        ('kilometre', 'Kilomètre'),
        ('metre', 'Mètre'),
        ('millimetre', 'Millimètre'),
    ], string="Unité de longueur d'échantillonnage", required=True)
    pourcentage = fields.Integer('Pourcentage de germination attendu', required=True)
    densite_theorique = fields.Integer('Densité théorique de semis', required=True)
    nombre_theorique = fields.Integer('Nombre théorique de graines', required=True)

    # SAISONNALITE
    saisonnalite = fields.Boolean('Utiliser les saisonnalites', help='Cochez un type')
    nom_saisonnalite = fields.Char('Nom Saison', required=True)

    # ITINERAIRE CULTURAUX
    itineraire = fields.Boolean('Utiliser les itineraires techniques', help='Cochez un type')
    nom_itineraire = fields.Char('Nom', required=True)
    date_semis = fields.Boolean('Date de semis prévisionnelle', help='')
    date_recolte = fields.Boolean('Date de récolte prévisionnelle', help='')
    intrui = fields.Boolean('intrui', help='')
    date_itineraire = fields.Datetime('Date')
    jour = fields.Integer('Nombre de Jour')
    espece = fields.Selection([
        ('abeille', 'Abeille'),
        ('mouton', 'Mouton'),
        ('autruche', 'Autruche'),
    ], string="Espèce", required=True)
    duree_vie = fields.Integer('Durée de vie (ans)', required=True)

    prod_reference = fields.Selection([
        ('ananas', 'Agriculture biologique'),
        ('abricotier', 'Agriculture conventionnelle'),
        ('ail', 'Agriculture de conservation'),
        ('agnelique', 'Agriculture durable'),
    ], string="Production de référence")
    annee_production = fields.Selection([
        ('n+1', 'N+1'),
        ('n+2', 'N+2'),
        ('n+3', 'N+3'),
        ('n+4', 'N+4'),
        ('n+5', 'N+5'),
    ], string="1ére année de production (année N)")


 # PRODUCTION ANIMALE
class ProdAnimal(models.Model):
    _name = 'activite.animal'
    _rec_name = 'espece'

    admin_id = fields.Many2one('activite.production', string="Admin ID")
    espece = fields.Selection([
        ('abeille', 'Abeille'),
        ('mouton', 'Mouton'),
        ('autruche', 'Autruche'),
    ], string="Espèce", required=True)
    duree_vie = fields.Integer('Durée de vie (ans)', required=True)


# TRANFORMATION
class Transformation(models.Model):
    _name = 'activite.transformation'
    _rec_name = 'nom'

    admin_id = fields.Many2one('activite.production', string="Admin ID")
    agreage = fields.Boolean('Utiliser les agréages', help='Cochez un type')
    piece = fields.Boolean("Mesurer le nombre de pièces de l'échantillon", help='Cochez un type')
    masse_nette = fields.Boolean("Mesurer la masse nette de l'échantillon", help='Cochez un type')
    unite = fields.Selection([
        ('microgramme', 'Microgramme'),
        ('milligramme', 'Milligramme'),
        ('gramme', 'Gramme'),
        ('kilogramme', 'Kilogramme'),
        ('quintal', 'Quintal'),
        ('tonne', 'Tonne'),
    ], string="Unité utilisée pour la masse nette")
    echantillon = fields.Boolean("Mesurer les extremas de l'échantillon", help='Cochez un type')
    indicateur = fields.Selection([
        ('calibre', 'Calibre'),
        ('cumul', 'Cumul des participations'),
        ('diametre', 'Diamètre'),
        ('hauteur', 'Hauteur'),
        ('intervalle', 'Intervalle inter-rangs'),
        ('intervalle', 'Intervalle inter-pieds'),
        ('largeur', 'Largeur'),
        ('largeur', 'Largeur de travail'),
        ('longueur', 'Longueur'),
        ('longueur', 'Longueur nette'),
        ('profondeur', 'Profondeur du sol'),
        ('zone', 'Zone non traitée(ZNT)'),
    ], string="Indicateur utilisé pour la mesure des extremas")
    unite_extrema = fields.Selection([
        ('centimetre', 'Centimètre'),
        ('kilometre', 'Kilomètre'),
        ('metre', 'Mètre'),
        ('millimetre', 'Millimètre'),
    ], string="Unité utilisée pour la mesure des extremas")
    indicateur_taille = fields.Selection([
        ('calibre', 'Calibre'),
        ('capacite', 'Capacité de stockage massique maximale'),
        ('capacite', 'Capacité de stockage massique minimale'),
        ('cumul', 'Cumul des participations'),
        ('diametre', 'Diamètre'),
        ('hauteur', 'Hauteur'),
        ('intervalle', 'Intervalle inter-rangs'),
        ('intervalle', 'Intervalle inter-pieds'),
        ('largeur', 'Largeur'),
        ('largeur', 'Largeur de travail'),
        ('longueur', 'Longueur'),
        ('longueur', 'Longueur nette'),
        ('masse', 'Masse nette'),
        ('poids', 'Poids de mille grains'),
        ('poids', 'Poids frais'),
    ], string="Indicateur de taille", required=True)
    unite_taille = fields.Selection([
        ('centimetre', 'Centimètre'),
        ('gramme', 'Gramme'),
        ('kilogramme', 'Kilogramme'),
        ('kilometre', 'Kilomètre'),
        ('metre', 'mètre'),
        ('millimetre', 'Millimètre'),
        ('microgramme', 'Microgramme'),
        ('milligramme', 'Milligramme'),
        ('quintal', 'Quintal'),
        ('tonne', 'Tonne'),
    ], string="Unité de taille", required=True)
    valeur_min = fields.Integer(string="Valeur minimale", required=True)
    valeur_max = fields.Integer(string="Valeur maximale", required=True)
    commercialisable = fields.Boolean('Commercialisable', help='Cochez un type')
    nom = fields.Char('Nom qualité', required=True)
    maladie = fields.Boolean('Maladie', required=True, help='')
    malformation = fields.Boolean('Malformation', required=True, help='')
    aucune = fields.Boolean('Aucune', required=True, help='')

    # COMPTAGES
    comptage = fields.Boolean('Utiliser les comptages', help='Cochez un type')
    nom_comptage = fields.Char('Nom comptage', required=True)
    unite_densite = fields.Selection([
        ('millier', 'Millier par hectare'),
        ('million', 'Million par hectare'),
        ('thousand', 'Thousand per square meter '),
        ('unite', 'Unité par hectare'),
        ('unite', 'Unité par mètre carré'),
    ], default="millier", string="Unité de densité de semis", required=True)
    unite_longueur = fields.Selection([
        ('centimetre', 'Centimètre'),
        ('kilometre', 'Kilomètre'),
        ('metre', 'Mètre'),
        ('millimetre', 'Millimètre'),
    ], string="Unité de longueur d'échantillonnage", required=True)
    pourcentage = fields.Integer('Pourcentage de germination attendu', required=True)
    densite_theorique = fields.Integer('Densité théorique de semis', required=True)
    nombre_theorique = fields.Integer('Nombre théorique de graines', required=True)

    # SAISONNALITE
    saisonnalite = fields.Boolean('Utiliser les saisonnalites', help='Cochez un type')
    nom_saisonnalite = fields.Char('Nom Saison', required=True)

    # ITINERAIRE CULTURAUX
    itineraire = fields.Boolean('Utiliser les itineraires techniques', help='Cochez un type')
    nom_itineraire = fields.Char('Nom', required=True)
    date_semis = fields.Boolean('Date de semis prévisionnelle', help='')
    date_recolte = fields.Boolean('Date de récolte prévisionnelle', help='')
    intrui = fields.Boolean('intrui', help='')
    date_itineraire = fields.Datetime('Date')
    jour = fields.Integer('Nombre de Jour')
    lost = fields.Boolean('lost', required=True)

# VINIFICATION
class Vinification(models.Model):
    _name = 'activite.vinification'

    admin_id = fields.Many2one('activite.production', string="Admin ID")
    agreage = fields.Boolean('Utiliser les agréages', help='Cochez un type')
    piece = fields.Boolean("Mesurer le nombre de pièces de l'échantillon", help='Cochez un type')
    masse_nette = fields.Boolean("Mesurer la masse nette de l'échantillon", help='Cochez un type')
    unite = fields.Selection([
        ('microgramme', 'Microgramme'),
        ('milligramme', 'Milligramme'),
        ('gramme', 'Gramme'),
        ('kilogramme', 'Kilogramme'),
        ('quintal', 'Quintal'),
        ('tonne', 'Tonne'),
    ], string="Unité utilisée pour la masse nette")
    echantillon = fields.Boolean("Mesurer les extremas de l'échantillon", help='Cochez un type')
    indicateur = fields.Selection([
        ('calibre', 'Calibre'),
        ('cumul', 'Cumul des participations'),
        ('diametre', 'Diamètre'),
        ('hauteur', 'Hauteur'),
        ('intervalle', 'Intervalle inter-rangs'),
        ('intervalle', 'Intervalle inter-pieds'),
        ('largeur', 'Largeur'),
        ('largeur', 'Largeur de travail'),
        ('longueur', 'Longueur'),
        ('longueur', 'Longueur nette'),
        ('profondeur', 'Profondeur du sol'),
        ('zone', 'Zone non traitée(ZNT)'),
    ], string="Indicateur utilisé pour la mesure des extremas")
    unite_extrema = fields.Selection([
        ('centimetre', 'Centimètre'),
        ('kilometre', 'Kilomètre'),
        ('metre', 'Mètre'),
        ('millimetre', 'Millimètre'),
    ], string="Unité utilisée pour la mesure des extremas")
    indicateur_taille = fields.Selection([
        ('calibre', 'Calibre'),
        ('capacite', 'Capacité de stockage massique maximale'),
        ('capacite', 'Capacité de stockage massique minimale'),
        ('cumul', 'Cumul des participations'),
        ('diametre', 'Diamètre'),
        ('hauteur', 'Hauteur'),
        ('intervalle', 'Intervalle inter-rangs'),
        ('intervalle', 'Intervalle inter-pieds'),
        ('largeur', 'Largeur'),
        ('largeur', 'Largeur de travail'),
        ('longueur', 'Longueur'),
        ('longueur', 'Longueur nette'),
        ('masse', 'Masse nette'),
        ('poids', 'Poids de mille grains'),
        ('poids', 'Poids frais'),
    ], string="Indicateur de taille", required=True)
    unite_taille = fields.Selection([
        ('centimetre', 'Centimètre'),
        ('gramme', 'Gramme'),
        ('kilogramme', 'Kilogramme'),
        ('kilometre', 'Kilomètre'),
        ('metre', 'mètre'),
        ('millimetre', 'Millimètre'),
        ('microgramme', 'Microgramme'),
        ('milligramme', 'Milligramme'),
        ('quintal', 'Quintal'),
        ('tonne', 'Tonne'),
    ], string="Unité de taille", required=True)
    valeur_min = fields.Integer(string="Valeur minimale", required=True)
    valeur_max = fields.Integer(string="Valeur maximale", required=True)
    commercialisable = fields.Boolean('Commercialisable', help='Cochez un type')
    nom = fields.Char('Nom qualité', required=True)
    maladie = fields.Boolean('Maladie', required=True, help='')
    malformation = fields.Boolean('Malformation', required=True, help='')
    aucune = fields.Boolean('Aucune', required=True, help='')

    # COMPTAGES
    comptage = fields.Boolean('Utiliser les comptages', help='Cochez un type')
    nom_comptage = fields.Char('Nom comptage', required=True)
    unite_densite = fields.Selection([
        ('millier', 'Millier par hectare'),
        ('million', 'Million par hectare'),
        ('thousand', 'Thousand per square meter '),
        ('unite', 'Unité par hectare'),
        ('unite', 'Unité par mètre carré'),
    ], default="millier", string="Unité de densité de semis", required=True)
    unite_longueur = fields.Selection([
        ('centimetre', 'Centimètre'),
        ('kilometre', 'Kilomètre'),
        ('metre', 'Mètre'),
        ('millimetre', 'Millimètre'),
    ], string="Unité de longueur d'échantillonnage", required=True)
    pourcentage = fields.Integer('Pourcentage de germination attendu', required=True)
    densite_theorique = fields.Integer('Densité théorique de semis', required=True)
    nombre_theorique = fields.Integer('Nombre théorique de graines', required=True)

    # SAISONNALITE
    saisonnalite = fields.Boolean('Utiliser les saisonnalites', help='Cochez un type')
    nom_saisonnalite = fields.Char('Nom Saison', required=True)

    # ITINERAIRE CULTURAUX
    itineraire = fields.Boolean('Utiliser les itineraires techniques', help='Cochez un type')
    nom_itineraire = fields.Char('Nom', required=True)
    date_semis = fields.Boolean('Date de semis prévisionnelle', help='')
    date_recolte = fields.Boolean('Date de récolte prévisionnelle', help='')
    intrui = fields.Boolean('intrui', help='')
    date_itineraire = fields.Datetime('Date')
    jour = fields.Integer('Nombre de Jour')
    lost = fields.Boolean('lost', required=True)


class Administratif(models.Model):
    _name = 'activite.administratif'
    _rec_name = 'montant_total'

    produit_id = fields.Many2one(comodel_name='new.variable', string="Nouvelle Variante de produit")
    admin_id = fields.Many2one(comodel_name='activite.production', string="Admin ID")
    montant_recette = fields.Float(string='Montant des recettes')
    montant_depense = fields.Float(string='Montant des dépenses')
    montant_total = fields.Float(string='Solde', compute='_get_montant')

    depense_id = fields.One2many('create.depense', 'depense_admin_id', string="Ajouter une dépense")
    recette_id = fields.One2many('create.recette', 'recette_admin_id', string="Ajouter une recette")

    # @api.depends('montant_total')

    @api.depends('depense_id', 'recette_id')
    def _get_montant(self):
        self.montant_total = 0
        if self.depense_id.montant_depense and self.recette_id.montant_recette:
            self.montant_total = self.depense_id.montant_depense + self.recette_id.montant_recette


class Depense(models.Model):
    _name = 'create.depense'
    _rec_name = 'montant_depense'

    produit_id = fields.Many2one(comodel_name='new.variable', string="Variante de produit")
    depense_admin_id = fields.Many2one(comodel_name='activite.administratif', string="Admin depense ID")
    methode_calcul = fields.Selection([('campagne', 'Par campagne')])
    quantite = fields.Integer(string="Quantité")
    prix_unitaire = fields.Float(string="Prix unitaire")
    montant_depense = fields.Float(string='Montant', compute='_get_montant_depense')

    @api.depends('quantite', 'prix_unitaire')
    def _get_montant_depense(self):
        self.montant_depense = 0
        if self.quantite and self.prix_unitaire:
            self.montant_depense = self.quantite * self.prix_unitaire


class Recette(models.Model):
    _name = 'create.recette'
    _rec_name = 'montant_recette'

    # Recette
    produit_id = fields.Many2one(comodel_name='new.variable', string="Variante de produit")
    recette_admin_id = fields.Many2one(comodel_name='activite.administratif', string="Admin recette ID")
    methode_calcul_recette = fields.Selection([('campagne', 'Par campagne')])
    quantite_recette = fields.Integer(string="Quantité")
    prix_unitaire_recette = fields.Float(string="Prix unitaire")
    montant_recette = fields.Float(string='Montant', compute='_get_montant_recette')

    @api.depends('quantite_recette', 'prix_unitaire_recette')
    def _get_montant_recette(self):
        self.montant_recette = 0
        if self.quantite_recette and self.prix_unitaire_recette:
            self.montant_recette = self.quantite_recette * self.prix_unitaire_recette


    # def name_get(self):
    #     result = []
    #     for rec in self:
    #         name = rec.famille + ' ' + rec.name
    #         result.append(rec.id, name)
    #         return result

    # @api.onchange('agreage')
    # def _agreage(self):
    #     if self.agreage:
    #         self.piece = False
    #     else:
    #         self.piece = True