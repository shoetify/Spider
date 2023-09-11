import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import time


class TranscriptsSpider(CrawlSpider):
    name = 'transcripts'
    allowed_domains = ['subslikescript.com']
    start_urls = ['https://subslikescript.com/movies_letter-X']

    rules = (
        # for scrape this whole page
        Rule(LinkExtractor(restrict_xpaths=("//ul[@class='scripts-list']/a")), callback='parse_item', follow=True),

        # to find the "next page button" and go to next page
        Rule(LinkExtractor(restrict_xpaths=("(//a[@rel='next'])[1]"))),
    )

    def parse_item(self, response):
        article = response.xpath("//article[@class='main-article']")

        # SQLite 不支持list格式，所以将list转换为string
        transcript_list = article.xpath("./div[@class='full-script']/text()").getall()
        transcript_string = ' '.join(transcript_list)

        yield {
            'title': article.xpath("./h1/text()").get(),
            'plot': article.xpath("./p/text()").get(),
            'transcript': transcript_string,
            'url': response.url,
        }
        time.sleep(1)
