from __future__ import unicode_literals
import json
import codecs

class SaveJSONPipeline(object):
    def __init__(self):
        self.file = codecs.open('birds.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        for row in item['page']:
            line = json.dumps(row, ensure_ascii=False) + "\n"
            self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()

