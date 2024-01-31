import scrapy


class SrealityspiderSpider(scrapy.Spider):
    name = "srealityspider"
    allowed_domains = ["sreality.cz"]
    start_urls = ["https://sreality.cz/hledani/prodej/byty?_escaped_fragment_="]

    def parse(self, response):
        flats = response.css('div.property.ng-scope > div > div > span > h2 > a').get()
        for flat in flats:
            text = flat.css('span:.text')
            yield text

