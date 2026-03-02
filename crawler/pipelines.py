
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import re
from pathlib import Path

def clean_item(item: dict) -> dict:
    string_to_remove = r'(\d+ điểm)'
    for key, value in item.items():
        if isinstance(value, str):
            item[key] = re.sub(string_to_remove, '', value)
    string_pattern = ["\n+"]
    for pattern in string_pattern:
        for key, value in item.items():
            item[key] = re.sub(pattern, "\n", value)
            item[key] = re.sub("^\(\d+,\)", "", item[key])
            item[key] = re.sub("^\n+", "", item[key])
            item[key] = re.sub("\s{3,}", "\n", item[key])
            item[key] = re.sub("^(\n)", "", item[key])
            item[key] = re.sub("^(\n)\n", "", item[key])
            item[key] = re.sub("^()", "", item[key])
            item[key] = re.sub("^.\n", "", item[key])
            item[key] = re.sub("^\n", "", item[key])
            item[key] = re.sub("([A-D])\s*\n\s*(\.)", r"\1\2", item[key])
            text = re.sub(r'([A-D]\.)\n', r'\1', item[key])
            item[key] = text
    string_to_remove = ["--Hết--", "--Hết--", "--HẾT--", "--HẾT--", "-------- Hết --------", "Chi tiết:", "Chi tiết", "I. Trắc nghiệm", "Phần tự luận", "Phần trắc nghiệm", "Lời giải chi tiết", "Phương pháp giải:", "Đáp án chi tiết:"]
    for string in string_to_remove:
        item['reasoning'] = item['reasoning'].replace(string, "")  
    
    reasoning = item['reasoning']
    
    # Xóa các pattern dư thừa trước
    reasoning = re.sub(r'\s*:\s*\n\s*:\s*', '\n', reasoning)  # Xóa " :\n :\n"
    reasoning = re.sub(r'^\s*\n+', '', reasoning)  # Xóa \n đầu
    
    # 1. Xử lý pattern ":\nĐáp án X." hoặc ":\nĐáp án X" ở cuối
    pattern1 = r'(.+):\n(Đáp án|đáp án) ([A-D])\.?\s*$'
    match1 = re.match(pattern1, reasoning, re.DOTALL)
    if match1:
        content = match1.group(1).strip()
        answer_prefix = match1.group(2)
        answer_letter = match1.group(3)
        reasoning = f"{content}\n{answer_prefix} {answer_letter}"
    
    # 2. Xử lý pattern "Đáp án X vì..." - chuyển xuống cuối nếu không có "Sai" đầu câu
    pattern2 = r'\n(Đáp án|đáp án) ([A-D]) vì (.+)$'
    match2 = re.search(pattern2, reasoning, re.DOTALL)
    if match2 and not reasoning.strip().startswith('Sai'):
        before_answer = reasoning[:match2.start()].strip()
        answer_prefix = match2.group(1)
        answer_letter = match2.group(2)
        explanation = match2.group(3).strip()
        reasoning = f"{before_answer}\n{explanation}\n{answer_prefix} {answer_letter}"
    
    # 3. Xử lý pattern "Đáp án\nX" (xuống dòng giữa)
    pattern3 = r'(.+)\n(Đáp án|đáp án)\n([A-D])\s*$'
    match3 = re.match(pattern3, reasoning, re.DOTALL)
    if match3 and not reasoning.strip().startswith('Sai'):
        content = match3.group(1).strip()
        answer_prefix = match3.group(2)
        answer_letter = match3.group(3)
        reasoning = f"{content}\n{answer_prefix} {answer_letter}"
    
    # 4. Xử lý pattern "Đáp án X\n..." ở đầu - chuyển xuống cuối, không đảo nếu có "Sai" 
    pattern4 = r'^(Đáp án|đáp án) ([A-D])\n(?!Sai)(.+)$'
    match4 = re.match(pattern4, reasoning, re.DOTALL)
    if match4:
        answer_prefix = match4.group(1)
        answer_letter = match4.group(2)
        content = match4.group(3).strip()
        reasoning = f"{content}\n{answer_prefix} {answer_letter}"
    
    # 5. Xử lý pattern "Đáp án : X" (có dấu cách trước dấu hai chấm)
    pattern5 = r'\n(Đáp án|đáp án)\s*:\s*([A-D])\s*$'
    match5 = re.search(pattern5, reasoning, re.DOTALL)
    if match5:
        before_answer = reasoning[:match5.start()].strip()
        answer_prefix = match5.group(1)
        answer_letter = match5.group(2)
        reasoning = f"{before_answer}\n{answer_prefix} {answer_letter}"
    
    # 6. Xóa các \n liên tiếp thành 1 \n sau khi xử lý xong tất cả
    reasoning = re.sub(r'\n{2,}', '\n', reasoning)
    reasoning = reasoning.strip()
    
    item['reasoning'] = reasoning
    if item["reasoning"].find(item['question']) != -1:
        item['reasoning'] = item['reasoning'].replace(item['question'], "")
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
        line_pattern = '\n+'
        item['reasoning'] = re.sub(line_pattern, '\n', item['reasoning'])
        item['question'] = re.sub(line_pattern, '\n', item['question'])
        item['answer'] = re.sub(line_pattern, '\n', item['answer'])
        item['reasoning'] = re.sub(regex_pattern1, '', item['reasoning']).strip()
        item['reasoning'] = item['reasoning'].strip()
        item['answer'] = item['answer'].strip()
        
        # Apply advanced cleaning
        item = clean_item(item)
        
        return item