import scrapy

class SrealitySpider(scrapy.Spider):
    name = 'srealityspider'
    allowed_domains = ['sreality.cz']
    start_urls = [f'https://www.sreality.cz/hledani/prodej/byty?strana={i}_escaped_fragment_=' for i in range(1, 26)]

    def parse(self, response):
        names = response.css('span.name.ng-binding::text').getall()

        images = response.css('div._2xzMRvpz7TDA2twKCXTS4R > a > img::attr(src)').getall()

        grouped_images = [images[i:i + 3] for i in range(0, len(images), 3)]

        for name, image_set in zip(names, grouped_images):
            image_set += [''] * (3 - len(image_set))
            yield {
                'name': name,
                'image1': image_set[0] if len(image_set) > 0 else '',
                'image2': image_set[1] if len(image_set) > 1 else '',
                'image3': image_set[2] if len(image_set) > 2 else ''
            }
