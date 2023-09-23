

"""
 @Desc      : 百度贴吧 搜索页面 HTML页面爬取
 @Author    : Coffee_Killer
 @Timer     : 2023_9_23
 @Version   : 1.0
 @Status    : None[未知]
"""
import urllib.request
from urllib import error


class BaiduBaikeSpider(object):
    def __init__(self):


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            print("url is None")
            return None
        try:
            response = urllib.request.urlopen(url, timeout=30)
            if response.getcode() != 200:
                print("failed")
                return None
            print("success")
        except error.URLError as e:
            print(e.reason)
        print(response.read())
        return response.read()

