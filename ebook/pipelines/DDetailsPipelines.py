# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html




import scrapy
import os
# from scrapy.pipeline.images import ImagesPipeline
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem

class DDetailsPipelines(FilesPipeline):

    def get_media_requests(self, item,info):
        for url in item["file_url"]:
            yield scrapy.Request(url)


    def get_media_requests(self, item, info):


        yield scrapy.Request(item["file_url"],meta={'item': item})


    def file_path(self, request, response=None, info=None):
        file_name = request.meta['item']['file_name']

        return  "full/%s"%file_name