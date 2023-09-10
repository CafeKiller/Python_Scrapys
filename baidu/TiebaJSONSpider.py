import codecs
import random
import time
from urllib import request
from lxml import etree

from commons.ua_info import ua_list

"""
 @Desc      : 百度贴吧 搜索页面 JSON数据获取
 @Author    : Coffee_Killer
 @Timer     : 2023_9_10
 @Version   : 1.0
 @Status    : None[未知]
"""


class TieBaJSONSpider(object):

    def get_timer_by_article(self, url):
        req = request.Request(url=url, headers={"User-Agent": random.choice(ua_list)})
        res = request.urlopen(req)
        html = res.read()
        dom = etree.HTML(html)
        dom.xpath('//span[@class="tail-info"]')[0].text
        print(time)
        return time


    def run(self):
        codecs.open("", "w", encoding="utf-8")


if __name__ == "__main__":
    start = time.time()

    spider = TieBaJSONSpider()
    spider.run()

    end = time.time()
    print("爬虫执行时间 ========> %.2f" % (end - start))
