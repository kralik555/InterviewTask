import scrapy

class SrealitySpider(scrapy.Spider):
    name = 'srealityspider'
    allowed_domains = ['sreality.cz']
    start_urls = [f"https://www.sreality.cz/hledani/prodej/byty?strana={i}_escaped_fragment_=" for i in range(1, 26)]

    def parse(self, response):
        names = response.css('span.name.ng-binding::text').getall()
        locations = response.css('span.locality.ng-binding::text').getall()
        costs = response.css('span.norm-price.ng-binding::text').getall()
        url_string = response.url
        page = 1
        images = []
        try:
            first_num = int(url_string.split("=")[1][0])
            second_num = int(url_string.split("=")[1][1])
            page = 10 * first_num + second_num
        except:
            page = int(url_string.split("=")[1][0])
        for property in response.css('div.property.ng-scope'):
            property_images = property.css('preact > div > div > a > img::attr(src)').getall()[:3]
            property_images += [''] * (3 - len(property_images))
            images += property_images

        grouped_images = [images[i:i + 3] for i in range(0, len(images), 3)]
        
        order = 0
        for name, location, cost, image_set in zip(names, locations, costs, grouped_images):
            image_set += [''] * (3 - len(image_set))
            order += 1
            print(page, order, (page - 1) * 20 + order)
            yield {
                'name': name,
                'location': location,
                'cost': cost,
                'image1': image_set[0] if len(image_set) > 0 else '',
                'image2': image_set[1] if len(image_set) > 1 else '',
                'image3': image_set[2] if len(image_set) > 2 else '',
                'number': (page - 1) * 20 + order,
            }
