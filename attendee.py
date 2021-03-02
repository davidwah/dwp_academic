from odoo import api, fields, models


class Attendee(models.Model):
    _name = "academic.attendee"

    name = fields.Char(string='Reg Number', required=True, size=100)

    session_id = fields.Many2one(comodel_name='academic.session', string='Session')
    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner')
    
    
    