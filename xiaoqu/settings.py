# -*- coding: utf-8 -*-

# Scrapy settings for xiaoqu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xiaoqu'

SPIDER_MODULES = ['xiaoqu.spiders']
NEWSPIDER_MODULE = 'xiaoqu.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 100

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 100
CONCURRENT_REQUESTS_PER_IP = 100

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'xiaoqu.middlewares.XiaoquSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'xiaoqu.middlewares.XiaoquDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'xiaoqu.pipelines.XiaoquPipeline': 300,
    'xiaoqu.pipelines.ExcelPipeline': 301,
    #'xiaoqu.pipelines.MysqlPipeline': 302,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '__customer_trace_id=B8D70080-5CA9-45D9-995E-F3DAB0EC0D1E; PHPSESSID=4qipinajmn8q9pvmkdcfpp3fh1; Hm_lvt_c07a5cf91cdac070faa1e701f45995a8=1577343206,1577347508; AGL_USER_ID=e79f0249-d96f-4a98-837a-398d4bb287b8; Hm_lvt_15e5e51b14c8efd1f1488ea51faa1172=1577347593,1577347761,1577771483,1578894243; loadDomain=http%3A%2F%2Fsz.loupan.com%2F; Hm_lvt_2c0f8f2133c1fc1d09538a565dd8d6c8=1577343206,1577347508,1579223144; Hm_lpvt_15e5e51b14c8efd1f1488ea51faa1172=1579240756; loupan_user_session=a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22622161d9507e199454d3eb844eb97b5d%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A13%3A%22121.15.170.60%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A115%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F78.0.3904.108+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1579241140%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7Dd2512f1f510eeb07c62f3db5e3ee5796; Hm_lpvt_2c0f8f2133c1fc1d09538a565dd8d6c8=1579241158; Hm_lpvt_c07a5cf91cdac070faa1e701f45995a8=1579241159',
    'Host': 'sz.loupan.com',
    'Upgrade-Insecure-Requests': 1,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
#LOG_LEVEL = 'INFO'
RETRY_ENABLED = False
#DOWNLOAD_TIMEOUT = 10

MYSQL_HOST = 'localhost'
MYSQL_DATABASE = 'community'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_PORT = 3306
