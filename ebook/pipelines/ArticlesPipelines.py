# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class ArticlesPipelines(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def str_md5(self, data):
        import hashlib
        hash = hashlib.md5()
        hash.update(data.encode('utf-8'))
        return hash.hexdigest()

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()


    def process_item(self, item, spider):

        from pymongo import ReturnDocument

        data = self.db["%s_num" % spider.name].find_one_and_update(

            {'_id': 'userid'},

            {'$inc': {'seq': 1}},

            projection={'seq': True, '_id': False},

            upsert=True,

            return_document=ReturnDocument.AFTER)

        item["inc_num"] = data['seq']

        self.db[spider.name].update({'url_token': self.str_md5(item['url'])}, {'$set': dict(item)}, True)
        return item
