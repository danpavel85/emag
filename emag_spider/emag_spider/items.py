# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


class EmagSpiderItem(scrapy.Item):
    id = scrapy.Field(output_processor = TakeFirst())
    current_price = scrapy.Field(output_processor = TakeFirst())
    initial_price = scrapy.Field(output_processor = TakeFirst())
    absolute_disc = scrapy.Field(output_processor = TakeFirst())
    percent_disc = scrapy.Field(output_processor = TakeFirst())
    url = scrapy.Field(output_processor = TakeFirst())
    part_number = scrapy.Field(output_processor = TakeFirst())
    name = scrapy.Field(output_processor = TakeFirst())
