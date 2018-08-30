# -*- coding: utf-8 -*-

from urllib import parse
import logging
import pymongo
import requests
from bs4 import BeautifulSoup
from scrapy.conf import settings
from scrapy.spiders import CrawlSpider
from pymongo import ReturnDocument


def str_md5(data):
    import hashlib
    hash = hashlib.md5()
    hash.update(data.encode('utf-8'))
    return hash.hexdigest()

class PagesSpider(CrawlSpider):
    name = 'sites'


    # 初始化,从参数中读取
    def __init__(self, site_name=None, *args, **kwargs):


        self.site_name = site_name
        self.site = settings.get('SITE').get(self.site_name , None).get("site", None)

        # 从mongo中指定要获取的website
        self.client = pymongo.MongoClient(settings.get('MONGO_URI'))
        self.db = self.client[settings.get('MONGO_DATABASE')]



        result = self.db["sites"].find_one({'url_token':str_md5(self.site['url'])})

        #如果没有存此站则INSERT
        if result == None:

            #自增加一
            data = self.db["sites_num"].find_one_and_update({'_id': 'userid'},{'$inc': {'seq': 1}},upsert=True,return_document=ReturnDocument.AFTER)

            #存贮数据
            self.site['status'] = 0
            self.site['url_token'] = str_md5(self.site['url'])
            self.site["inc_num"] = data['seq']

            self.db["sites"].insert(self.site)

        #如果有 则UPDATE状态从新采集
        else:

            result['status'] = 0
            self.db["sites"].update({"url_token": result['url_token']}, result, True)

        super(PagesSpider, self).__init__(*args, **kwargs)


