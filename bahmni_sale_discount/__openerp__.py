{
    "name": "Bahmni Sale Discount",
    "version": "1.0",
    "depends": ["base","sale","account"],
    "author": "ThoughtWorks Technologies Pvt. Ltd.",
    "category": "Sale",
	"summary": "Sale Discount ",
    "description": """
    """,
    'data': ['sale_discount_price_view.xml','invoice_discount_view.xml','quotation_view.xml'],
    'js': ['static/src/js/*.js'],
    'qweb': ['static/src/xml/*.xml'],
    'demo': [],
    'auto_install': False,
    'application': True,
    'installable': True,
#    'certificate': 'certificate',
}
