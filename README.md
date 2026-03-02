# Educational Data Crawler

Dự án crawl dữ liệu đề thi và tài liệu giáo dục từ các nguồn trực tuyến, sử dụng Scrapy framework.

## 📋 Mô tả

Crawler tự động thu thập và xử lý dữ liệu đề thi các môn học (Toán, Vật Lý, Hóa học) từ website loigiaihay.com và các nguồn khác. Dữ liệu được cấu trúc hóa và lưu trữ dưới dạng JSON, với tính năng tự động phát hiện môn học và lớp từ URL.

## ✨ Tính năng chính

- 🎯 **Auto-detection**: Tự động phát hiện môn học và lớp học từ URL
- 🧹 **Data cleaning**: Pipeline xử lý và làm sạch dữ liệu tự động
- 📚 **Multi-subject**: Hỗ trợ Toán, Vật Lý, Hóa học (lớp 6-12)
- 🔄 **Chunking**: Xử lý và phân đoạn dữ liệu cho training AI
- 📊 **Multiple formats**: Export JSON, CSV, JSON Lines

## 🗂️ Cấu trúc dự án

```
crawler/
├── crawler/
│   ├── spiders/
│   │   ├── loigiaihay.py           # Spider chính crawl đề thi (Toán, Lý, Hóa)
│   │   ├── ptit_crawer.py          # Spider crawl tin tức PTIT
│   │   └── vietjack.py             # Spider crawl từ Vietjack
│   ├── utils/
│   │   ├── get_collections.py      # Tạo collections links theo môn/lớp
│   │   └── get_links.py            # Utility functions cho links
│   ├── items.py                    # Định nghĩa data items (StemItem, ExamItem)
│   ├── middlewares.py              # Custom middlewares
│   ├── pipelines.py                # Data cleaning pipelines
│   └── settings.py                 # Cấu hình Scrapy
├── *.json                          # Output files (math, physics, chemistry)
├── pyproject.toml                  # Dependencies & project config
├── scrapy.cfg                      # Scrapy configuration
├── main.py                         # Entry point script
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
# Crawl tất cả đề thi (Toán, Lý, Hóa lớp 6-12)
scrapy crawl loigiaihay -o output.json

# Crawl tin tức PTIT
scrapy crawl ptit_crawer -o ptit.json

# Crawl từ Vietjack
scrapy crawl vietjack -o vietjack.json
```

### Tuỳ chỉnh output

```bash
# Export ra CSV
scrapy crawl loigiaihay -o output.csv

# Export ra JSON Lines
scrapy crawl loigiaihay -o output.jsonl

# Export với encoding cụ thể
scrapy crawl loigiaihay -o output.json -s FEED_EXPORT_ENCODING=utf-8
```

### Chạy với main.py

```bash
python main.py
```

## 🕷️ Spiders

### 1. **loigiaihay**
- **Nguồn**: loigiaihay.com
- **Mục đích**: Crawl đề thi Toán, Vật Lý, Hóa học (lớp 6-12)
- **Tính năng**: 
  - Tự động phát hiện môn học từ URL (math, physics, chemistry)
  - Tự động phát hiện lớp từ URL (6, 7, 8, 9, 10, 11, 12)
  - Trích xuất câu hỏi, lời giải, đáp án
  - Xử lý hình ảnh và bảng biểu
- **Output fields**: `question`, `reasoning`, `answer`, `subject`, `grade`

### 2. **ptit_crawer**
- **Nguồn**: ptit.edu.vn
- **Mục đích**: Crawl tin tức và bài viết từ Học viện Công nghệ Bưu chính Viễn thông
- **Output**: Text files được lưu theo thư mục

### 3. **vietjack**
- **Nguồn**: vietjack.com
- **Mục đích**: Crawl tài liệu học tập từ Vietjack

## 🔧 Pipelines

### ExamPipeline
- **Validate data**: Kiểm tra các trường bắt buộc (question, answer, grade, subject)
- **Clean questions**: Xóa prefix "Câu X:" và các ký tự đặc biệt
- **Filter images**: Loại bỏ items chứa image markers `[[HAS_IMAGE]]`
- **Advanced cleaning**: 
  - Xóa điểm số (8 điểm, 12 điểm, v.v.)
  - Xóa date patterns và timestamps
  - Xóa "PHẦN TỰ LUẬN", "HẾT", etc.
  - Reorganize "Đáp án X" patterns
  - Xóa URL patterns

### StemPipeline
- **Extends ExamPipeline**: Kế thừa tất cả tính năng của ExamPipeline
- **Additional filters**:
  - Loại bỏ câu hỏi chứa từ "bảng" (câu hỏi tham chiếu bảng)
  - Xử lý đặc biệt cho dữ liệu STEM
- **Regex cleaning**: Pattern matching nâng cao cho Vietnamese text

### PtitPipeline
- **Save to files**: Lưu content vào file `.txt`
- **Organize structure**: Tổ chức theo thư mục `data/ptit/`
- **Text processing**: Xử lý và format text content

### Data Cleaning Functions

```python
clean_item(item_dict):
    """
    Làm sạch dữ liệu với 10+ regex patterns:
    - Xóa score markers (điểm)
    - Xóa date/time patterns  
    - Xóa answer prefixes
    - Xóa exam markers (HẾT, PHẦN TỰ LUẬN)
    - Normalize whitespace
    """
```

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
4. **Images**: Items chứa hình ảnh sẽ bị dropped (có thể tuỳ chỉnh trong pipeline)
5. **Auto-detection**: Spider tự động detect môn học và lớp, không cần config thủ công

## 📊 Data Collections

### Supported Subjects & Grades

- **Toán (Math)**: Lớp 6, 10, 11, 12
- **Vật Lý (Physics)**: Lớp 10, 11, 12
- **Hóa Học (Chemistry)**: Lớp 10, 11, 12

### Collection Functions

File `crawler/utils/get_collections.py` chứa các hàm tạo collections:

```python
create_collection_link_math_11()      # 140+ URLs đề thi Toán 11
create_collection_link_physics_11()   # URLs đề thi Vật Lý 11
create_collection_link_chemical_10()  # URLs đề thi Hóa 10
# ... và nhiều functions khác
```

### Subject Detection Patterns

```python
# Toán: 'toan', 'dai-so', 'giai-tich', 'hinh-hoc'
# Vật Lý: 'vat-ly', 'vat-li', 'ly-thuyet'
# Hóa Học: 'hoa-hoc'
```

## 📦 Output Data Structure

### JSON Format

```json
{
  "question": "Câu hỏi đề thi...",
  "reasoning": "Lời giải chi tiết...",
  "answer": "A",
  "subject": "math",
  "grade": "11"
}
```

### Available Output Files

- `math_loigiaihay.json` - Đề thi Toán
- `physics_11.json`, `physics_12.json` - Đề thi Vật Lý
- `chemical_loigiaihay.json` - Đề thi Hóa
- `loigiaihay_cleaned.json` - Dữ liệu đã cleaned

## 🛠️ Development

### Thêm spider mới

```bash
scrapy genspider <spider_name> <domain>
```

### Test spider

```bash
# Test với 1 URL cụ thể
scrapy parse <url> --spider=loigiaihay

# Chạy với debug mode
scrapy crawl loigiaihay -L DEBUG

# Test với số lượng giới hạn
scrapy crawl loigiaihay -o test.json -s CLOSESPIDER_ITEMCOUNT=10
```

### Xem log

```bash
# Xem realtime log
tail -f scrapy_log.txt

# Windows PowerShell
Get-Content scrapy_log.txt -Wait
```

## 🧩 Data Processing & Chunking

### Chunking Workflow

Thư mục `crawler/chunking/` chứa notebooks và scripts để xử lý dữ liệu:

1. **chunking.ipynb**: Jupyter notebook để chunk dữ liệu thành smaller pieces
2. **data_chunked.json**: Output data đã được chunked
3. **data_ptit.json**: PTIT data đã được processed

### Usage

```bash
# Mở Jupyter notebook
jupyter notebook crawler/chunking/chunking.ipynb
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is for educational purposes.

## 🔗 Resources

- [Scrapy Documentation](https://docs.scrapy.org/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Python Regex Guide](https://docs.python.org/3/library/re.html)