BOT_NAME = 'XLSX_books'

SPIDER_MODULES = ['XLSX_books.spiders']
NEWSPIDER_MODULE = 'XLSX_books.spiders'

XLSX_FILE = 'books.xlsx'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure item pipelines
ITEM_PIPELINES = {
    'XLSX_books.pipelines.XlsxBooksPipeline': 300,
}

