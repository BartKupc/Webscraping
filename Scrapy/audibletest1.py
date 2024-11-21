import scrapy


class Audibletest1Spider(scrapy.Spider):
    name = "audibletest1"
    allowed_domains = ["www.audible.co.uk"]
    #start_urls = ["https://www.audible.co.uk/search"]

    def start_requests(self):
        yield scrapy.Request(url='https://www.audible.co.uk/search', callback=self.parse,
                       headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'})

    def parse(self, response):
        product_container = response.xpath('//div[@class="adbl-impression-container "]//li[contains(@class, "productListItem")]')

        for product in product_container:

            author = product.xpath('.//li[contains(@class , "authorLabel")]/span/a/text()').getall()
            length = product.xpath('.//li[contains(@class , "runtimeLabel")]/span/text()').get()
            title = product.xpath('.//h3[contains(@class , "bc-heading")]/a/text()').get()

            yield{
                'title': title,
                'author': author,
                'length': length,
                'User_Agent': response.request.headers['User-Agent'],
            }

        pagination = response.xpath('//ul[contains(@class , "pagingElements")]')
        next_page_url = pagination.xpath('.//span[contains(@class , "nextButton")]/a/@href').get()

        if next_page_url:
            yield response.follow(url=next_page_url, callback=self.parse,
                                  headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'})
