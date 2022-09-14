from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'New Description'

    is_pembeli = fields.Boolean(string='Is Pembeli')
    is_direksi = fields.Boolean(string='Is Direksi')
    poin = fields.Integer(string='Poin')
    level = fields.Char(string='Level')