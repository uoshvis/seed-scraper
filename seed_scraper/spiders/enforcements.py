import scrapy


class EnforcementsSpider(scrapy.Spider):
    name = 'enforcements'
    allowed_domains = ['research.seed.law.nyu.edu']
    start_urls = ['https://research.seed.law.nyu.edu/Search/Results']

    def parse(self, response):
        pass
