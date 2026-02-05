
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import re

class ExamPipeline:
    def process_item(self, item, spider):
        if not item.get('answer'):
            raise DropItem("Missing answer in %s" % item)
        if not item.get('question'):
            raise DropItem("Missing question in %s" % item)
        if not item.get('grade'):
            raise DropItem("Missing grade in %s" % item)
        if not item.get('subject'):
            raise DropItem("Missing subject in %s" % item)
        raw_string = item['question'] + '\n' + item['reasoning'] + '\n' + item['answer']
        image_mark = '[[HAS_IMAGE]]'
        if image_mark in raw_string:
            raise DropItem("Item contains image mark in %s" % item)
        regex_pattern = r"Câu\s+(\d+)(\s*)[:.]\s*"
        if re.match(regex_pattern, item['question']):
            item['question'] = re.sub(regex_pattern, '', item['question'], count=1).strip()
        item['question'] = item['question'].strip()
        regex_pattern1 = r"Loigiaihay.com\s*"
        item['reasoning'] = re.sub(regex_pattern1, '', item['reasoning']).strip()
        item['reasoning'] = item['reasoning'].strip()
        item['answer'] = item['answer'].strip()
        return item
