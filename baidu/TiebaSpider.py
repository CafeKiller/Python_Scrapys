import os
import random
import time
from urllib import request, parse

from commons.ua_info import ua_list


class TieBaHTMLSpider(object):
    def __init__(self):
        self.url = "http://tieba.baidu.com/f?{}"

    def get_html(self, url):
        req = request.Request(url=url, headers={"User-Agent": random.choice(ua_list)})
        res = request.urlopen(req)
        html = res.read().decode("gbk", "ignore")
        return html

    def pares_html(self):
        pass

    def sava_html(self, filename, html):

        dir_name = os.getcwd() + "\\..\\outer_files\\"
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)

        with open(dir_name + filename, "w") as f:
            f.write(html)

    def run(self):
        name = input("输出贴吧名称: ")
        begin = int(input("输出起始页页码: "))
        stop = int(input("输入终止页页码: "))

        for page in range(begin, stop + 1):
            pn = (page - 1) * 50
            params = {
                "kw": name,
                "pn": str(pn)
            }
            params = parse.urlencode(params)
            url = self.url.format(params)
            html = self.get_html(url)
            filename = "百度贴吧_{}吧 {}-{}页.html".format(name, begin, stop)
            self.sava_html(filename, html)

            print("### 爬取第%d页 抓取成功" % page)

            time.sleep(random.randint(1,2))


if __name__ == "__main__":
    start = time.time()

    spider = TieBaHTMLSpider()
    spider.run()

    end = time.time()
    print("爬虫执行时间 ========> %.2f" % (end - start))
