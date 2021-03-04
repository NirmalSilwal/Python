import scrapy
from ..items import FlipcartcrawlingItem


class FlipcartclothingSpider(scrapy.Spider):
    name = 'flipcartClothing'
    page_number = 2

    # TODO handle for multiple url at same time
    start_urls = [
        # 'https://www.flipkart.com/clothing-and-accessories/topwear/pr?sid=clo%2Cash&otracker=categorytree&p%5B%5D=facets.ideal_for%255B%255D%3DMen&page=1'
        'https://www.flipkart.com/womens-footwear/pr?sid=osp,iko&otracker=nmenu_sub_Women_0_Footwear&page=1'
    ]

    def parse(self, response):

        items = FlipcartcrawlingItem()

        all_prod_categories = ['mens topwear', 'womens footwear']

        all_responses = response.css('._373qXS')

        for myresponse in all_responses:

            name = myresponse.css('.IRpwTa::text').extract()
            brand = myresponse.css('._2WkVRV::text').extract()

            original_price = myresponse.css('._3I9_wc::text')[1::2].extract()
            original_price = [float(i.replace(',', '')) for i in original_price]

            sale_price = myresponse.css('._30jeq3::text').extract()
            sale_price = [float(i[1:].replace(',', '')) for i in sale_price]

            # TODO, resolve it as it is giving blank url
            image_url = myresponse.css('._2r_T1I::attr(src)').extract()
            # image_url = myresponse.css('._2r_T1I')
            # image_url = myresponse.xpath('//img[contains(@class,"._2r_T1I")]/@src').extract()[0]
            # response.selector.xpath('//img/@src').extract()

            product_page_url = response.url

            # for men
            # product_category = all_prod_categories[0]

            # for women
            product_category = all_prod_categories[1]

            items['name'] = name
            items['brand'] = brand
            items['original_price'] = original_price
            items['sale_price'] = sale_price
            items['image_url'] = image_url
            items['product_page_url'] = product_page_url
            items['product_category'] = product_category

            yield items

        # for mens
        # next_page = "https://www.flipkart.com/clothing-and-accessories/topwear/pr?sid=clo%2Cash&otracker=categorytree&p%5B%5D=facets.ideal_for%255B%255D%3DMen&page=" + str(FlipcartclothingSpider.page_number)

        # for womens
        next_page = 'https://www.flipkart.com/womens-footwear/pr?sid=osp%2Ciko&otracker=nmenu_sub_Women_0_Footwear&page=' + str(FlipcartclothingSpider.page_number)

        if FlipcartclothingSpider.page_number <= 25:
            FlipcartclothingSpider.page_number += 1

            yield response.follow(next_page, callback=self.parse)

