# BY : Omar elkazini
# Visite https://github.com/casinoomarelkazini/School_manager for more information

from odoo import fields, models


class SaleOrder(models.Model):
    # python-inherited models
    _inherit = 'sale.order'

    # new field to add to 'sale.order' model after of the 'date_order' field
    additional_note = fields.Char(string='Additional Note')

