from odoo import api, fields, models


class Attendee(models.Model):
    _name = "academic.attendee"

    name = fields.Char(string='Name', required=True, size=100)
    