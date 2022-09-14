from crypt import methods
import json


import json

from odoo import http, models, fields
from odoo.http import request


class deliciousbakery(http.Controller):
    @http.route('/deliciousbakery/getroti', auth='public', method=['GET'])
    def getBarang(self, **kw):
        # Mengambil semua barang dari table barang
        barang = request.env['deliciousbakery.roti'].search([])
        items = []

        for item in barang:
            items.append({
                'nama_roti': item.name,
                'harga_jual': item.harga_jual,
                'stok': item.stok
            })
        
        return json.dumps(items)

    @http.route('/deliciousbakery/getsupplier', auth='public', method=['GET'])
    def getSupplier(self, **kw):
        supplier = request.env['deliciousbakery.supplier'].search([])
        items = []

        for item in supplier:
            items.append({
                'nama_perusahaan': item.name,
                'alamat': item.alamat,
                'no_telepon': item.no_telp,
                'roti_id': item.roti_id[0].name
            })
        
        return json.dumps(items)