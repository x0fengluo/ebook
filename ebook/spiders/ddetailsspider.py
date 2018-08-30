# -*- coding: utf-8 -*-

import time
import scrapy
import logging
from scrapy.selector import Selector
from scrapy.conf import settings
from scrapy.spiders import CrawlSpider
import  requests
from scrapy.conf import settings
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError



from ebook.items import *




class ContentsSpider(CrawlSpider):
    """
    小说章节目录入口和章节内容采集
    """

    name = 'ddetails'
    # 自定义配置
    custom_settings = {
        # item处理管道
        'ITEM_PIPELINES': {
            'ebook.pipelines.DDetailsPipelines.DDetailsPipelines': 5,
        },
    }

    # 初始化,从参数中读取
    def __init__(self, site_name=None, article_name=None, article_url=None, *args, **kwargs):

        self.site_name = site_name
        self.article_name = article_name
        self.article_url = article_url

        self.contents_conf = settings.get('SITE').get(site_name, None).get("contents", None)
        self.details_conf = settings.get('SITE').get(site_name, None).get("details", None)
        self.contents_conf_is_download = settings.get('SITE').get(site_name, None).get("contents", None).get("is_download",False)

        super(ContentsSpider, self).__init__(*args, **kwargs)

    # 爬取网站入口设置
    def start_requests(self):

        if self.contents_conf_is_download:
            yield scrapy.Request(self.article_url, callback=self.contents_download)



    def open_url(self, url):

        r = requests.get(url)

        if r.status_code == requests.codes.ok:

            r.encoding = "utf-8" if self.details_conf.get("charset", None) == None  else  self.details_conf.get("charset", None)

            html = r.text
            return html
        else:
            return False

            # 解析数据


    # 解析数据
    def contents_download(self, response):


        download_url = response.css(self.contents_conf["robot_url_tag"]).css('a::attr(href)').extract()[1]
        print(download_url)

        title = response.css(".title::text").extract_first()
        print(title)


        matpl = DDetailItem()
        matpl['file_url'] = download_url
        matpl['file_name'] = title
        return matpl

