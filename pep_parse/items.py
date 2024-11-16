import scrapy


class PepParseItem(scrapy.Item):
    number: str = scrapy.Field()
    name: str = scrapy.Field()
    status: str = scrapy.Field()
