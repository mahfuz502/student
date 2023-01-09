from odoo import api, fields, models, _

class Registration(models.Model):
    _name = 'school.registration'
    _description = 'registration'
    section_id = fields.Many2one('Section Name','school.section')
    course_id = fields.Many2one('Course','school.course')
    teacher_id = fields.Many2one('Teacher','achool,.teacher')
    student_ids = fields.Many2many('Student List','school.student','registration_student_rel','registration_id','student_id')