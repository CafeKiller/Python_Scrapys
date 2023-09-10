import codecs
import json
import random
import time
import urllib.parse
from urllib import request
from lxml import etree

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
        output = codecs.open("_TieBa_.json", "w", encoding="utf-8")
        output.write("[" + "\n")

        for pn in range(0, 1, 1):
            kw = u"{}".format(keyword).encode("utf-8")
            url = "http://tieba.baidu.com/f?kw=" + urllib.parse.quote(kw) + '&ie=utf-8&pn=' + str(pn)
            print("#####", url)
            req = request.Request(url)
            res = request.urlopen(req)

            html = res.read().decode("utf-8", "ignore")
            # print("#######", html)

            dom = etree.HTML(html)

            # print(dom)

            for site in dom.xpath('//li[@data-field]'):

                # print("#$#$#$#$#$#$", site.xpath('//span[@class="tb_icon_author "]')[0].text())
                # _span = etree.tostring(site.xpath('//span[@class="tb_icon_author "]')[3])
                print("#$#$#$#$#$#$", str(_span, "gbk"))

                title = site.xpath('.//a')[0].text
                article_url = site.xpath('.//a')[0].attrib['href']

                # print("#$#$#$#$#$#$", article_url)

                # reply_date = self.get_timer_by_article('http://tieba.baidu.com' + article_url)
                reply_date = ""

                if len(site.xpath('.//*[@class="threadlist_abs threadlist_abs_onlyline "]')) > 1:
                    desc = site.xpath('.//*[@class="threadlist_abs threadlist_abs_onlyline "]')[0].text.strip()
                else:
                    desc = ""

                if len(site.xpath('.//*[@class="tb_icon_author"]')) > 1:
                    print("#$#$#$#$#$#$", site.xpath('.//*[@class="tb_icon_author')[0].text)
                    author = site.xpath('.//*[@class="tb_icon_author').attrib['href']
                else:
                    author = ""

                item = {
                    'title': title,
                    'author': author,
                    'desc': desc,
                    'reply_date': reply_date
                }

                # print("#########", item)

                line = json.dumps(item, ensure_ascii=False)

                output.write(line + ",\n")

        output.write("]")
        output.close()


if __name__ == "__main__":
    start = time.time()

    spider = TieBaJSONSpider()
    spider.run("海贼王")

    end = time.time()
    print("爬虫执行时间 ========> %.2f" % (end - start))
