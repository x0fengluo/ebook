#!/usr/bin/env python
# encoding: utf-8


"""
mail:wqc2008@gmail.com
@createtime: 17/10/30 下午4:44
@license: Apache Licence 2.0
usege:
    ......

"""

import time
import pymongo
import requests
from pymongo import ReturnDocument

from settings  import  MONGO_DATABASE,MONGO_URI,CURRENT_SITE_NAME,BOT_NAME

client = pymongo.MongoClient(MONGO_URI)
db = client[MONGO_DATABASE]
url = "http://localhost:6800/schedule.json"

i = 0
while True:

    where = {"status": 0}
    updata = {'$set': {'status': 1}}
    sort = [('inc_num', pymongo.ASCENDING)]

    result = db["articles"].find_one_and_update(where, updata, sort=sort, return_document=ReturnDocument.AFTER)

    if result != None:

        data = {"project": BOT_NAME, "spider": 'details', "site_name": CURRENT_SITE_NAME, "article_name": result['title'],
                "article_url": result['url']}
        r = requests.post(url, data)
        print(r.text)

    else:

        print("在数据库中pages中状态为0 已经为空")
        break

    i = i + 1

    if i % 10 == 0:
        time.sleep(3)

