import scrapy
from ..items import QuotescrawlingItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    page_number = 2
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        # using items fields from items.py
        items = QuotescrawlingItem()

        # all quotes are inside this div tag with quote class
        all_div_quotes = response.css("div.quote")

        for myqote in all_div_quotes:
            title = myqote.css("span.text::text").extract()
            authors = myqote.css(".author::text").extract()
            tags = myqote.css(".tag::text").extract()

            items['title'] = title
            items['authors'] = authors
            items['tags'] = tags

            yield items

        # next_page = response.css("li.next a::attr(href)").get()
        #
        # if next_page is not None:
        #     # spider will automatically look for follow in response
        #
        #     yield response.follow(next_page, callback=self.parse)

        # Using Pagination concept now

        next_page = 'http://quotes.toscrape.com/page/' + str(QuotesSpider.page_number) + '/'

        if QuotesSpider.page_number < 11:
            QuotesSpider.page_number += 1

            yield response.follow(next_page, callback=self.parse)
