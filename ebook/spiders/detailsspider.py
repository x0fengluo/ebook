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

    name = 'details'
    # 自定义配置
    custom_settings = {
        # item处理管道
        'ITEM_PIPELINES': {
            'ebook.pipelines.DetailsPipelines.DetailsPipelines': 500,
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

            exit("check var is_download  is true should flase")

        else:
            yield scrapy.Request(self.article_url, callback=self.contents)


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
    def contents(self, response):


        # 获取页面内容
        datas = response.css(self.contents_conf["robot_url_tag"]).extract()
        if datas == None:
            self.log("contents中的robot_url_tag选择器写的不正确", level=logging.ERROR)
            return False

        c_index = 0
        for data in datas:

            title = Selector(text=data).css('a::text').extract_first()
            url = Selector(text=data).css('a::attr(href)').extract_first()
            onclick_url = Selector(text=data).css('a::attr(onclick)').re(r'\w\(\'(.*)\'\)')  # .extract()

            # 如果是JS跳转的就要用JS传的参数,否则用href属性
            url = onclick_url[0] if onclick_url != [] else url

            # 如果是http://xxxxx全路径就不用处理了,否则要加上前面的url
            url = (response.url + url) if not url.startswith('http') else url

            content ={}
            content['article_name'] = self.article_name
            content['content_name'] = title
            content['index'] = c_index


            yield scrapy.Request(url,callback=self.details,meta=content)

            c_index = c_index+1

        else:

            self.log("contents的url:%s采集完毕" % response.url, level=logging.INFO)


    def details(self, response):

        # 字符有问题 SO用requests吧
        result = self.open_url(response.url)

        # 获取页面内容
        datas = Selector(text=result).css(self.details_conf["robot_url_tag"]).extract()
        if datas == None:
            self.log("details中的robot_url_tag选择器写的不正确", level=logging.ERROR)
            return False

        # 如果获取到内容
        if datas != []:

            for data in datas:
                # 保存当前
                item = DetailItem()
                item['url'] = response.url
                item['title'] = response.meta['article_name']
                item['content'] = response.meta['content_name']
                item['index'] = response.meta['index']
                item['data'] = data
                yield item
        else:

            self.log("details的url:%s采集完毕" % response.url, level=logging.INFO)
