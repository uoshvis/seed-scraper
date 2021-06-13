import os
import scrapy
from seed_scraper.items import EnforcementItem
from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst


class EnforcementsSpider(scrapy.Spider):
    name = 'enforcements'
    allowed_domains = ['research.seed.law.nyu.edu']
    start_urls = ['https://research.seed.law.nyu.edu/Search/Results']

    # output csv field order

    custom_settings = {
        "FEED_EXPORT_FIELDS": ['legal_case_name',
                               'defendant_name',
                               'defendant_type',
                               'first_doc_date',
                               'first_resolution_date',
                               'allegation_type',
                               'initial_filling_format',
                               'case_number',
                               'federal_district_court',
                               ]
    }

    try:
        os.remove('output.csv')
    except OSError:
        pass

    def parse(self, response):
        rows = response.xpath('//table//tr')
        count = 0
        for row in rows:
            td = row.xpath('td')
            if td:
                count += 1
                legal_case_detail_url = td[0].xpath('a/@href').get()
                first_resolution_date = td[4].xpath('text()').get()
                absolute_url = response.urljoin(legal_case_detail_url)
                yield scrapy.Request(url=absolute_url,
                                     callback=self.parse_details,
                                     cb_kwargs=dict(first_resolution_date=first_resolution_date)
                                     )
                # limit counter
                if count > 20:
                    break

    def parse_details(self, response, first_resolution_date):
        loader = ItemLoader(item=EnforcementItem(), response=response)
        loader.default_input_processor = MapCompose(str.strip)
        loader.default_output_processor = TakeFirst()

        loader.add_value('first_resolution_date', first_resolution_date)
        loader.add_xpath('legal_case_name',
                         '//span[contains(.//text(), "Legal Case Name")]/following-sibling::span/text()')
        loader.add_value('legal_case_detail_url',
                         response.url)
        loader.add_xpath('defendant_name',
                         '//h2[contains(./span/text(), "Defendant Name")]/span/following-sibling::text()')
        loader.add_xpath('defendant_type',
                         '//div[contains(.//text(), "Defendant Type")]/span/text()')
        loader.add_xpath('first_doc_date',
                         '//span[contains(.//text(), "First Document Date")]/following-sibling::span/text()')
        loader.add_xpath('allegation_type',
                         '//span[contains(.//text(), "Allegation Type")]/following-sibling::span/text()')
        loader.add_xpath('initial_filling_format',
                         '//span[contains(.//text(), "Initial Filing Format")]/following-sibling::span/text()')
        loader.add_xpath('case_number',
                         '//span[contains(.//text(), "Case Number")]/following-sibling::span/text()')
        loader.add_xpath('federal_district_court',
                         '//span[contains(.//text(), "Federal District Court")]/following-sibling::span/text()')

        # mostly empty fields

        # loader.add_xpath('sic_code',
        #                  '//div[contains(.//text(), "SIC Code")]/span/text()')
        # loader.add_xpath('cusip',
        #                  '//div[contains(.//text(), "CUSIP")]/span/text()')
        yield loader.load_item()

