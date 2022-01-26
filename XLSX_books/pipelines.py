# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import xlsxwriter

class XlsxBooksPipeline:
    @classmethod
    def from_crawler(cls, crawler):
        file_name = crawler.settings.get('XLSX_FILE')
        return cls(xlsx_name=file_name)

    def __init__(self, xlsx_name):
        self.xlsx_name = xlsx_name
        self.worksheet = None
        self.workbook = None
        self.current_roll_index = 0

    def process_item(self, item, spider):
        # spider.logger.info('IN PROCESS ITEM')

        title = item.get('title')
        price = item.get('price')
        stock = item.get('stock')

        self.worksheet.write(self.current_roll_index, 0, title)
        self.worksheet.write(self.current_roll_index, 1, price)
        self.worksheet.write(self.current_roll_index, 2, stock)
        self.current_roll_index = 0

    def process_item(self, item, spider):

        adapter = ItemAdapter(item)
        d = adapter.asdict()
        if self.current_roll_index ==0:
           # writes header
            data = d.keys()
        else:
            # writes values
            data = d.values()

        for col, value in enumerate(data):
                self.worksheet.write(self.current_roll_index, col, value)
        self.current_roll_index += 1
        return item


    def open_spider (self, spider):
        spider.logger.info('IN OPEN SPIDER')
        self.workbook = xlsxwriter.Workbook(self.xlsx_name)
        self.worksheet = self.workbook.add_worksheet()

    def close_spider(self, spider):
        spider.logger.info('IN CLOSE SPIDER')
        self.workbook.close()

