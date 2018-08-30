#!/usr/bin/env python
# encoding: utf-8


"""
mail:wqc2008@gmail.com
@createtime: 17/10/30 下午4:44
@license: Apache Licence 2.0
usege:
    ......
    
"""

import  time
import  pymongo
import  requests
from settings import  MONGO_DATABASE,MONGO_URI,CURRENT_SITE_NAME,BOT_NAME

client = pymongo.MongoClient(MONGO_URI)
db = client[MONGO_DATABASE]


url ="http://localhost:6800/schedule.json"

data = {"project":BOT_NAME, "spider":"sites", "site_name":CURRENT_SITE_NAME }
r = requests.post(url,data)
print(r.text)


