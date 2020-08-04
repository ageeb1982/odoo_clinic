# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo import api, fields, models, _


class DoctorSpecialty(models.Model):
    _name = 'doctor.specialty'
    _description = "تخصصات الأطباء"

    name = fields.Char(string='اسم التخصص')
    doctor_id = fields.One2many(
        'clinic.doctor', 'specialty', string='الاطباء')
