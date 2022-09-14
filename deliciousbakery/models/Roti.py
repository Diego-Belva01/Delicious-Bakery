from odoo import api, fields, models


class Roti(models.Model):
    _name = 'deliciousbakery.roti'
    _description = 'New Description'

    name = fields.Char(string='Nama Roti')
    harga_beli = fields.Integer(string='Harga Modal', required=True)
    harga_jual = fields.Integer(string='Harga Jual', required=True)
    kelompokroti_id = fields.Many2one(comodel_name='deliciousbakery.kelompokroti',
                                        string='Kelompok Roti',
                                        ondelete='cascade')

    supplier_id = fields.Many2many(comodel_name='deliciousbakery.supplier', string='Supplier')
    stok = fields.Integer(string='Stok')
    
