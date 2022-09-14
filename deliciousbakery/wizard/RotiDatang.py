from odoo import api, fields, models


'''
Membuat model BarangDarang yang inherit
ke Transient Model, Odoo 14 ke atas harus
di daftarkan di security
'''
class RotiDatang(models.TransientModel):
    _name = 'deliciousbakery.rotidatang'

    roti_id = fields.Many2one(comodel_name='deliciousbakery.roti', string='Nama Roti', required=True)
    jumlah = fields.Integer(string='Jumlah', required=False)

    def button_roti_datang(self):
        for line in self:
            self.env['deliciousbakery.roti'].search([('id', '=', line.roti_id.id)]).write(
                {'stok': line.roti_id.stok +  line.jumlah}
            )