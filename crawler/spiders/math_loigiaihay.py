import scrapy
from bs4 import BeautifulSoup
import re
import unicodedata
from ..items import ExamMathItem

def gen_links_1(chuong, start_id, so_de, lop, mon):
    return [
        f"https://loigiaihay.com/de-kiem-tra-15-phut-chuong-{chuong}-de-so-{i}-dai-so-va-giai-tich-{lop}-c46a{start_id + i - 1}.html"
        for i in range(1, so_de + 1)
    ]
    
def create_collection_link_math():
    collection_math = []
    link_chuong_1_11_15p = gen_links_1(chuong=1, start_id=45788, so_de=10, lop=11, mon='math')
    link_chuong_2_11_15p = gen_links_1(chuong=2, start_id=45832, so_de=9, lop=11, mon='math')
    link_chuong_3_11_15p = gen_links_1(chuong=3, start_id=50032, so_de=3, lop=11, mon='math')
    link_chuong_4_11_15p = gen_links_1(chuong=4, start_id=46489, so_de=8, lop=11, mon='math')
    link_chuong_5_11_15p = gen_links_1(chuong=5, start_id=46507, so_de=5, lop=11, mon='math')
    link_chuong_1_11_45p = gen_links_1(chuong=1, start_id=45827, so_de=5, lop=11, mon='math')
    link_chuong_2_11_45p = gen_links_1(chuong=2, start_id=45852, so_de=5, lop=11, mon='math')
    link_chuong_3_11_45p = gen_links_1(chuong=3, start_id=50035, so_de=2, lop=11, mon='math')
    link_chuong_4_11_45p = gen_links_1(chuong=4, start_id=46497, so_de=4, lop=11, mon='math')
    link_chuong_5_11_45p = gen_links_1(chuong=5, start_id=46687, so_de=5, lop=11, mon='math')
    link_math_11 = link_chuong_1_11_15p + link_chuong_2_11_15p + link_chuong_3_11_15p + link_chuong_4_11_15p + link_chuong_5_11_15p
    link_math_11 += link_chuong_1_11_45p + link_chuong_2_11_45p + link_chuong_3_11_45p + link_chuong_4_11_45p + link_chuong_5_11_45p
    collection_math.extend(link_math_11)
    link_chuong_1_12_15p = gen_links_1(chuong=1, start_id=44772, so_de=5, lop=12, mon='math')
    link_chuong_2_12_15p = gen_links_1(chuong=2, start_id=44791, so_de=5, lop=12, mon='math')
    link_chuong_3_12_15p = gen_links_1(chuong=3, start_id=47413, so_de=5, lop=12, mon='math')
    link_chuong_4_12_15p = gen_links_1(chuong=4, start_id=47424, so_de=5, lop=12, mon='math')
    link_chuong_1_12_45p = gen_links_1(chuong=1, start_id=44796, so_de=5, lop=12, mon='math')
    link_chuong_2_12_45p = gen_links_1(chuong=2, start_id=44808, so_de=4, lop=12, mon='math')
    link_chuong_3_12_45p = gen_links_1(chuong=3, start_id=47429, so_de=5, lop=12, mon='math')
    link_chuong_4_12_45p = gen_links_1(chuong=4, start_id=47438, so_de=5, lop=12, mon='math')
    link_math_12 = link_chuong_1_12_15p + link_chuong_2_12_15p + link_chuong_3_12_15p + link_chuong_4_12_15p
    link_math_12 += link_chuong_1_12_45p + link_chuong_2_12_45p + link_chuong_3_12_45p + link_chuong_4_12_45p
    collection_math.extend(link_math_12)
    return collection_math

class LoiGiaiHayMathSpider(scrapy.Spider):
    name = "math_loigiaihay"
    start_urls = create_collection_link_math()
    IMAGE_MARK = "[[HAS_IMAGE]]"

    def parse(self, response):
        soup = BeautifulSoup(response.text, "html.parser")

        # bỏ bảng đáp án
        for t in soup.find_all("table"):
            t.decompose()

        box = soup.find("div", id="box-content")
        if not box:
            return

        paragraphs = box.find_all("p")

        items = {}              # cau_num -> ExamMathItem
        mode = {}               # cau_num -> "question" | "reasoning"
        current_cau = None

        for p in paragraphs:
            text = p.get_text(strip=True)
            has_img = p.find("img") is not None
            m = re.search(r"Câu\s+(\d+)", text)

            # ===== GẶP CÂU =====
            if m:
                cau = int(m.group(1))

                # lần đầu → question
                if cau not in items:
                    item = ExamMathItem()
                    item["question"] = text
                    item["reasoning"] = ""
                    item["answer"] = ""

                    items[cau] = item
                    mode[cau] = "question"
                else:
                    # lần 2 → reasoning
                    mode[cau] = "reasoning"

                current_cau = cau
                continue

            # ===== CHƯA CÓ CÂU =====
            if current_cau is None:
                continue

            # ===== APPEND NỘI DUNG =====
            target = items[current_cau][mode[current_cau]]

            if has_img:
                target += "\n" + self.IMAGE_MARK

            target += "\n" + text
            items[current_cau][mode[current_cau]] = target

        # ===== FINALIZE =====
        for item in items.values():
            item["answer"] = self.extract_answer_1(item["reasoning"])
            if item["answer"] == "":
                item['answer'] = self.extract_answer_2(item["question"])
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
        import re
        import unicodedata

        if not text:
            return ''

        # try explicit 'Đáp án' pattern first (with accents)
        m = re.search(r'Đáp án[:\s]*([A-D])\b', text, re.IGNORECASE)
        if m:
            return m.group(1).upper()

        # normalize (remove diacritics) to match variants like 'câu 1:C' or 'cau 1: C'
        nf = unicodedata.normalize('NFD', text)
        plain = ''.join(c for c in nf if unicodedata.category(c) != 'Mn')
        plain_low = plain.lower()

        # match patterns like 'cau 1:C', 'cau1: c', 'cau 1 ) C' etc.
        m = re.search(r'cau\s*\d+\s*[:\)\.\-\s]*([a-d])\b', plain_low)
        if m:
            return m.group(1).upper()

        # fallback: simple 'dap an' without accents (already normalized)
        m = re.search(r'dap an[:\s]*([a-d])\b', plain_low)
        if m:
            return m.group(1).upper()

        return ''