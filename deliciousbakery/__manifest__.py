# -*- coding: utf-8 -*-
{
    'name': "addonsdeliciousbakery/deliciousbakery",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/kelompokroti_view.xml',
        'views/roti_view.xml',
        'views/person_view.xml',
        'views/kasir_view.xml',
        'views/cleaning_view.xml',
        'views/pembeli_view.xml',
        'views/supplier_view.xml',
        'views/direksi_view.xml',
        'views/penjualan_view.xml',
        'report/report.xml',
        'report/PenjualanPdf.xml',
        'report/wizard_penjualanreport_template.xml',
        'wizard/rotidatang_wizard_view.xml',
        'wizard/penjualanreport_wizard_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
