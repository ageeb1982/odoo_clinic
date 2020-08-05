# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ClinicBooking(models.Model):
    ###############################
    # كلاس حجز عند الطبيب
    ###############################
    _name = 'clinic.booking'
    _description = "object contain all doctor data"

    state = fields.Selection([('draft', 'البداية-المسودة'), ('wait_d_meeting', 'انتظار الدخول على الطبيب'),
                              ('stay_on_ward', 'تنويم في العنبر'), ('medical_bill', 'صرف روشته')], string='االوضع الحالي', default='draft')
    patient_id = fields.Many2one(
        'clinic.patient', string='اسم المريض', required=True)
    doctor_id = fields.Many2one(
        'clinic.doctor', string='اسم الطبيب', required=True)
    date = fields.Date(string=" االتاريخ", default=fields.date.today())
    meeting_date = fields.Date(string="تاريخ المقابلة", required=True)
    paid_fees = fields.Boolean(string="هل تم الدفع؟")
    note = fields.Html(string="ملاحظات")

    @api.one
    def action_to_wait_d_meeting(self):
        """عن طريق موظف الإستقبال يحول حالة المريض من البداية إلى انتظار الطبيب"""
        if self.paid_fees == False:
            raise ValidationError(_("هذا المريض لم يدفع قيمة الكشف !"))
        self.state = 'wait_d_meeting'

    @api.one
    def clinic_ward_action(self):
        """يقوم الطبيب بتحويل الحالة إلى ان ينوم المريض في المستشفى"""
        self.patient_id.write({'met_doctor': True})
        self.patient_id.write({'last_meeting': self.meeting_date})
        # يقوم بتسجيل انه تم زيارة للطبيب بتاريخ معين
        self.state = 'stay_on_ward'

    @api.one
    def medical_bill_action(self):
        """يحول الدالة إلى صرف روشته علاج"""
        self.patient_id.write({'met_doctor': True})
        self.patient_id.write({'last_meeting': self.meeting_date})
        # يقوم بتسجيل انه تم زيارة للطبيب بتاريخ معين
        self.state = 'medical_bill'
   
