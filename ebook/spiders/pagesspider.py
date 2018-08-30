# -*- coding: utf-8 -*-

from urllib import parse
from scrapy.conf import settings
from scrapy.spiders import CrawlSpider

from ebook.items import *
from scrapy.selector import Selector


def get_domain_root(url):
    from tld import parse_tld
    domain_root = ""
    try:

        ## 若不是 http或https开头，则补上方便正则匹配规则
        if len(url.split("://")) <= 1 and url[0:4] != "http" and url[0:5] != "https":
            url = "http://" + url

        domain_root = '.'.join(list(parse_tld(url))[::-1])
    except Exception as ex:
        domain_root = "-"
    return domain_root

class PagesSpider(CrawlSpider):
    name = 'pages'

    # 自定义配置
    custom_settings = {
        # item处理管道
        'ITEM_PIPELINES': {
            'ebook.pipelines.PagesPipelines.PagesPipelines': 300,
        },
    }

    # 初始化,从参数中读取
    def __init__(self, site_name=None, site_url=None, *args, **kwargs):
        self.site_name = site_name
        self.url = site_url
        self.page = settings.get('SITE').get(site_name, None).get("pages", None)

        super(PagesSpider, self).__init__(*args, **kwargs)

    # 爬取网站入口设置
    def start_requests(self):
        # 指定开始页面以及允许的域名
        #self.allowed_domains = [parse.urlparse(self.url).netloc]

        yield scrapy.Request(self.url, self.parse)

    # 解析数据
    def parse(self, response):


        # 保存当前
        item = PagesItem()
        item['site_name'] = self.site_name
        item['url'] = response.url
        item['status'] = 0
        yield item

        # 下页
        next_url  = response.css(self.page["robot_url_tag"]).css('a::attr(href)').extract_first()


        # 如果有下页, 递归执行
        if next_url != None:

            self.host = get_domain_root(response.url)
            if  next_url.startswith('http') == False:
                next_url = "http://" + self.host + "/" + next_url

            yield scrapy.Request(next_url, callback=self.parse, meta=response.meta)
