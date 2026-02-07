# Educational Data Crawler

Dự án crawl dữ liệu đề thi và tài liệu giáo dục từ các nguồn trực tuyến, sử dụng Scrapy framework.

## 📋 Mô tả

Crawler tự động thu thập và xử lý dữ liệu đề thi các môn học (Toán, Hóa, STEM) từ website loigiaihay.com và các nguồn khác. Dữ liệu được cấu trúc hóa và lưu trữ dưới dạng JSON, phù hợp cho các ứng dụng học tập và phân tích.

## 🗂️ Cấu trúc dự án

```
crawler/
├── crawler/
│   ├── spiders/
│   │   ├── math_loigiaihay.py      # Spider crawl đề thi Toán
│   │   ├── stem_loigiaihay.py      # Spider crawl STEM (Khoa học tự nhiên)
│   │   ├── ptit_crawler.py         # Spider crawl tin tức PTIT
│   │   └── vietjack.py             # Spider crawl từ Vietjack
│   ├── utils/
│   │   └── get_collections.py      # Hàm tạo collection links
│   ├── items.py                    # Định nghĩa data items
│   ├── middlewares.py              # Custom middlewares
│   ├── pipelines.py                # Data processing pipelines
│   └── settings.py                 # Cấu hình Scrapy
├── pyproject.toml                  # Dependencies & project config
├── scrapy.cfg                      # Scrapy configuration
└── README.md
```

## 🚀 Cài đặt

### Yêu cầu

- Python 3.11+
- pip hoặc uv package manager

### Các bước cài đặt

1. Clone repository:
```bash
git clone <repository-url>
cd crawler
```

2. Tạo virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# hoặc
.venv\Scripts\activate     # Windows
```

3. Cài đặt dependencies:
```bash
pip install -r requirements.txt
# hoặc sử dụng uv
uv sync
```

## 📖 Sử dụng

### Chạy spider cơ bản

```bash
# Crawl đề thi Toán lớp 10
scrapy crawl math_loigiaihay -o math_10.json

# Crawl đề thi STEM lớp 10
scrapy crawl stem_loigiaihay -o stem_10.json

# Crawl đề thi Hóa lớp 10
scrapy crawl chemical_loigiaihay -o chemical_10.json
```

### Tuỳ chỉnh output

```bash
# Export ra CSV
scrapy crawl math_loigiaihay -o output.csv

# Export ra JSON Lines
scrapy crawl math_loigiaihay -o output.jsonl

# Export với encoding cụ thể
scrapy crawl math_loigiaihay -o output.json -s FEED_EXPORT_ENCODING=utf-8
```

## 🕷️ Spiders

### 1. **math_loigiaihay**
- **Nguồn**: loigiaihay.com
- **Mục đích**: Crawl đề thi Toán 

### 2. **stem_loigiaihay**
- **Nguồn**: loigiaihay.com
- **Mục đích**: Crawl đề thi Khoa học tự nhiên 
- 
### 3. **chemical_loigiaihay**
- **Nguồn**: loigiaihay.com
- **Mục đích**: Crawl đề thi Hóa học 

### 4. **ptit_crawler**
- **Nguồn**: ptit.edu.vn
- **Mục đích**: Crawl tin tức và bài viết từ PTIT

## 🔧 Pipelines

### ExamPipeline
- Validate các trường bắt buộc (question, answer, grade, subject)
- Loại bỏ items chứa hình ảnh markers
- Xóa prefix "Câu X:" khỏi câu hỏi
- Làm sạch và format dữ liệu

### StemPipeline
- Tương tự ExamPipeline
- Thêm filter loại bỏ câu hỏi chứa từ "bảng"
- Xóa các chuỗi không cần thiết (Phần tự luận, HẾT, etc.)

### PtitPipeline
- Lưu content vào file text
- Tổ chức theo cấu trúc thư mục

## ⚙️ Cấu hình

### settings.py

```python
ROBOTSTXT_OBEY = True                    # Tuân thủ robots.txt
CONCURRENT_REQUESTS_PER_DOMAIN = 4       # Số request đồng thời
DOWNLOAD_DELAY = 2                       # Delay giữa các request (giây)
FEED_EXPORT_ENCODING = 'utf-8'          # Encoding cho output file
LOG_LEVEL = 'INFO'                       # Mức độ logging
```

## 📝 Lưu ý

1. **Rate limiting**: Crawler có DOWNLOAD_DELAY = 2s để tránh overload server
2. **Robots.txt**: Tự động tuân thủ quy tắc robots.txt
3. **Data quality**: Pipeline tự động validate và filter dữ liệu
4. **Images**: Items chứa hình ảnh sẽ bị dropped (có thể tuỳ chỉnh)

## 🛠️ Development

### Thêm spider mới

```bash
scrapy genspider <spider_name> <domain>
```

### Test spider

```bash
# Test với 1 URL cụ thể
scrapy parse <url> --spider=<spider_name>

# Chạy với debug mode
scrapy crawl <spider_name> -L DEBUG
```

### Xem log

```bash
tail -f scrapy_log.txt
```