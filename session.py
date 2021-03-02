from odoo import api, fields, models

class Session(models.Model):
    _name = "academic.session"

    name = fields.Char("Name", required=True, size=100)
    

    course_id = fields.Many2one(comodel_name="academic.course", string="Course", required=True, )
    instructor_id = fields.Many2one(comodel_name="res.partner", string="Instructor", required=False, )
    start_date = fields.Date(string="Start Date", required=False, )
    duration = fields.Integer(string="Duration", required=False, )
    seats = fields.Integer(string="Seats", required=False, )
    active = fields.Boolean(string="Active", default=True)

    attendee_ids = fields.One2many(comodel_name='academic.attendee', 
        inverse_name='session_id', 
        string='Attendees')

    taken_seats = fields.Float(string="Taken Seats", 
        compute="_compute_taken_seats")
    
    
    def _compute_taken_seats(self):
        for x in self:
            x.taken_seats = 99.9
    
    
    
    
    