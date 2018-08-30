#!/usr/bin/env python
# encoding: utf-8


"""
mail:wqc2008@gmail.com
@createtime: 17/10/30 下午4:44
@license: Apache Licence 2.0
usege:
    ......
    
"""

import  re
import  pymongo



client = pymongo.MongoClient(host="127.0.0.1", port=27017)
db = client['ebook']
table = db['details']

re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)  # Script


datas = table.find({},{ 'title':1,'content':1,'data':1,'index':1,'_id':0}).sort([("title", pymongo.ASCENDING),("index",pymongo.ASCENDING)])
for data in datas:

    f = open("./ebook/"+data['title'].replace("/",'')+".txt", 'a+')
    f.write(str(data['index']) + "\n")
    f.write(data['content'] + "\n")
    d = re_script.sub('', data['data'])
    d = d.replace("<br>", "\n")

    f.write(d + "\n")

    f.close()

