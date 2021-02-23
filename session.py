from odoo import api, fields, models

class Session(models.Model):
    _name = "academic.session"

    name = fields.Char("Name", required=True, size=100)
    

    course_id = fields.Many2one(comodel_name="academic.course", string="Course", required=False, )
    instructor_id = fields.Many2one(comodel_name="res.partner", string="Instructor", required=False, )
    start_date = fields.Date(string="Start Date", required=False, )
    duration = fields.Integer(string="Duration", required=False, )
    seats = fields.Integer(string="Seats", required=False, )
    active = fields.Boolean(string="Active", )
    
    
    
    
    
    