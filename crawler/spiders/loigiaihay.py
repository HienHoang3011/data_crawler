import scrapy
from ..items import StemItem
import re
from bs4 import BeautifulSoup
import unicodedata
from ..utils.get_collections import *

collection_link = (create_collection_link_chemical_10() + create_collection_link_chemical_11() + create_collection_link_chemical_12() +
                   create_collection_link_math_6() + create_collection_link_math_10() + create_collection_link_math_11() + create_collection_link_math_12() +
                   create_collection_link_physics_10() + create_collection_link_physics_11() + create_collection_link_physics_12())
class LoigiaihaySpider(scrapy.Spider):
    name = "loigiaihay"
    start_urls = collection_link
    IMAGE_MARK = "[[HAS_IMAGE]]"
    custom_settings = {
        "ITEM_PIPELINES": {
         "crawler.pipelines.StemPipeline": 300,
        }
    }
    
    def detect_grade_from_url(self, url):
        """Tự động phát hiện lớp từ URL"""
        # Ưu tiên các pattern cụ thể trước
        patterns = [
            r'lop-(\d{1,2})\b',           # lop-11, lop-12
            r'toan-(\d{1,2})\b',          # toan-11, toan-6
            r'vat-l[iy]-(\d{1,2})\b',     # vat-ly-11, vat-li-12
            r'hoa-hoc-(\d{1,2})\b',       # hoa-hoc-11
            r'hinh-hoc-(\d{1,2})\b',      # hinh-hoc-11
            r'-(\d{1,2})-',               # fallback: bất kỳ số nào giữa dấu gạch ngang
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, url)
            if matches:
                # Ưu tiên lớp 10, 11, 12, sau đó 6-9
                for grade in ('12', '11', '10', '9', '8', '7', '6'):
                    if grade in matches:
                        return grade
                return matches[0]
        
        return "12"  # default
    
    def detect_subject_from_url(self, url):
        """Tự động phát hiện môn học từ URL"""
        subject_patterns = {
            'math': [r'toan', r'dai-so', r'giai-tich', r'hinh-hoc'],
            'physics': [r'vat-l[iy]', r'ly-thuyet'],
            'chemistry': [r'hoa-hoc', r'hoa-hoc']
        }
        
        url_lower = url.lower()
        
        for subject, patterns in subject_patterns.items():
            for pattern in patterns:
                if re.search(pattern, url_lower):
                    return subject
        
        return "math"  # default
    
    def parse(self, response):
        soup = BeautifulSoup(response.text, "html.parser")
        div = soup.find("div", id="box-content")
        
        if not div:
            div = soup.find("div", class_="content_box")
        if not div:
            div = soup.find("div", class_="box")
        # Thay thế tất cả thẻ img bằng image mark
        for img in div.find_all("img"):
            img.replace_with(self.IMAGE_MARK)
        
        for tag in div(["table"]):
            tag.decompose()
        text = div.get_text("\n")
        text_final = text
        
        # Tự động phát hiện lớp và môn học từ URL
        grade = self.detect_grade_from_url(response.url)
        subject = self.detect_subject_from_url(response.url)
        
        items = {}              # cau_num -> StemItem
        mode = {}               # cau_num -> "question" | "reasoning"
        current_cau = None

        for p in text_final.splitlines():
            text = p.strip()
            text = text.replace('\xa0', ' ')
            m = re.search(r"Câu\s+(\d+)", text)
            if m:
                cau = int(m.group(1))

                # lần đầu → question
                if cau not in items:
                    item = StemItem()
                    # Sử dụng subject và grade đã detect tự động
                    item["subject"] = subject
                    item["grade"] = grade
                    item["question"] = text
                    item["reasoning"] = ""
                    item["answer"] = ""

                    items[cau] = item
                    mode[cau] = "question"
                else:
                    # extract inline answer if the 'Câu N' paragraph also includes the answer like 'Câu 19: (A)'
                    ans = self.extract_inline_answer(text)
                    if ans:
                        items[cau]["answer"] = ans

                    # if there's any additional content after 'Câu <n>' (e.g. 'Câu 4: (B) explanation'),
                    # keep that remainder in the reasoning bucket so it's not lost.
                    try:
                        rest = re.sub(rf'^.*?Câu\s*{cau}\s*[:\)\.\-\s]*', '', text, flags=re.IGNORECASE)
                    except re.error:
                        rest = ''
                    if rest.strip():
                        items[cau]["reasoning"] += "\n" + rest.strip()

                    mode[cau] = "reasoning"

                current_cau = cau
                continue

            # ===== CHƯA CÓ CÂU =====
            if current_cau is None:
                continue

            # ===== APPEND NỘI DUNG =====
            target = items[current_cau][mode[current_cau]]
            target += "\n" + text
            items[current_cau][mode[current_cau]] = target

        # ===== FINALIZE =====
        for item in items.values():
            if not item["answer"]:
                item["answer"] = self.extract_answer_1(item["reasoning"])
            if not item["answer"]:
                item["answer"] = self.extract_answer_2(item["question"])
            yield item


    def extract_answer_1(self, text):
        if not text:
            return ''

        # try direct common patterns first (with Vietnamese accents)
        patterns = [r'Chọn\s*(?:đáp án\s*)?[:\s]*([A-D])\b',
                    r'Chọn[:\s]*([A-D])\b',
                    r'Đáp án[:\s]*([A-D])\b',
                    r'Chon\s*(?:dap an\s*)?[:\s]*([A-D])\b']
        for p in patterns:
            m = re.search(p, text, re.IGNORECASE)
            if m:
                return m.group(1).upper()

        # normalize (remove diacritics) to match variants like 'Chon dap an A' etc.
        nf = unicodedata.normalize('NFD', text)
        plain = ''.join(c for c in nf if unicodedata.category(c) != 'Mn')
        plain_low = plain.lower()

        # try normalized patterns
        norm_patterns = [r'chon\s*(?:dap an\s*)?[:\s]*([a-d])\b',
                         r'dap an[:\s]*([a-d])\b']
        for p in norm_patterns:
            m = re.search(p, plain_low)
            if m:
                return m.group(1).upper()

        return ''
    def extract_answer_2(self, text):
        if not text:
            return ''

        # normalize unicode
        nf = unicodedata.normalize('NFD', text)
        plain = ''.join(c for c in nf if unicodedata.category(c) != 'Mn')
        plain_low = plain.lower()

        # FIXED regex: allow optional parentheses
        m = re.search(
            r'cau\s*\d+\s*[:\)\.\-\s]*\(?\s*([a-d])\s*\)?',
            plain_low
        )
        if m:
            return m.group(1).upper()

        # fallback
        m = re.search(r'dap an[:\s]*([a-d])\b', plain_low)
        if m:
            return m.group(1).upper()

        return ''

    def extract_inline_answer(self, text):
          return self.extract_answer_2(text)