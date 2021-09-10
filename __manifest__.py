# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Production Agricole',
    'version' : '1.1',
    'summary': 'Application de production agricole',
    'sequence': 15,
    'description': """
Invoicing & Payments
====================
The specific and easy-to-use Invoicing system in Odoo allows you to keep track of your accounting, even when you are not an accountant. It provides an easy way to follow up on your vendors and customers.

You could use this simplified accounting in case you work with an (external) account to keep your books, and you still want to keep track of payments. This module also offers you an easy method of registering payments, without having to encode complete abstracts of account.
    """,
    'category': 'Production Application',
    'website': 'https://www.odoo.com/page/billing',
    'images' : ['images/accounts.jpeg','images/bank_statement.jpeg','images/cash_register.jpeg','images/chart_of_accounts.jpeg','images/customer_invoice.jpeg','images/journal_entries.jpeg'],
    'depends' : ['base','web'],
    'data': [
            'security/ir.model.access.csv',
            'views/dashboard_view.xml',
            'views/nubium_production_view.xml',
            'intervensions/create_admin_inter.xml',
            'intervensions/equipe.xml',
            'intervensions/etiquette.xml',
            'intervensions/journal.xml',
            'intervensions/paiement.xml',
            'intervensions/personne.xml',
            'intervensions/prescripteur.xml',
            'intervensions/prescription.xml',
            'intervensions/responsable.xml',
            'intervensions/tresorerie.xml',
            'views/activite_production_view.xml',
            'views/equipement_production_view.xml',
            'views/intervension_production_view.xml',
            'views/nubium_qualite_view.xml',
            'views/analyse_qualite_view.xml',
            'views/incidence_qualite_view.xml',
            'views/agreage_qualite_view.xml',
            'views/comptage_qualite_view.xml',
            'views/nubium_parcellaire_view.xml',
            'views/zone_parcellaire_view.xml',
            'views/culture_parcellaire_view.xml',
            'views/parcelle_parcellaire_view.xml',
            'views/settings.xml',
            'views/produit.xml',
            'views/transformation_view.xml',
            'views/vinification_view.xml',
            'views/viticole_view.xml',
            'views/animal_view.xml',
            'views/administratif_view.xml',
            'views/vegetal_view.xml',
            'views/prestation_view.xml',
            # 'views/activite_production_administratif_view.xml',
            # 'wizards/create_administratif.xml',
            # 'wizards/create_maintenance.xml',
            # 'wizards/create_prestation.xml',
            # 'wizards/create_productionanimale.xml',
            # 'wizards/create_productionviticole.xml',
            # 'wizards/create_productionvegetale.xml',
            # 'wizards/create_transformation.xml',
            # 'wizards/create_vinification.xml',
    ],
    'demo': [
    
    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
