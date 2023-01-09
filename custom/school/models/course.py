from odoo import api, fields, models, _

class course(models.Model):
    _name = 'school.teacher'
    _description = 'teacher'
    name = fields.Char('Section Name', required=True)
    code = fields.Char('Code')
