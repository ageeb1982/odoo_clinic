# -*- coding: utf-8 -*-
##############################################################
from odoo import fields, models, api, _
import time
from datetime import date
from odoo.exceptions import ValidationError, UserError


class ClinicBookingWiz(models.TransientModel):
    _name = "clinic.booking.report.wiz"
    state = fields.Selection(
        [('draft', 'Draft'), ('wait_d_meeting', 'Wait Doctor Meeting'), ('stay_on_ward', 'Stay On Ward'),
         ('medical_bill', 'Medical Bill')], string='الحالة')
    patient_id = fields.Many2one('clinic.patient', string='المريض')
    doctor_id = fields.Many2one('clinic.doctor', string='الطبيب')
    date = fields.Date(string="التاريخ")
    meeting_date = fields.Date(string="تاريخ الموعد")


    @api.multi
    def print_booking_report(self):
        """
        This Function Get The Data For Booking Reports
        """
        booking_ids = self.env['clinic.booking'].search([])
        data = {}
        booking_list = []
        state = 'no'
        patient_id = 'no'
        doctor_id = 'no'
        date = 'no'
        meeting_date = 'no'
        if self.state:
            for rec in booking_ids:
                if rec.state == self.state:
                    booking_list.append(rec.id)
            booking_ids = booking_ids.search([('id', 'in', booking_list)])
            booking_list = []
            state = str(self.state)

        if self.patient_id:
            for rec in booking_ids:
                if rec.patient_id == self.patient_id:
                    booking_list.append(rec.id)
            booking_ids = booking_ids.search([('id', 'in', booking_list)])
            booking_list = []
            patient_id = str(self.patient_id.name)

        if self.doctor_id:
            for rec2 in booking_ids:
                if rec2.doctor_id == self.doctor_id:
                    booking_list.append(rec2.id)
            booking_ids = booking_ids.search([('id', 'in', booking_list)])
            booking_list = []
            doctor_id = str(self.doctor_id.name)

        if self.date:
            for rec3 in booking_ids:
                self_date = str(self.date)
                rec_date = str(rec3.date)
                if self_date == rec_date:
                    booking_list.append(rec3.id)
            booking_ids = booking_ids.search([('id', 'in', booking_list)])
            booking_list = []
            date = str(self.date)

        if self.meeting_date:
            for rec4 in booking_ids:
                self_meeting_date = str(self.meeting_date)
                rec_meeting_date = str(rec4.meeting_date)
                if self_meeting_date == rec_meeting_date:
                    booking_list.append(rec4.id)
            booking_ids = booking_ids.search([('id', 'in', booking_list)])
            booking_list = []
            meeting_date = str(self.meeting_date)

        for rec5 in booking_ids:
            booking_list.append(rec5.id)
        data = {'booking_ids': booking_list}
        return self.env.ref('clinic.booking_custom_report_action').report_action(self, data=data)


class ClinicBookingReportDetails(models.AbstractModel):
    _name = "report.clinic.booking_custom_report_temp"

    @api.model
    def get_report_values(self, docids, data=None):
        booking_ids = self.env['clinic.booking'].search([('id', '=', data['booking_ids'])])
        docids = docids
        # self.get_menus_skel(docids, data)
        return {
            'data': booking_ids
        }
