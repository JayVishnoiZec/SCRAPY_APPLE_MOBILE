import scrapy


class FlipkartscrapySpider(scrapy.Spider):
    name = 'FlipKartScrapy'
    start_urls = ['https://www.flipkart.com/search?q=applemobile']

    def parse(self, response):
        data = response.css('._13oc-S')
        for series in data:
            Apple_item = {
                '   MOBILE_NAME     ': series.css('._4rR01T::text').getall(),
                '   APPLE_PRICE     ': series.css('._1_WHN1::text').getall(),
                '   APPLE_RATING     ': series.css('._3LWZlK::text').getall(),
                '   APPLE_FEATURES  ': series.css('.rgWa7D::text').getall(),
            }
            yield Apple_item
