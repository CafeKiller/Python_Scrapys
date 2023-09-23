

"""
 @Desc      : 百度贴吧 搜索页面 HTML页面爬取
 @Author    : Coffee_Killer
 @Timer     : 2023_9_23
 @Version   : 1.0
 @Status    : None[未知]
"""

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
