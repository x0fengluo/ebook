# -*- coding: utf-8 -*-


import logging



from scrapy.conf import settings
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider

from ebook.items import *



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



class ArticlesSpider(CrawlSpider):
    """
    小说名称和小说连接入口
    """
    name = 'articles'
    # 自定义配置
    custom_settings = {
        # item处理管道
        'ITEM_PIPELINES': {
            'ebook.pipelines.ArticlesPipelines.ArticlesPipelines': 300,
        },
    }

    # 初始化,从参数中读取
    def __init__(self, site_name=None, page_url=None, *args, **kwargs):

        self.site = settings.get('SITE').get(site_name, None).get("articles", None)
        self.url = page_url




        super(ArticlesSpider, self).__init__(*args, **kwargs)

    # 爬取网站入口设置
    def start_requests(self):

        yield scrapy.Request(self.url, self.parse)

    # 解析数据
    def parse(self, response):

        self.host = get_domain_root(response.url)


        datas = response.css(self.site["robot_url_tag"]).extract()

        if datas == None:
            self.log("articles中的robot_url_tag选择器写的不正确", level=logging.ERROR)
            return  False

        # 如果获取到内容
        for data in datas:

            title = Selector(text=data).css('a::text').extract_first()
            url = Selector(text=data).css('a::attr(href)').extract_first()

            if not url.startswith('http'):
                url = "http://" + self.host + "/" + url

            # 保存当前
            item = ArticlesItem()
            item['title'] = title
            item['url'] = url
            item['status'] = 0

            yield item
        else:

            self.log("articles的url:%s采集完毕"%response.url, level=logging.INFO)
