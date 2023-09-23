
"""
 @Desc      : 百度贴吧 搜索页面 HTML页面爬取
 @Author    : Coffee_Killer
 @Timer     : 2023_9_23
 @Version   : 1.0
 @Status    : None[未知]
"""
import os
import re
import ssl
import urllib.request
from urllib import error
from urllib.parse import urljoin

from bs4 import BeautifulSoup


class BaiduBaikeSpider(object):
    def __init__(self):
        self.urls = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.outer = HtmlOuter()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                count = count+1
                print("craw %d : %s" % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)


            except:
                print("craw failed")


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


ssl._create_default_https_context = ssl.create_default_context()
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


class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):

        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/item/*"))

        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):

        res_data = {}
        res_data['url'] = page_url
        soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        print(res_data['title'])

        catlog_node = soup.select('div[class="para"]')
        for content in catlog_node:
          print(content.get_text().strip())

        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            print("page_url is None")
            return
        soup = BeautifulSoup(html_cont, "html.parser", from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

class HtmlOuter(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def outer_html(self):
        f_outer = open(os.getcwd() + "\\..\\outer_files\\outer.html", "w")

        f_outer.write("<html>")
        f_outer.write("<body>")
        f_outer.write("<table>")

        for data in self.datas:
            f_outer.write("<tr>")
            f_outer.write("<td>%s</td>" % data['url'])
            f_outer.write("<td>%s</td>" % data['title'].encode('utf-8'))
            # fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            f_outer.write("</tr>")

        f_outer.write("</table>")
        f_outer.write("</body>")
        f_outer.write("</html>")
