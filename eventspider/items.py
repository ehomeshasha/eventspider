# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EventItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    id = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()
    start_time = scrapy.Field()
    venue_id = scrapy.Field()
    venue_url = scrapy.Field()
    country = scrapy.Field()
    city = scrapy.Field()
    image = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()


    pass


class EventBriteItem(scrapy.Item):
    id = scrapy.Field()
    event = scrapy.Field()
