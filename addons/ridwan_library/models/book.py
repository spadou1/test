from odoo import _, api, fields, models


class RidwanLibraryBookAuthor(models.Model):
    _name = 'ridwan_library.book.author'
    _description = 'Authors'

    name = fields.Char(
        string='Name',
        required=True, 
    )

    book_ids = fields.One2many(
        comodel_name='ridwan_library.book',
        inverse_name='author_id',
        string='Books'
    )


class RidwanLibraryBookPubHouse(models.Model):
    _name = 'ridwan_library.book.pub_house'
    _desctiption = 'Publishing Houses'

    name = fields.Char(
        string='Name',
        required=True
    )

    book_ids = fields.One2many(
        comodel_name='ridwan_library.book',
        inverse_name='publishing_house_id',
        string='Books'
    )
    
    code_qr = fields.Char(
        string='Code QR'
    )
class RidwanLibraryBookCopyLoan(models.Model):
    _name = 'ridwan_library.book.copy.loan'
    _description = 'Book Copies Loan'
    
    copy_id = fields.Many2one(
        comodel_name='ridwan_library.book.copy', 
        string='Copy'
    )
    
    engaged_id = fields.Many2one(
        comodel_name='res.partner', 
        string='Engaged'
    )
    
    from_date = fields.Date(
        string='From'
    )
    
    to_date = fields.Date(
        string='To'
    )


class RidwanLibraryBookCopy(models.Model):
    _name = 'ridwan_library.book.copy'
    _description = 'Book Copies'

    name = fields.Char(
        string='Inventory Number',
        required=True
    )

    book_id = fields.Many2one(
        comodel_name='ridwan_library.book',
        string='Book'
    )

    state = fields.Selection(
        string='State',
        selection=[
            ('available', 'Available'),
            ('loan', 'Loan')
        ],
        default='available'
    )

    loan_ids = fields.Many2many(
        comodel_name='ridwan_library.book.copy.loan', 
        string='Loans'
    )

    def action_available(self):
        for copy in self:
            copy.state = 'available'
            
    def action_loan(self):
        for copy in self:
            copy.state = 'loan'


class RidwanLibraryBook(models.Model):
    _name = 'ridwan_library.book'
    _description = 'Books'

    name = fields.Char(
        string='Name',
        required=True
    )

    author_id = fields.Many2one(
        comodel_name='ridwan_library.book.author',
        string='Author'
    )

    publishing_house_id = fields.Many2one(
        comodel_name='ridwan_library.book.pub_house',
        string='Publishing House'
    )

    publishing_date = fields.Date(
        string='Publishing Date'
    )

    pages_count = fields.Integer(
        string='Pages Count'
    )

    copy_ids = fields.One2many(
        comodel_name='ridwan_library.book.copy',
        inverse_name='book_id',
        string='Copies'
    )

    copies_count = fields.Integer(
        string='Copies Count',
        compute='_compute_copies_count',
        store=True
    )

    @api.depends('copy_ids')
    def _compute_copies_count(self):
        for book in self:
            book.copies_count = len(book.copy_ids)
