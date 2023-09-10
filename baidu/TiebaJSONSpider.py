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
 @Desc      : 百度贴吧 搜索页面 JSON数据获取
 @Author    : Coffee_Killer
 @Timer     : 2023_9_10
 @Version   : 1.0
 @Status    : Error[不可用]
"""


class TieBaJSONSpider(object):

    def get_timer_by_article(self, url):
        req = request.Request(url=url, headers={"User-Agent": random.choice(ua_list)})
        res = request.urlopen(req)

        html = res.read().decode("utf-8", "ignore")
        dom = etree.HTML(html)
        dom.xpath('//span[@class="threadlist_title pull_left j_th_tit "]')[0].text
        print(time)
        return time

    def run(self, keyword):
        output = codecs.open(os.getcwd() + "\\..\\outer_files\\" + "_TieBa_.json", "w", encoding="utf-8")
        output.write("[" + "\n")

        for pn in range(0, 1, 1):
            kw = u"{}".format(keyword).encode("utf-8")
            url = "http://tieba.baidu.com/f?kw=" + urllib.parse.quote(kw) + '&ie=utf-8&pn=' + str(pn)

            print("##### run.for", url)

            req = request.Request(url)
            res = request.urlopen(req)

            html = res.read().decode("utf-8", "ignore")

            doc = BeautifulSoup(html, features="lxml")

            last_len = len(doc.select("li.j_thread_list.thread_item_box")) - 1
            for site in doc.select("li.j_thread_list.thread_item_box"):

                title = site.select_one("a.j_th_tit").get_text()

                article_url = "https://tieba.baidu.com/" + site.select_one("a.j_th_tit").attrs['href']

                # reply_date = self.get_timer_by_article('http://tieba.baidu.com' + article_url)
                reply_date = ""

                if len(site.select_one("span.frs-author-name-wrap").get_text()) > 1:
                    author = site.select_one("span.frs-author-name-wrap").get_text()
                else:
                    author = "NULL"

                # print(site.select_one("div.threadlist_abs.threadlist_abs_onlyline"))
                if site.select_one("div.threadlist_abs.threadlist_abs_onlyline") is not None:
                    desc = site.select_one("div.threadlist_abs.threadlist_abs_onlyline").get_text()
                else:
                    desc = "NULL"

                item = {
                    'title': title,
                    'author': author,
                    'desc': desc,
                    'article_url': article_url,
                    'reply_date': reply_date
                }

                line = json.dumps(item, ensure_ascii=False)

                if site == doc.select("li.j_thread_list.thread_item_box")[last_len]:
                    output.write(line + "\n")
                else:
                    output.write(line + ",\n")

        output.write("]")
        output.close()


if __name__ == "__main__":
    start = time.time()

    spider = TieBaJSONSpider()
    spider.run("海贼王")

    end = time.time()
    print("爬虫执行时间 ========> %.2f" % (end - start))
