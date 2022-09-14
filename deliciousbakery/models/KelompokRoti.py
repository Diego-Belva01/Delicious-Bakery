from odoo import api, fields, models


class KelompokRoti(models.Model):
    _name = 'deliciousbakery.kelompokroti'
    _description = 'New Description'

    name = fields.Selection([
        ('spesial tart', 'Spesial Tart'),
        ('spesial bakery', 'Spesial Bakery'),
        ('spesial pastry', 'Spesial Pastry'),
        ('spesial donuts', 'Spesial Donuts'),
        ('spesial cake', 'Spesial Cake'),
    ], string='Nama Kelompok')

    kode_kelompok = fields.Char(string='Kode Kelompok')

    @api.onchange('name')
    def _onchange_kode_kelompok(self):
        if self.name == 'spesial tart':
            self.kode_kelompok = 'SPESIAL_TART'
        if self.name == 'spesial bakery':
            self.kode_kelompok = 'SPESIAL_BAKERY'
        if self.name == 'spesial pastry':
            self.kode_kelompok = 'SPESIAL_PASTRY'
        if self.name == 'spesial donuts':
            self.kode_kelompok = 'SPESIAL_DONUTS'    
        if self.name == 'spesial cake':
            self.kode_kelompok = 'SPESIAL_CAKE'

    kode_rak = fields.Char(string='Kode Rak')
    roti_id = fields.One2many(comodel_name='deliciousbakery.roti',
                                inverse_name='kelompokroti_id',
                                string='Daftar Roti')
    jml_item = fields.Char(compute='_compute_jml_item', string='Jml Item')


    @api.depends('roti_id')
    def _compute_jml_item(self):
        for record in self:
            a = self.env['deliciousbakery.roti'].search([('kelompokroti_id', '=', record.id)]).mapped('name')
            b = len(a)
            record.jml_item = b
            record.daftar = a
    
    daftar = fields.Char(string='Daftar isi')