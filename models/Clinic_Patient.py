# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ClinicPatient(models.Model):
    _name = 'clinic.patient'
    _description = "لعرض كل بيانات المرضى"

    first_name = fields.Char(string='الاسم الأول', required=True)
    second_name = fields.Char(string='الاسم الثاني', required=True)
    third_name = fields.Char(string='الاسم الثالث', required=True)
    forth_name = fields.Char(string='الاسم الرابع', required=True)

    name = fields.Char(string="الاسم كامل", readonly=True,
                       compute='get_full_name')
    image = fields.Binary(string='الصورة', copy=False)
    gender = fields.Selection(
        [('ذكر', 'ذكر'), ('أثنى', 'أنثى')], string='الجنس', default='ذكر', required=True)
    birth_day = fields.Date(string='تاريخ الميلاد', required=True)
    met_doctor = fields.Boolean(string='زار الطبيب؟')
    last_meeting = fields.Date(string='آخر زيارة')
    age_year = fields.Integer(string="سنوات", compute='calculate_age')
    age_month = fields.Integer(string="شهور", compute='calculate_age')
    age_day = fields.Integer(string="أيام", compute='calculate_age')
    country_id = fields.Many2one('res.country', string="الدولة")
    phone = fields.Char(string="رقم الهاتف")
    doctor_id = fields.Many2one('clinic.doctor', string='الطبيب')
    
    @api.one
    def get_full_name(self):
        """
                        دالة لجلب الإسم كاملاً
                        """
        self.name = self.first_name+' '+self.second_name + \
            ' '+self.third_name+' '+self.forth_name

    @api.one
    def calculate_age(self):
        """
        دالة لحساب عمر المريض

        """
        if self.birth_day:
            birth_day = str(self.birth_day)
            current_date = str(fields.Date.today())
            birth_day_year_as_int = int(
                birth_day[0]+birth_day[1]+birth_day[2]+birth_day[3])
            birth_day_month_as_int = int(birth_day[5]+birth_day[6])
            birth_day_day_as_int = int(birth_day[8]+birth_day[9])

            current_date_year_as_int = int(
                current_date[0]+current_date[1]+current_date[2]+current_date[3])
            current_date_month_as_int = int(current_date[5]+current_date[6])
            current_date_day_as_int = int(current_date[8]+current_date[9])

            period_years = current_date_year_as_int-birth_day_year_as_int
            period_months = current_date_month_as_int-birth_day_month_as_int
            period_days = current_date_day_as_int-birth_day_day_as_int

            months_list_1 = ['04', '06', '09', '11']
            months_list_2 = ['01', '03', '05', '07', '08', '10', '12']

            if period_days < 0:
                if str(current_date_month_as_int) == '02':
                    if current_date_year_as_int % 4 == 0:
                        period_days = 29+period_days
                    if current_date_year_as_int % 4 != 0:
                        period_days = 28+period_days
                for index in range(0, 4):
                    if current_date_month_as_int == int(months_list_1[index]):
                        period_days = 30+period_days
                for index in range(0, 7):
                    if current_date_month_as_int == int(months_list_2[index]):
                        period_days = 31+period_days
                period_months = period_months-1
            if period_months < 0:
                period_months = 12+period_months
                period_years = period_years-1

            self.age_year = period_years
            self.age_month = period_months
            self.age_day = period_days

    @api.constrains('phone')
    def phone_validation(self):
        """
        دالة التأكد من رقم الهاتف
        """
        phone_prefix = [1, 9]
        phone_type = [0, 1, 2, 6, 9]
        check_value = 0

        if self.phone and self.country_id:
            # if self.country_id.code == 'SD':
            phone = self.phone
            if len(phone) != 9:
                raise ValidationError(
                    _("خطأ في رقم الهاتف -عدد الأرقام غير صحيح"))
            if len(phone) == 9:
                for index in range(0, len(phone_prefix)):
                    if phone[0] == str(phone_prefix[index]):
                        check_value = 1
                if check_value == 0:
                    raise ValidationError(
                        _("خطأ في رقم الهاتف - يجب ان يبدأ الرقم ب1 ارقام سوداني - أو 9 ارقام زين وام تي ان"))
                check_value = 0
                for index in range(0, len(phone_type)):
                    if phone[1] == str(phone_type[index]):
                        check_value = 1
                if check_value == 0:
                    raise ValidationError(
                        _("خطأ في رقم الهاتف - هذا الرقم غير حقيقي"))
                check_value = 0
                for index in range(0, len(phone)):
                    check_value = 0
                for number in range(0, 10):
                    if phone[index] == str(number):
                        check_value = 1
                if check_value == 0:
                    raise ValidationError(
                        _("خطأ في رقم الهاتف - يجب ان لا يحتوى الرقم على حروف"))
