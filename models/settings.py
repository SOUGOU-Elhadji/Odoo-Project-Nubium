# -*- coding: utf-8 -*-
from odoo import models, fields, api,  _
from ast import literal_eval


class ProductionSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    note = fields.Char(string='Default Note')
    module_product = fields.Boolean(string='Production')
    product_ids = fields.Many2many('product.product', string='Productions')

    def set_values(self):
        res = super(ProductionSettings, self).set_values()
        self.env['ir.config_parameter'].set_param('production_agricol_nubium.note', self.note)
        print("test", self.product_ids.ids)
        self.env['ir.config_parameter'].set_param('production_agricol_nubium.product_ids', self.product_ids.ids)
        return res

    @api.model
    def get_values(self):
        res = super(ProductionSettings, self).get_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        notes = ICPSudo.get_param('production_agricol_nubium.note')
        product_ids = self.env['ir.config_parameter'].sudo().get_param('production_agricol_nubium.product_ids')
        if product_ids:
            res.update(
                note=notes,
                product_ids=[(6, 0, literal_eval(product_ids))],
            )
        return res

