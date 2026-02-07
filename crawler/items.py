# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
   
class ExamMathItem(scrapy.Item):
    subject = scrapy.Field()
    grade = scrapy.Field()
    question = scrapy.Field()
    reasoning = scrapy.Field()
    answer = scrapy.Field()
    
class PtitItem(scrapy.Item):
    text = scrapy.Field()
    key = scrapy.Field()
    
class StemItem(scrapy.Item):
    subject = scrapy.Field()
    grade = scrapy.Field()
    question = scrapy.Field()
    reasoning = scrapy.Field()
    answer = scrapy.Field()