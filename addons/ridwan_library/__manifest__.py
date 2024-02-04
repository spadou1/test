{
    'name': 'Ridwan Library',
    'version': '15.1.0',
    'summary': 'Ridwan library books and engaged management ',
    'category': 'Library',
    'author': 'Nour Elyakine Saci',
    'maintainer': 'Nour Elyakine Saci',
    'license': 'LGPL-3',
    'depends': [
        'contacts',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/ridwan_library_book.xml',
        'views/ridwan_library_book_author.xml',
        'views/ridwan_library_book_pub_house.xml',
        'views/ridwan_library_book_copy.xml',
        'views/ridwan_library_book_copy_loan.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}
