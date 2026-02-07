import scrapy
from ..items import StemItem
import re
from bs4 import BeautifulSoup
import unicodedata


def create_collection_link_math_10():
    collection_math_10 = [
        "https://loigiaihay.com/de-khao-sat-chat-luong-dau-nam-lop-10-mon-toan-de-so-2-a113801.html",
        "https://loigiaihay.com/de-khao-sat-chat-luong-dau-nam-lop-10-mon-toan-de-so-4-a113803.html"
    ]
    link_math_10_gk1 = [
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-ket-noi-tri-thuc-de-so-1-a121902.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-ket-noi-tri-thuc-de-so-2-a122128.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-ket-noi-tri-thuc-de-so-3-a122129.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-ket-noi-tri-thuc-de-so-4-a122130.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-de-so-6-a152176.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-ket-noi-tri-thuc-de-so-6-a152177.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-ket-noi-tri-thuc-de-so-7-a152188.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-ket-noi-tri-thuc-de-so-8-a152197.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-ket-noi-tri-thuc-de-so-9-a152203.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-ket-noi-tri-thuc-de-so-10-a152210.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-ket-noi-tri-thuc-de-so-11-a176248.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-ket-noi-tri-thuc-de-so-12-a176249.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-ket-noi-tri-thuc-de-so-13-a176250.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-de-so-14-a188967.html",
        "https://loigiaihay.com/de-thi-giua-ki-1-toan-10-de-so-15-a188972.html"
    ]
    link_math_10_gk1 += [
        "https://loigiaihay.com/de-thi-hoc-ki-1-toan-10-ket-noi-tri-thuc-de-so-1-a124204.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-toan-10-ket-noi-tri-thuc-de-so-2-a124237.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-toan-10-ket-noi-tri-thuc-de-so-3-a124238.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-toan-10-ket-noi-tri-thuc-de-so-4-a124240.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-toan-10-ket-noi-tri-thuc-de-so-5-a124393.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-toan-10-ket-noi-tri-thuc-de-so-6-a124394.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-toan-10-ket-noi-tri-thuc-de-so-6-a124395.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-toan-10-ket-noi-tri-thuc-de-so-9-a124425.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-toan-10-ket-noi-tri-thuc-de-so-9-a124426.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-toan-10-ket-noi-tri-thuc-de-so-11-a178718.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-toan-10-ket-noi-tri-thuc-de-so-11-a178719.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-toan-10-ket-noi-tri-thuc-de-so-11-a178720.html",
        "https://loigiaihay.com/de-thi-hoc-ki-1-toan-10-ket-noi-tri-thuc-de-so-15-a189469.html"
    ]
    link_math_10_gk2 = [
        "https://loigiaihay.com/de-thi-giua-ki-2-toan-10-ket-noi-tri-thuc-de-so-1-a156395.html",
        "https://loigiaihay.com/de-thi-giua-ki-2-toan-10-ket-noi-tri-thuc-de-so-2-a156399.html",
        "https://loigiaihay.com/de-thi-giua-ki-2-toan-10-ket-noi-tri-thuc-de-so-3-a156400.html",
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-2-toan-10-de-so-1-ket-noi-tri-thuc-a134980.html",
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-2-toan-10-de-so-ket-noi-tri-thuc-a135043.html",
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-2-toan-10-de-so-3-ket-noi-tri-thuc-a135044.html",
        "https://loigiaihay.com/de-kiem-tra-hoc-ki-2-toan-10-de-so-4-ket-noi-tri-thuc-a135046.html",
        
    ]
    collection_math_10 += link_math_10_gk1
    collection_math_10 += link_math_10_gk2
    return collection_math_10

def is_multiple_choice_question(text):
    if not text or not isinstance(text, str):
        return False

    lines = text.strip().splitlines()

    # Pattern cho phương án A., A), (A), A
    choice_pattern = r'^\s*(\(?[A-Da-d]\)|[A-Da-d][\.\)])\s+.+'

    choice_count = 0

    for line in lines:
        if re.match(choice_pattern, line.strip()):
            choice_count += 1

    return choice_count >= 2

class StemLoigiaihaySpider(scrapy.Spider):
    name = "stem_loigiaihay"
    start_urls = create_collection_link_math_10()
    IMAGE_MARK = "[[HAS_IMAGE]]"
    custom_settings = {
        "ITEM_PIPELINES": {
         "crawler.pipelines.StemPipeline": 300,
        }
    }
    def parse(self, response):
        soup = BeautifulSoup(response.text, "html.parser")
        div = soup.find("div", id="box-content")
        
        # Thay thế tất cả thẻ img bằng image mark
        for img in div.find_all("img"):
            img.replace_with(self.IMAGE_MARK)
        
        for tag in div(["table"]):
            tag.decompose()
        text = div.get_text("\n")
        
        # Loại bỏ phần tự luận nếu tìm thấy
        idx1 = text.lower().find("tự luận")
        idx2 = text.lower().find("lời giải")
        if idx1 != -1 and idx2 != -1 and idx1 < idx2:
            substring1 = text[idx1:idx2]
            text = text.replace(substring1, "")
        
        idx3 = text.find("Phần tự luận")
        idx4 = text.find("HẾT")
        if idx4 == -1:
            idx4 = len(text)
        if idx3 != -1 and idx4 != -1 and idx3 < idx4:
            substring2 = text[idx3:idx4]
            text = text.replace(substring2, "")
        
        text_final = text
        self.logger.info(f"Text length after cleanup: {len(text_final)}")
        self.logger.info(f"First 500 chars: {text_final[:500]}")
        
        grade = None
        matches = re.findall(r'-(\d{1,2})', response.url)
        if matches:
            for prefer in ('12', '11', '10'):
                if prefer in matches:
                    grade = prefer
                    break
        else:
            grade = matches[0]
        
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
                    item["subject"] = "math"
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