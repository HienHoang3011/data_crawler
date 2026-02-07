import scrapy
from ..items import StemItem
import re
from bs4 import BeautifulSoup
import unicodedata
from ..utils.get_collections import *

class ChemicalLoigiaihaySpider(scrapy.Spider):
    name = "chemical_loigiaihay"
    start_urls = create_collection_chemical_10()
    IMAGE_MARK = "[[HAS_IMAGE]]"
    custom_settings = {
        "ITEM_PIPELINES": {
         "crawler.pipelines.StemPipeline": 300,
        }
    }
    def parse(self, response):
        soup = BeautifulSoup(response.text, "html.parser")
        div = soup.find("div", id="box-content")
        if not div:
            div = soup.find("div", class_="box")
        if not div:
            div = soup.find("div", class_="content_box")
        # Thay thế tất cả thẻ img bằng image mark
        for img in div.find_all("img"):
            img.replace_with(self.IMAGE_MARK)
        
        for tag in div(["table"]):
            tag.decompose()
        text = div.get_text("\n")
        text_final = text
        
        grade = "10"
        # matches = re.findall(r'-(\d{1,2})', response.url)
        # if matches:
        #     for prefer in ('12', '11', '10'):
        #         if prefer in matches:
        #             grade = prefer
        #             break
        # else:
        #     grade = matches[0]
        
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
                    # minimal fields to populate for easier downstream use
                    item["subject"] = "chemical"
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