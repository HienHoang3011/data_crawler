import scrapy
from bs4 import BeautifulSoup
from ..items import PtitItem

url_collection_nganh = {
    "CNTT-Việt-Nhật": "https://daotao.ptit.edu.vn/chuong-trinh-dao-tao/chuong-trinh-cong-nghe-thong-tin-viet-nhat/",
    "Trí tuệ nhân tạo": "https://daotao.ptit.edu.vn/chuong-trinh-dao-tao/chuong-trinh-tri-tue-nhan-tao/",
    "Phát triển Game": "https://daotao.ptit.edu.vn/chuong-trinh-dao-tao/chuong-trinh-thiet-ke-va-phat-trien-game/",
    "Quan hệ công chúng": "https://daotao.ptit.edu.vn/chuong-trinh-dao-tao/chuong-trinh-quan-he-cong-chung-nganh-marketing/",
    "IoT": "https://daotao.ptit.edu.vn/chuong-trinh-dao-tao/nganh-cong-nghe-internet-van-vat-iot/",
    "Kế toán ACCA": "https://daotao.ptit.edu.vn/chuong-trinh-dao-tao/nganh-ke-toan-chat-luong-cao-chuan-quoc-te-acca/",
    "Marketing CLC": "https://daotao.ptit.edu.vn/chuong-trinh-dao-tao/nganh-marketing-he-clc/",
    "Kỹ thuật dữ liệu": "https://daotao.ptit.edu.vn/chuong-trinh-dao-tao/chuong-trinh-ky-thuat-du-lieu-nganh-mang-may-tinh-va-truyen-thong-du-lieu/",
    "Fintech": "https://daotao.ptit.edu.vn/chuong-trinh-dao-tao/nganh-cong-nghe-tai-chinh-fintech/",
    "Báo chí": "https://daotao.ptit.edu.vn/chuong-trinh-dao-tao/nganh-bao-chi-journalism/",
    "Kế toán": "https://daotao.ptit.edu.vn/chuong-trinh-dao-tao/nganh-ke-toan-2022/",
    "Điều khiển và Tự động hóa": "https://daotao.ptit.edu.vn/chuong-trinh-dao-tao/nganh-ky-thuat-dieu-khien-va-tu-dong-hoa/",
    "CNTT CLC": "https://daotao.ptit.edu.vn/chuong-trinh-dao-tao/nganh-cong-nghe-thong-tin-he-clc/",
    "Quản trị kinh doanh": "https://daotao.ptit.edu.vn/chuong-trinh-dao-tao/nganh-quan-tri-kinh-doanh/",
    "Thương mại điện tử": "https://daotao.ptit.edu.vn/chuong-trinh-dao-tao/nganh-thuong-mai-dien-tu/",
    "Marketing": "https://daotao.ptit.edu.vn/chuong-trinh-dao-tao/nganh-marketing/",
    "Truyền thông đa phương tiện": "https://daotao.ptit.edu.vn/chuong-trinh-dao-tao/nganh-truyen-thong-da-phuong-tien/",
    "Công nghệ đa phương tiện": "https://daotao.ptit.edu.vn/chuong-trinh-dao-tao/nganh-cong-nghe-da-phuong-tien/",
    "Điện - Điện tử": "https://daotao.ptit.edu.vn/chuong-trinh-dao-tao/nganh-cong-nghe-ky-thuat-dien-dien-tu/",
    "Điện tử viễn thông": "https://daotao.ptit.edu.vn/chuong-trinh-dao-tao/nganh-ky-thuat-dien-tu-vien-thong/",
    "An toàn thông tin": "https://daotao.ptit.edu.vn/chuong-trinh-dao-tao/nganh-an-toan-thong-tin/",
    "Công nghệ thông tin": "https://daotao.ptit.edu.vn/chuong-trinh-dao-tao/nganh-cong-nghe-thong-tin/",
    "Khoa học máy tính": "https://daotao.ptit.edu.vn/chuong-trinh-dao-tao/nganh-khoa-hoc-may-tinh/"
}

url_collection_news =[
    "https://ptit.edu.vn/tin-tuc/hoc-vien-cong-nghe-buu-chinh-vien-thong-bo-sung-chinh-sach-hoc-bong-tai-nang-2025-them-co-hoi-cho-cac-thi-sinh-dat-ket-qua-cao-ky-thi-thpt",
    "https://ptit.edu.vn/tin-tuc/thong-bao-ve-viec-sua-doi-bo-sung-mot-so-noi-dung-cua-de-an-tuyen-sinh-va-thong-bao-tuyen-sinh-dai-hoc-he-chinh-quy-nam-2025",
    "https://ptit.edu.vn/tin-tuc/gs-ts-vu-minh-khuong-truyen-cam-hung-cho-cac-nha-khoa-hoc-tre-ptit",
    "https://ptit.edu.vn/tin-tuc/gs-ts-vu-minh-khuong-giu-chuc-chu-tich-hoi-dong-co-van-vien-lanh-dao-quan-tri-va-quan-ly-viet-nam-tai-ptit",
    "https://ptit.edu.vn/uncategorized/thu-truong-bo-khoa-hoc-va-cong-nghe-hoang-minh-lam-viec-voi-hoc-vien-cong-nghe-buu-chinh-vien-thong-2",
    "https://ptit.edu.vn/uncategorized/ptit-ky-thoa-thuan-hop-tac-voi-cong-ty-tnhh-mot-thanh-vien-tai-nguyen-va-moi-truong-viet-nam",
    "https://ptit.edu.vn/tin-tuc/ptit-tham-gia-lien-minh-ai-au-lac",
    "https://ptit.edu.vn/tin-tuc/36704",
    "https://ptit.edu.vn/tin-tuc/ptit-va-msm-hop-tac-trong-linh-vuc-cong-nghe-cao",
    "https://ptit.edu.vn/tin-tuc/sinh-vien-ptit-dat-giai-nhat-quoc-gia-vao-cuoc-thi-vo-dich-tin-hoc-van-phong-the-gioi-mos-world-championship-2025",
    "https://ptit.edu.vn/tin-tuc/hoc-vien-cong-nghe-buu-chinh-vien-thong-hop-tac-voi-hoc-vien-y-duoc-hoc-co-truyen-viet-nam-trong-hoat-dong-chuyen-doi-so",
    "https://ptit.edu.vn/tin-tuc/doan-cong-tac-binh-chung-thong-tin-lien-lac-tham-va-lam-viec-tai-hoc-vien-cong-nghe-buu-chinh-vien-thong",
    "https://ptit.edu.vn/tin-tuc/ptit-la-1-trong-4-co-so-giao-duc-dai-hoc-tham-gia-xay-dung-de-an-quoc-gia-ve-tri-tue-nhan-tao",
    "https://ptit.edu.vn/tin-tuc/hoc-vien-cong-nghe-buu-chinh-vien-thong-hop-luc-nha-nuoc-nha-truong-doanh-nghiep-de-dao-tao-xuat-sac",
    "https://ptit.edu.vn/tin-tuc/ptit-duoc-lua-chon-la-1-trong-13-truong-dai-hoc-dan-dat-trung-tam-dao-tao-xuat-sac-va-tai-nang",
    "https://ptit.edu.vn/tin-tuc/hoc-vien-cong-nghe-buu-chinh-vien-thong-tiep-doan-cong-tac-cua-bao-dien-tu-vtc-news",
    "https://ptit.edu.vn/tin-tuc/doan-cong-tac-so-khoa-hoc-va-cong-nghe-tinh-cao-bang-tham-va-lam-viec-tai-hoc-vien-cong-nghe-buu-chinh-vien-thong",
    "https://ptit.edu.vn/tin-tuc/dai-hoi-dang-bo-hoc-vien-cong-nghe-buu-chinh-vien-thong-lan-thu-vii-nhiem-ky-2025-2030",
    "https://ptit.edu.vn/tin-tuc/hoc-vien-cong-nghe-buu-chinh-vien-thong-ket-noi-hop-tac-voi-vien-ho-tro-khoi-nghiep-kaist-han-quoc-trong-viec-ho-tro-cac-hoat-dong-khoi-nghiep-doi-moi-sang-tao",
    "https://ptit.edu.vn/tin-tuc/toa-dam-cong-nghe-chien-luoc-uc-viet-tai-ptit-cac-cong-nghe-ket-noi-cho-tuong-lai",
    "https://ptit.edu.vn/tin-tuc/hoi-nghi-cong-bo-quyet-dinh-ve-cong-tac-can-bo",
    "https://ptit.edu.vn/tin-tuc/ptit-va-dai-hoc-cong-nghe-sydney-uts-se-thuc-day-hop-tac-manh-me-hon-nua",
    "https://ptit.edu.vn/tin-tuc/ra-mat-trung-tam-cong-nghe-chien-luoc-uc-viet-va-cong-bo-tai-tro-8-du-an-hat-giong",
    "https://ptit.edu.vn/tin-tuc/dai-hoi-dang-bo-hoc-vien-cong-nghe-buu-chinh-vien-thong-nhiem-ky-2025-2030-dau-moc-chinh-tri-quan-trong-khang-dinh-vai-tro-tien-phong-trong-doi-moi-sang-tao-va-chuyen-doi-so",
    "https://ptit.edu.vn/tin-tuc/bai-viet-cua-tong-bi-thu-to-lam-to-chuc-tot-dai-hoi-dang-bo-cac-cap-nhiem-ky-2025-2030",
    "https://ptit.edu.vn/tin-tuc/le-ky-ket-thoa-thuan-hop-tac-giua-hoc-vien-cong-nghe-buu-chinh-vien-thong-va-ubnd-tinh-lai-chau",
    "https://ptit.edu.vn/tin-tuc/hoi-thao-khoa-hoc-quoc-gia-khoa-hoc-tu-nhien-va-ung-dung-trong-thoi-dai-so-nsa-2025",
    "https://ptit.edu.vn/tin-tuc/thong-bao-mo-he-thong-dang-ky-thong-tin-xet-tuyen-truc-tuyen-cho-thi-sinh-dang-ky-xet-tuyen-vao-dai-hoc-chinh-quy-nam-2025",
    "https://ptit.edu.vn/tin-tuc/day-manh-cong-tac-phat-hien-boi-duong-tai-nang-tre-tai-hoc-vien-cong-nghe-buu-chinh-vien-thong",
    "https://ptit.edu.vn/tin-tuc/bo-truong-nguyen-manh-hung-trao-30-suat-hoc-bong-lanh-dao-tre-trong-ky-nguyen-so-cho-sinh-vien-tai-nang-ptit",
    "https://ptit.edu.vn/tin-tuc/hoc-vien-cong-nghe-buu-chinh-vien-thong-se-tuyen-sinh-80-sinh-vien-cho-chuong-trinh-dao-tao-tri-tue-nhan-tao-van-vat",
    "https://ptit.edu.vn/tin-tuc/thong-bao-ve-viec-xet-tuyen-thang-va-uu-tien-xet-tuyen-vao-dai-hoc-he-chinh-quy-nam-2025",
    "https://ptit.edu.vn/uncategorized/hoc-vien-cong-nghe-buu-chinh-vien-thong-va-dai-hoc-chubu-nhat-ban-trao-thoa-thuan-hop-tac-mou-duoi-su-chung-kien-cua-pho-thu-tuong-nguyen-chi-dung",
    "https://ptit.edu.vn/tin-tuc/bo-truong-nguyen-manh-hung-dai-hoc-ve-lau-dai-phai-la-dai-hoc-nghien-cuu",
    "https://ptit.edu.vn/tin-tuc/sinh-vien-nam-thu-3-nganh-cong-nghe-thong-tin-cua-ptit-se-duoc-dai-hoc-cong-nghe-queensland-tiep-nhan-hoc-chuyen-tiep-va-cap-bang",
    "https://ptit.edu.vn/tin-tuc/khai-mac-cuoc-thi-ptit-cau-hackathon-2025",
    "https://ptit.edu.vn/tin-tuc/lanh-dao-ptit-tham-du-chuong-trinh-gap-go-huu-nghi-nhan-dan-viet-nam-trung-quoc",
    "https://ptit.edu.vn/tin-tuc/ptit-hop-tac-voi-cong-ty-rapid-space-cong-hoa-phap-ve-nghien-cuu-phat-trien-san-pham-trong-linh-vuc-5g"
    
]
class PtitCrawlerSpider(scrapy.Spider):
    name = "ptit_crawler"
    start_urls = list(url_collection_nganh.values())

    custom_settings = {
        "ITEM_PIPELINES": {
            "crawler.pipelines.PtitPipeline": 300,
        }
    }

    def parse(self, response):
        soup = BeautifulSoup(response.text, "html.parser")

        div = soup.find("div", class_="ova_dir_content")
        if not div:
            return

        for tag in div(["script", "style", "aside", "nav"]):
            tag.decompose()

        content = div.get_text("\n", strip=True)
        key = next(
            k for k, v in url_collection_nganh.items()
            if v == response.url
        )

        item = PtitItem()
        item["text"] = content
        item["key"] = key

        yield item

class PtitNewsCrawlerSpider(scrapy.Spider):
    name = "ptit_news_crawler"
    start_urls = list(url_collection_news)

    custom_settings = {
        "ITEM_PIPELINES": {
            "crawler.pipelines.PtitPipeline": 300,
        }
    }

    def parse(self, response):
        soup = BeautifulSoup(response.text, "html.parser")

        div = soup.find("div", class_="ova_dir_content")
        if not div:
            return

        for tag in div(["script", "style", "aside", "nav", "img"]):
            tag.decompose()

        content = div.find("div", class_="post-content").get_text("\n", strip=True)
        key = soup.find("h1", class_="post-title").get_text(strip=True)

        item = PtitItem()
        item["text"] = content
        item["key"] = key

        yield item