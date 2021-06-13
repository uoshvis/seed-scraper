# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EnforcementItem(scrapy.Item):

    legal_case_name = scrapy.Field()
    legal_case_detail_url = scrapy.Field()
    defendant_name = scrapy.Field()
    defendant_type = scrapy.Field()
    first_doc_date = scrapy.Field()
    first_resolution_date = scrapy.Field()
    allegation_type = scrapy.Field()
    initial_filling_format = scrapy.Field()
    case_number = scrapy.Field()
    federal_district_court = scrapy.Field()
    # sic_code = scrapy.Field()
    # cusip = scrapy.Field()

