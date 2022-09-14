from odoo import fields, models, api


class PenjualanReport(models.TransientModel):
    _name = 'deliciousbakery.penjualanreport'
    _description = 'Description'

    pembeli_id = fields.Many2one(
        comodel_name='res.partner',
        string='Pembeli',
        required=False)
    dari_tgl = fields.Date(
        string='Dari Tanggal',
        required=False)
    ke_tgl = fields.Date(
        string='Ke tanggal',
        required=False)

    def action_penjualan_report(self):
        filter = []
        pembeli_id = self.pembeli_id
        dari_tgl = self.dari_tgl
        ke_tgl = self.ke_tgl
        if pembeli_id:
            filter += [('nama_pembeli', '=', pembeli_id.id)]
        if dari_tgl:
            filter += [('tgl_penjualan', '>=', dari_tgl)]
        if ke_tgl:
            filter += [('tgl_penjualan', '<=', ke_tgl)]
        print(filter)
        penjualan = self.env['deliciousbakery.penjualan'].search_read(filter)
        print(penjualan)
        data = {
            'form': self.read()[0],
            'penjualanxx': penjualan,
        }
        print(data)
        return self.env.ref('deliciousbakery.wizard_penjualanreport_pdf').report_action(self, data=data)