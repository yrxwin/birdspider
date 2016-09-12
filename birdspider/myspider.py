from __future__ import unicode_literals
import scrapy

class BirdSpider(scrapy.Spider):
    def __init__(self):
        self.params = ["id", "", "location", "categories", "recorder", "views", "time"]
    name = 'birdspider'
    start_urls = ['http://www.birdreport.cn/Watch/RecordList4Field?pageIndex=%s' % page for page in xrange(1, 10)]

    def parse(self, response):
        rows = response.xpath('//table/tr/td//text()').extract()
        retRows = []
        row = {}
        for index, ele in enumerate(rows[6:]):
            if index % 7 == 1:
                continue
            if index % 7 == 4:
                ele = ele.strip()
            row[self.params[index % 7]] = ele
            if index % 7 == 6:
                retRows.append(row)
                row = {}
        myItem = {}
        myItem['page'] = retRows
        yield myItem

