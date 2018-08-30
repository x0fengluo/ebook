# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SitesItem(scrapy.Item):
    # define the fields for your item here like:

    title = scrapy.Field()
    url = scrapy.Field()
    inc_num = scrapy.Field()
    status =  scrapy.Field()


class PagesItem(scrapy.Item):
    # define the fields for your item here like:

    site_name = scrapy.Field()
    page = scrapy.Field()
    url = scrapy.Field()
    inc_num = scrapy.Field()
    status =  scrapy.Field()


class ArticlesItem(scrapy.Item):
    # define the fields for your item here like:

    title = scrapy.Field()
    url = scrapy.Field()
    inc_num = scrapy.Field()
    status = scrapy.Field()


class ContentsItem(scrapy.Item):
    # define the fields for your item here like:

    article_name = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    index = scrapy.Field()
    inc_num = scrapy.Field()
    status = scrapy.Field()


class DetailItem(scrapy.Item):
    # define the fields for your item here like:

    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    data = scrapy.Field()
    index = scrapy.Field()
    inc_num = scrapy.Field()


class DDetailItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    file_url = scrapy.Field()
    file_name = scrapy.Field()
