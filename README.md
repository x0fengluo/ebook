
1.环境
1.1.机器环境

    mongodb3.4 python2.7 pip9.0

1.2.python环境

    pip install requests[security]
    #http://docs.python-requests.org/en/master/

    pip install beautifulsoup4
    #https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id5

    pip install pymongo
    #https://github.com/mongodb/mongo-python-driver

    pip install scrapy
    #http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html


2.使用方式


2.1 一个窗口启动服务

	- scrapyd

2.2 一个窗口发布代码[只要有代码更新就要发布一次]

	- scrapyd-deploy ebook -p ebook
2.3 改配置:

	###=============================================
	#采集dybz
	SITE["dybz"] = {}
	## dybz 采集的列表入口地址
	SITE["dybz"]['site'] = {
	    "title": "dybz",
	    "url": "http://m.335xs.net/ph/week_2.html"
	}
	## dybz 采集的列表上面分页的标识
	SITE["dybz"]['pages'] = {
	    "charset": "utf-8",
	    "robot_url_tag": "p.page a:last-child "
	}
	## dybz 采集的分页上面文章的标识
	SITE["dybz"]['articles'] = {
	    "charset": "gbk",
	    "robot_url_tag": "div.hot_sale a",
	}
	## dybz 采集的文章的章节的标识
	SITE["dybz"]['contents'] = {
	    "is_download": True,
	    "charset": "gbk",
	    "robot_url_tag": '.btn >a:last-child ',
	
	}
	## dybz 采集的章节内容的标识
	SITE["dybz"]['details'] = {
	    "charset": "gbk",
	    "robot_url_tag": u'div.box_box ',
	}

2.4  依次执行:

	rebot_sites.py
	rebot_pages.py
	rebot_articles.py
	rebot_details.py
	rebot_ddetails.py 如果页面上有下载用这个
	
	


## 下面是介绍怎么样做的 看不看都可以

2. 采集规律分析

2.1. 定位采集列表入口位置
    有分页的所以要实现翻页功能

    scrapy crawl pages -a site_name=dybz -a url="https://www.dybz.in/shuku.html"


2.2.定位每篇文章的入口
    每一页中的文章标题就是文章的入口

    scrapy crawl  articles -a site_name=dybz -a url="https://www.dybz.in/shuku/shuku_0_20.html"


2.3.采集每篇文章的章节列表
    有的站点有下载链接,为了统一处理,所以还是一章节一章节的采集比较通用

    scrapy crawl details -a site_name=dybz -a article_name=xxxx -a article_url=https://www.dybz.in/6/6475/



3.并发采集

3.1 规则介绍
    scrapy.cfg 格式
    [deploy:<target>]
    url = <url>
    project = <project>

    发布指令
    scrapyd-deploy <target> -p <project>

    查看指令
    scrapyd-deploy -l

    执行爬虫
    curl http://localhost:6800/schedule.json -d project=myproject -d spider=somespider -d setting=DOWNLOAD_DELAY=2 -d arg1=val1
    
    

4.数据导成文本

    use admin
    db.adminCommand({setParameter: 1, internalQueryExecMaxBlockingSortBytes: 524288000})

    #加引
    db.contents.ensureIndex({title:1,index:1},{background:1})


    从mongo中导出文章内容(可能要写个查询语句,排序什么的)

    mongoexport -h IP --port 端口 -u 用户名 -p 密码 -d 数据库 -c 表名 -f 字段1，字段2 -q‘{条件导出}’ --csv -o 文件名

    mongoexport   -h "127.0.0.1" -d ebook  -c articles -f title,url  -o tt.txt


参考:
http://blog.csdn.net/zp2006011242/article/details/74941004