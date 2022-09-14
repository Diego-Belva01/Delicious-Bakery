from odoo import api, fields, models


class Supplier(models.Model):
    _name = 'deliciousbakery.supplier'
    _description = 'New Description'

    name = fields.Char(string='Nama Perushaan')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No. Telepon')
    roti_id = fields.Many2many(comodel_name='deliciousbakery.roti', string='Roti')