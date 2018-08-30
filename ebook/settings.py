# -*- coding: utf-8 -*-

# Scrapy settings for ebook project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

SCHEDULER_ORDER = 'BFO'

LOG_LEVEL = "ERROR"

# LOG_ENABLED = True
# LOG_ENCODING = 'utf-8'
# LOG_FORMATTER = 'scrapy.logformatter.LogFormatter'
# LOG_STDOUT = True
# LOG_LEVEL = 'DEBUG'
# LOG_FILE =  './debug.log'


DOWNLOAD_DELAY = 0
# Pipeline的并发数。同时最多可以有多少个Pipeline来处理item
CONCURRENT_ITEMS = 250
# 并发请求的最大数
CONCURRENT_REQUESTS = 200
# 对一个网站的最大并发数
CONCURRENT_REQUESTS_PER_DOMAIN = 180
# 对一个IP的最大并发数
CONCURRENT_REQUESTS_PER_IP = 200


BOT_NAME = 'ebook'

SPIDER_MODULES = ['ebook.spiders']
NEWSPIDER_MODULE = 'ebook.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'ebook (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True
ROBOTSTXT_OBEY = False
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 0
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'ebook.middlewares.EbookSpiderMiddleware': 543,
# }

# DOWNLOADER_MIDDLEWARES = {
#     "ebook.middlewares.UserAgentMiddleware": 400,
# }


# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'ebook.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#     'ebook.pipelines.ArticlesPipelines.ArticlesPipelines': 400,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'



SITE = {}



###=============================================
#采集dybz
SITE["dybz"] = {}
## dybz 采集的列表入口地址
SITE["dybz"]['site'] = {
    "title": "dybz",
    "url": "http://m.335xs.net/ph/week_480.html"
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


###=============================================
### 平时改这里 =================================
CURRENT_SITE_NAME = "dybz"

###=============================================

MONGO_URI = 'mongodb://localhost:27017'
MONGO_DATABASE = CURRENT_SITE_NAME

FILES_STORE = 'novel'
FEED_EXPORT_ENCODING = 'gbk'


