# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time

class EventPipeline(object):
    def process_item(self, item, spider):

        db = spider.settings.get('MONGO_DB')


        if spider.name == "eventful":


            res = db.events.update({"id":item['id']},{"$set":{
                "title":item['title'],
                "url":item['url'],
                "description":item['description'],
                "start_time":item['start_time'],
                "venue_id":item['venue_id'],
                "venue_url":item['venue_url'],
                "country":item['country'],
                "city":item['city'],
                "image":item['image'],
                "latitude":item['latitude'],
                "longitude":item['longitude'],
                "update_time":int(time.time())
                #dict(item)
            }}, upsert=True)


        elif spider.name == "eventbrite":
            #res = db.events.update({"id":item['id']},{"$set":item['event']}, upsert=True)


            pass


        return item


