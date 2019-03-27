import time,random
from selenium import webdriver         #无界面浏览器
from scrapy.http import HtmlResponse   #封装
from scrapy.conf import settings      #代理Ip
from fake_useragent import UserAgent  #伪装浏览器
class MyprojectDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    # def __init__(self):
    #     self.ua=UserAgent()
    def process_request(self, request, spider):
    #     #伪装浏览器head
    #     ua = self.ua.random
    #     request.headers.setdefault(ua)
    #     # 代理ip
    #     proxies = settings.get('PROXIES')
    #     proxy = random.choice(proxies)
    #     request.meta['proxies'] = proxy['host']

        # 自定义请求方式
        # if request.meta.get('tencent',False):
        # 这里路径是我本地路径
        driver = webdriver.PhantomJS(executable_path=r"C:\Users\Administrator\Desktop\爬虫\phantomjs-2.1.1-windows\bin\phantomjs.exe")
        driver.get(request.url)
        time.sleep(1)
        content = driver.page_source
        return HtmlResponse(url = request.url,body = content,encoding='utf-8',request = request)
