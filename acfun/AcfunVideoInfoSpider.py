
import crawlertool as tool
"""
 @Desc      : AcFun 视频信息爬取
 @Author    : Coffee_Killer
 @Timer     : 2023_9_17
 @Version   : 1.0
 @Status    : None[未知]
"""

class AcfunVideoInfoSpider(object):

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

    def run(self):
        tool


if __name__ == "__main__":
    spider = AcfunVideoInfoSpider()
    spider.run()
