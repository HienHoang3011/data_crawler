
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import re
from pathlib import Path

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

class PtitPipeline:
    def process_item(self, item, spider):
        if not item.get('text'):
            raise DropItem("Missing text in item")
        if not item.get('key'):
            raise DropItem("Missing key in item")
        
        # Tạo thư mục nếu chưa tồn tại
        output_dir = Path("crawler/chunking/data/ptit")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        output_file = output_dir / f"{item['key']}.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(item['text'])
        
        return item
    
class StemPipeline:
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
        if "bảng" in item['question']:
            raise DropItem("Item contains the word 'bảng' in question %s" % item)
        item['question'] = item['question'].strip()
        string_to_delete = ['Phần tự luận',
                            'HẾT', 'Loigiaihay.com', "Phần trắc nghiệm", 
                            "Phần II: Tự luận", "Phần I: Trắc nghiệm",
                            "Phần II: Phần tự luận", "Phần II: Phần tự luận (6 điểm)"
                        ]
        for s in string_to_delete:
            item['reasoning'] = item['reasoning'].replace(s, '')
            item['question'] = item['question'].replace(s, '')
            item['answer'] = item['answer'].replace(s, '')
        if item['reasoning'].find(item['question']) != -1:
            item['reasoning'] = item['reasoning'].replace(item['question'], '')
        regex_pattern = r"Câu\s+(\d+)(\s*)[:.]\s*"
        if re.match(regex_pattern, item['question']):
            item['question'] = re.sub(regex_pattern, '', item['question'], count=1).strip()
        regex_pattern1 = r"Loigiaihay.com\s*"
        item['reasoning'] = re.sub(regex_pattern1, '', item['reasoning']).strip()
        item['reasoning'] = item['reasoning'].strip()
        item['answer'] = item['answer'].strip()
        return item