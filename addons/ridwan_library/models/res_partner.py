from odoo import _, api, fields, models


class RidwanResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    ridwan_engagement_number = fields.Char(
        string='Engagement Number'
    )

    ridwan_library_book_copy_loan_ids = fields.One2many(
        comodel_name='ridwan_library.book.copy.loan', 
        inverse_name='engaged_id', 
        string='Loans'
    )
