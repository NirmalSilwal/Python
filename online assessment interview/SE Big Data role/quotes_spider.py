import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):

        all_div_quotes = response.css("div.quote")

        for myqote in all_div_quotes:
            title = myqote.css("span.text::text").extract()
            author_name = myqote.css(".author::text").extract()
            tags = myqote.css(".tag::text").extract()
            yield {
                "title": title,
                "author" : author_name,
                "tags" : tags
            }