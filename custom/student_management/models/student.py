from odoo import api, fields, models, tools, _

class SchoolModel(models.Model):
    _name = "school.init"
    _description = "My Model Names"

    ID = fields.Char(string="ID_")
    name = fields.Char(string="Name")
    roll = fields.Char(string="Roll")
    group = fields.Char(string="Group")
    address = fields.Char(string="Address")
    phone = fields.Char(string="Phone")

# class SchoolModel2(models.Model):
#     _name = "school.init"
#     _description = "My Model Names"
#
#     des = fields.Char(string="description")