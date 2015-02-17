# -*- coding: utf-8 -*-

# Scrapy settings for crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import pymongo

BOT_NAME = 'eventspider'

SPIDER_MODULES = ['eventspider.spiders']
NEWSPIDER_MODULE = 'eventspider.spiders'
ITEM_PIPELINES = {'eventspider.pipelines.EventPipeline':0}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'crawler (+http://www.yourdomain.com)'





#mongodb
MONGO_HOST = "127.0.0.1"
MONGO_PORT = 27017
MONGO_DB = pymongo.Connection(host=MONGO_HOST,port=MONGO_PORT).crawler