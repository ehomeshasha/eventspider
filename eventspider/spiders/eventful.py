# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import XMLFeedSpider
from scrapy.http.request import Request
from crawler.items import EventItem
import re

class EventfulSpider(XMLFeedSpider):
    name = 'eventful'
    #allowed_domains = ['eventful.com']
    start_urls = ['http://api.eventful.com/rest/events/search?app_key=9TqKHHbdpcf33wmb&location=canada']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'search' # change it accordingly

    description_pattern = re.compile(r'^<description\s*>([\s\S]+)</description>$')
    image_pattern = re.compile(r'^<image\s*>([\s\S]+)</image>$')



    def parse_node(self, response, node):

        page_count = int(node.xpath('page_count/text()').extract()[0])
        print page_count
        for n in range(1, page_count+1):
            url = self.start_urls[0]+"&page_number="+str(n)
            yield Request(url, callback=self.parse_item)
            #break
            #if page_count > 5:
            #    break
#        print page_count

        #i = CrawlerItem()
        #i['url'] = selector.select('url').extract()
        #i['name'] = selector.select('name').extract()
        #i['description'] = selector.select('description').extract()
        #return i

    def parse_item(self, response):

        event_list = response.xpath('descendant::event')
        #id, title,url,description,start_time,venue,country,city,image,category,tag,latitude, longitude
        event_items = []
        for event in event_list:
            event_item = EventItem()

            #id
            event_item['id'] = event.xpath('@id').extract()[0]

            #title
            event_item['title'] = event.xpath('title/text()').extract()[0]

            #url
            event_item['url'] = event.xpath('url/text()').extract()[0]

            #description
            description_text = event.xpath('description').extract()[0]
            description_match = re.search(self.description_pattern, description_text)
            if description_match:
                event_item['description'] = description_match.group(1)
            else:
                event_item['description'] = ''

            #start_time
            event_item['start_time'] = event.xpath('start_time/text()').extract()[0]

            #venue_id
            event_item['venue_id'] = event.xpath('venue_id/text()').extract()[0]

            #venue_url
            event_item['venue_url'] = event.xpath('venue_url/text()').extract()[0]

            #country
            event_item['country'] = event.xpath('country_name/text()').extract()[0]

            #city
            event_item['city'] = event.xpath('city_name/text()').extract()[0]

            #image

            image_text = event.xpath('image').extract()[0]
            image_match = re.search(self.image_pattern, image_text)
            if image_match:
                event_item['image'] = image_match.group(1)
            else:
                event_item['image'] = ''

            #latitude
            event_item['latitude'] = event.xpath('latitude/text()').extract()[0]

            #longitude
            event_item['longitude'] = event.xpath('longitude/text()').extract()[0]

            event_items.append(event_item)
            pass

        return event_items
