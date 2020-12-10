# -*- coding: utf-8 -*-

from flectra import models, fields

# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'

#     name = fields.Char()

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Records'

    patient_name = fields.Char(String='Name', required=True)
    patient_age = fields.Integer('Age')
    notes = fields.Text(String='Notes')
    image = fields.Binary(String='Image')