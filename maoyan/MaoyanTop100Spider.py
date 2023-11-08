import json
import os
import random
import re
import time

import requests
from requests import RequestException

from commons.ua_info import ua_list


def get_on_page(url):
    try:
        headers = {
            "User-Agent": random.choice(ua_list)
        }
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile(
        r'<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.'
        r'*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
        re.S
    )
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1].split('@')[0],
            'title': item[2].strip(),
            'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score': item[5].strip() + item[6].strip()
        }


def write_to_file(content):
    dir_name = os.getcwd() + "\\..\\outer_files\\"
    with open(dir_name + "result.txt", 'a', encoding="utf-8") as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def save_to_mongo(item):
    pass


def main(offset):
    url = "http://maoyan.com/board/4?offset={}".format(str(offset))
    html = get_on_page(url)
    for item in parse_one_page(html):
        write_to_file(item)


if __name__ == "__main__":
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)
