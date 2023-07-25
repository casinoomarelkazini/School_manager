from odoo import api, fields, models

class Teacher(models.Model):
    _name = 'school.teacher'
    _description = 'Teacher Record'
    _inherit = ['mail.thread']
    _order = 'name'

    # Fields
    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    photo = fields.Binary(string='Image')
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ('others', 'Others')],
        string='Gender')
    teacher_dob = fields.Date(string="Date of Birth")
    teacher_blood_group = fields.Selection(
        [('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
         ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
        string='Blood Group')
    nationality = fields.Many2one('res.country', string='Nationality')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancel', 'Cancel')],
        string='State', default='draft')

    # Computed Field
    level_education = fields.Selection([
        ('kinder_garden', 'Kinder Garden'),
        ('primary', 'Primary'),
        ('secondary', 'Secondary')],
        string='Level of Education', compute='_compute_level_education', store=True)

    @api.depends('age')
    def _compute_level_education(self):
        for rec in self:
            if rec.age < 1:
                rec.level_education = "kinder_garden"
            elif (rec.age >= 1) and (rec.age < 2):
                rec.level_education = "kinder_garden"
            elif (rec.age >= 2) and (rec.age < 10):
                rec.level_education = "primary"
            else:
                rec.level_education = "secondary"

    # Methods for handling state
    def button_done(self):
        for rec in self:
            rec.state = 'done'
    
    def button_reset(self):
        for rec in self:
            rec.state = 'draft'
    
    def button_cancel(self):
        for rec in self:
            rec.state = 'cancel'
