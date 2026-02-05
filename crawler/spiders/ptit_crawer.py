import scrapy
from bs4 import BeautifulSoup
import re
import unicodedata

def create_start_urls_ptit():
    start_urls = [
        
    ]
class PtitCrawlerSpider(scrapy.Spider):
    name = "ptit_crawer"
    