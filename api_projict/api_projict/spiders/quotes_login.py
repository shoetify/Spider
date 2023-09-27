import scrapy
from scrapy import FormRequest


class QuotesLoginSpider(scrapy.Spider):
    name = 'quotes_login'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/login']

    def parse(self, response):
        #获得csrf_token
        csrf_token = response.xpath("//input[@name='csrf_token']/@value").get()

        # 将登录信息填写如表格并发送
        yield FormRequest.from_response(
            response,
            formxpath='//form',
            formdata={
                'csrf_token': csrf_token,
                'username': 'admin',
                'password': 'admin',
            },
            callback=self.after_login
        )

    # Logged in 之后的页面
    def after_login(self, response):
        # 验证，如果页面中有Logout则证明登录成功
        if response.xpath("//a[@href='/logout']/text()").get() == 'Logout':
            print('Successful Logged in!')
