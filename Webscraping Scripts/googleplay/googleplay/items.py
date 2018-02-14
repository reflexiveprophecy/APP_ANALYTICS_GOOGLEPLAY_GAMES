# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class GoogleplayItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    appname = scrapy.Field()
    companyname = scrapy.Field()
    gamecategory = scrapy.Field()
    starrating = scrapy.Field()
    appprice = scrapy.Field()
    badgetitle = scrapy.Field()
    inapppurchase = scrapy.Field()
    inappprice = scrapy.Field()
    ads = scrapy.Field()
    ratingnums = scrapy.Field()
    newcontent = scrapy.Field()
    version = scrapy.Field()
    requiredsystem = scrapy.Field()
    developerinfo = scrapy.Field()
    contentrating = scrapy.Field()
    installs = scrapy.Field()
    updatedate = scrapy.Field()
    imagenum = scrapy.Field()
    reviewcontent = scrapy.Field()
    reviewer = scrapy.Field()
    reviewrating = scrapy.Field()
    reviewdate = scrapy.Field()
    toplist = scrapy.Field()
