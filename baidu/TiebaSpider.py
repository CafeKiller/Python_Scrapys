import random
import time
from urllib import request

from commons.ua_info import ua_list


class TieBaSpider(object):
    def __init__(self):
        self.url = "http://tieba.baidu.com/f?{}"

    def get_html(self, url):
        req = request.Request(url=url, headers={"User-Agent": random.choice(ua_list)})
        res = request.urlopen(req)
        html = res.read().decode("gbk","ignore")
        return html

    def pares_html(self):
        pass

    def sava_html(self, fileName, html):
        with open(fileName, "w") as f:
            f.write(html)

    def run(self):
        name = input("输出贴吧名称: ")
        begin = int(input("输出起始页页码: "))
        stop = int(input("输入终止页页码: "))

        for page in range(begin, stop +1):
            pn = (page-1)*50
            parser = {
                "kw": name,
                "pn": str(pn)
            }


if __name__ == "__main__":
    start = time.time()

    end = time.time()

    print("爬虫执行时间 ========> %.2f" % (end - start))
