import random
import re
import time
from urllib import request

from commons.ua_info import ua_list

"""
 @Desc      : 猫眼电影
 @Author    : Coffee_Killer
 @Timer     : 2023-9-11
 @Version   : 1.0
 @Status    : None[未知]
"""


class MaoYanTopSpider(object):

    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.parse_html = None

    # 请求页面结构
    def get_html(self, url):
        header = {"User-Agent" : random.choice(ua_list)}
        req = request.Request(url=url, header=header)
        res = request.urlopen(req)
        html = res.read().decode()

        self.parse_html = html

    # 解析HTML结构
    def parse_html(self, html):
        # 正则
        re_bds = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>'
        pattern = re.compile(re_bds, re.S)
        r_list = pattern.findall(html)


    def run(self):
        pass


if __name__ == "__main__":
    start = time.time()

    end = time.time()
    print("爬虫执行时间 ========> %.2f" % (end - start))
