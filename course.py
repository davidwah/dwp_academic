from odoo import api, fields, models 


class Course(models.Model):
    _name = "academic.course"

    name = fields.Char("Name", required=True, size=100)
    description = fields.Text(string="Description", required=False, )
    responsible_id = fields.Many2one(comodel_name="res.users", string="Responsible", required=True)
    
    session_ids = fields.One2many(comodel_name="academic.session", string="Session",
        inverse_name="course_id")

    
    
