# -*- coding: utf-8 -*-
from __future__ import division
import os
import math
from scrapy.selector import HtmlXPathSelector
from crawler.items import EventBriteItem
from scrapy.spider import Spider
from scrapy.http.request import Request
from scrapy.conf import settings
import json

class EventBriteSpider(Spider):

    name = 'eventbrite'


    start_urls = ["https://www.eventbrite.com/json/event_search?country=CA&app_key=UIOOMGYQ2RIDNNTFMB"]





    def parse(self, response):

        #print response.body
        #获取页面内容

        try:
            ret = json.loads(response.body)
            total_items = ret['events'][0]['summary']['total_items']
            page_size = ret['events'][0]['summary']['num_showing']
        except:
            pass

        page_number = int(math.ceil(total_items / page_size))

        for n in range(1, page_number + 1):
            url = response.url+"&page=%d" % n
            yield Request(url, callback=self.extract_url)
            break



    def extract_url(self, response):
        ret = json.loads(response.body)
        events = ret['events'][1:]
        items = {}
        for e in events:
            item = EventBriteItem()
            item['event'] = json.dumps(e)
            item['id'] = e['id']

        pass







    def __init__(self, name=None, **kwargs):
        super(EventBriteSpider, self).__init__(name, **kwargs)