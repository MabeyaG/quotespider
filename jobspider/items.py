import scrapy

class JobspiderItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
    link = scrapy.Field()
