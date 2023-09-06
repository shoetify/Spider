import scrapy


class AudibleSpider(scrapy.Spider):
    name = 'audible'
    allowed_domains = ['www.audible.com']
    start_urls = ['https://www.audible.com/search']

    def parse(self, response):
        product_container = response.xpath('//div[@class="adbl-impression-container "]/div/span/ul/li')

        for product in product_container:
            book_title = product.xpath('.//h3[contains(@class, "bc-heading")]/a/text()').get()
            book_author = product.xpath('.//li[contains(@class, "authorLabel")]/span/a/text()').getall()
            book_length = product.xpath('.//li[contains(@class, "runtimeLabel")]/span/text()').get()

            yield {
                'title': book_title,
                'author': book_author,
                'length': book_length,
            }

        # 获取next button的url
        pagination = response.xpath("//ul[contains(@class, 'pagingElements')]")
        next_button_url = pagination.xpath(".//span[contains(@class, 'nextButton')]/a/@href").get()

        # 如果有下一页，则继续爬
        if next_button_url:
            yield response.follow(url=next_button_url, callback=self.parse)