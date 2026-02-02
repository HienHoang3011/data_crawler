import scrapy


class VietjackSpider(scrapy.Spider):
    name = "vietjack"
    allowed_domains = ["vietjack.com"]
    start_urls = ["https://vietjack.com"]

    def parse(self, response):
        pass
