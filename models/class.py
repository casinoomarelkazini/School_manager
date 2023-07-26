from odoo import fields, models

class Class(models.Model):
    _name = 'school.class'
    _description = 'Class Model'

    num = fields.Integer()
    name = fields.Char()