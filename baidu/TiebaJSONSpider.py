import codecs
import json
import os
import random
import time
import urllib.parse
from urllib import request
from lxml import etree

from bs4 import BeautifulSoup

from commons.ua_info import ua_list

"""
 @Desc      : 百度贴吧 搜索页面 JSON数据获取, 注意: 贴吧具有反爬取机制, 过度爬取会失效
 @Author    : Coffee_Killer
 @Timer     : 2023_9_10
 @Version   : 2.0
 @Status    : Usable[可用]
"""


class TieBaJSONSpider(object):

    # 呼气帖子的发布时间
    def get_timer_by_article(self, url):

        req = request.Request(url=url, headers={"User-Agent": random.choice(ua_list)})
        res = request.urlopen(req)

        html = res.read().decode("utf-8", "ignore")
        dom = BeautifulSoup(html, features="lxml")

        if len(dom.select("span.tail-info")) < 4:
            timer = dom.select("span.tail-info")[2].get_text()
        else:
            timer = "NULL"

        return timer

    def run(self, keyword):
        output = codecs.open(os.getcwd() + "\\..\\outer_files\\" + "_TieBa_.json", "w", encoding="utf-8")
        output.write("[" + "\n")

        for pn in range(0, 1, 1):

            kw = u"{}".format(keyword).encode("utf-8")
            url = "http://tieba.baidu.com/f?kw=" + urllib.parse.quote(kw) + '&ie=utf-8&pn=' + str(pn)

            req = request.Request(url)
            res = request.urlopen(req)
            html = res.read().decode("utf-8", "ignore")

            dom = BeautifulSoup(html, features="lxml")

            last_len = len(dom.select("li.j_thread_list.thread_item_box")) - 1
            for site in dom.select("li.j_thread_list.thread_item_box"):

                # 获取帖子的标题
                title = site.select_one("a.j_th_tit").get_text()

                # 获取帖子的链接
                article_url = "https://tieba.baidu.com/" + site.select_one("a.j_th_tit").attrs['href']

                # 获取帖子的发布时间, 此时需要对帖子进行二次爬取, 速度较慢
                # 可以选择不选择爬取, 提升爬取速度
                # reply_timer = self.get_timer_by_article(article_url)
                reply_timer = ""

                # 获取发帖者昵称
                if len(site.select_one("span.frs-author-name-wrap").get_text()) > 1:
                    author = site.select_one("span.frs-author-name-wrap").get_text()
                else:
                    author = "NULL"

                # 获取帖子的简述内容
                if site.select_one("div.threadlist_abs.threadlist_abs_onlyline") is not None:
                    desc = site.select_one("div.threadlist_abs.threadlist_abs_onlyline").get_text()
                else:
                    desc = "NULL"

                # 合成对象
                item = {
                    'title': title,
                    'author': author,
                    'desc': desc,
                    'article_url': article_url,
                    'reply_timer': reply_timer
                }

                line = json.dumps(item, ensure_ascii=False)

                # 判断是否是最后一条数据
                if site == dom.select("li.j_thread_list.thread_item_box")[last_len]:
                    output.write(line + "\n")
                else:
                    output.write(line + ",\n")

                print("############## 爬取成功 休眠1~2秒")
                # time.sleep(random.randint(1, 2))

        output.write("]")
        output.close()


if __name__ == "__main__":
    start = time.time()

    spider = TieBaJSONSpider()
    spider.run("海贼王")

    end = time.time()
    print("爬虫执行时间 ========> %.2f" % (end - start))
