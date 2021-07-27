import scrapy


class ThespiderSpider(scrapy.Spider):
    name = 'thespider'
    start_urls = ['https://www.amazon.com/dp/B08HR5SXPS/?coliid=IHXESHSBC60PX&colid=6GEW9TQ8VS1D&psc=0&ref_=lv_vv_lig_dp_it']

    def parse(self, response):
        data={}
        cards=response.css('div.pc en_US')
        for card in cards:
            for c in card.css('div.a-container'):
                data['title'] = c.css('span::attr(productTitle)').getall()
                yield data

