# -*- coding: utf-8 -*-
import csv
import os
import random
import re
import time
from urllib import request

from commons.ua_info import ua_list

"""
 @Desc      : 猫眼电影 爬取排行榜 保存为csv文件
 @Author    : Coffee_Killer
 @Timer     : 2023-9-11
 @Version   : 1.0
 @Status    : Error[不可用]
"""


class MaoYanTopSpider(object):

    def __init__(self):
        self.sava_file_name = os.getcwd() + "\\..\\outer_files\\" + "maoyan_top.csv"
        self.url = 'https://www.maoyan.com/board/4?offset={}'

    # 请求页面结构
    def get_html(self, url):
        headers = {"User-Agent": random.choice(ua_list)}

        print(url)

        req = request.Request(url=url, headers=headers)
        res = request.urlopen(req)
        html = res.read("utf-8", "ignore")

        self.parse_html(html)

    # 解析HTML结构
    def parse_html(self, html):
        # 正则
        re_bds = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>'
        pattern = re.compile(re_bds, re.S)
        re_list = pattern.findall(html)
        self.save_html(re_list)

    # 保存数据
    def save_html(self, re_list):
        print(re_list)
        with open(self.sava_file_name, "a", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            for r in re_list:
                name = r[0].strip()
                star = r[1].strip()[3:]
                timer = r[2].strip()[5:15]
                line = [name, star, timer]

                writer.writerow(line)
                print("##########" + line)

    def run(self):
        for offset in range(0, 11, 10):
            url = self.url.format(offset)
            self.get_html(url)
            time.sleep(random.randint(1, 2))


if __name__ == "__main__":
    start = time.time()

    spider = MaoYanTopSpider()
    spider.run()
    # try:
    #
    # except Exception as e:
    #     print("!!!!!!!!!!! Error")
    #     print(e)

    end = time.time()
    print("爬虫执行时间 ========> %.2f" % (end - start))
