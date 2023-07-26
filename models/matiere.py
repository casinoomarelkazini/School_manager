from odoo import fields, models

class Matiere(models.Model):
    _name = 'school.matiere'
    _description = 'Matiere Model'

    name = fields.Char()
    code = fields.Char()