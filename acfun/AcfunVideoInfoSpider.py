import re
from random import random
from typing import List, Dict
import crawlertool as tool

from commons.ua_info import ua_list

"""
 @Desc      : AcFun 视频信息爬取
 @Author    : Coffee_Killer
 @Timer     : 2023_9_17
 @Version   : 1.0
 @Status    : None[未知]
"""


class AcfunVideoInfoSpider(object):

    _HEADERS = {
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25"
    }

    # 视频信息的url
    _DOWNLOAD_URL = ("https://api-new.acfunchina.com/rest/app/play/playInfo/mp4"
                     "?videoId={}"
                     "&resourceId={}"
                     "&resourceType=2"
                     "&mkey=AAHewK3eIAAyMjAzNTI2NDMAAhAAMEP1uwS3Vi7NYAAAAJumF4MyTTFh5HGoyjW6ZpdjKymALUy9jZbsMTBVx-F10EhxyvpMtGQbBCYipvkMShM3iMNwbMd9DM6r2rnOYRVEdr6MaJS4yxxlA_Sl3JNWup57qBCQzOSC7SZnbEsHTQ%3D%3D"
                     "&market=xiaomi"
                     "&product=ACFUN_APP"
                     "&sys_version=10"
                     "&app_version=6.20.0.915"
                     "&boardPlatform=sdm845"
                     "&sys_name=android"
                     "&socName=UNKNOWN"
                     "&appMode=0")

    def run(self, page_url) -> list[Dict]:
        response = tool.do_request(page_url, headers =self._HEADERS).text
        title = re.search(r"(?<=<title>)[^<]+(?=</title>)", response).group()
        video_id = re.search(r"(?<=\"vid\":\")\d+(?=\",)", response).group()
        resource_id = re.search(r"(?<=\"ac\":\")\d+(?=\",)", response).group()

        rep_info = tool.do_request(self._DOWNLOAD_URL.format(video_id, resource_id), headers =self._HEADERS)

        video_url = rep_info.json()["playInfo"]["streams"][0]["playUrls"][0]

        return [{
            "Title": title,
            "Download Url": video_url
        }]


if __name__ == "__main__":
    page_url = "https://www.acfun.cn/v/ac16986343"
    spider = AcfunVideoInfoSpider()
    print(spider.run(page_url))
