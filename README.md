# Python_Scrapys 

Python 爬虫集合  
CoffeeKiller出品，古法编程，无AI，纯手敲，天然又健康  
整理一些自己编写的爬虫脚本，不过爬虫都是具有时效性的，时间一长可能很多就没用了


## 贡献者
| Name          | JoinTime   | Status |
|:--------------|:-----------|:-------|
| Coffee_Killer | 2023_09_10 | 持续输出中  |


## 技术栈
| LibraryName    | Version | Description   | pip command                |
|:---------------|:--------|:--------------|:---------------------------|
| Python         | 3.10.11 |               |                            |
| lxml           | 4.9.3   | 处理ElementTree | pip install lxml           |
| Beautiful Soup | 4.12.1  | HTML数据提取      | pip install beautifulsoup4 |
| crawlertool    | 0.1.28  | 爬虫工具集合        | pip install crawlertool    |


## 文件说明
``` 
├── common -- 通用资源

├── baidu -- 百度相关
    ├── TiebaHTMLSpider -- 贴吧: HTML页面
    ├── TiebaJSONSpider -- 贴吧: HTML转为JSON数据
    ├──
├── bilibili -- B站相关
    ├──
├── acfun -- A站相关
    ├── AcfunVideoInfoSpider -- A站视频信息获取
```

## 声明

爬虫有风险, 使用需谨慎  
你这是违法行为请跟我去自首(doge

``` 
数据爬虫技术的合法使用边界: 
    一是合法的网络数据爬取应限于对开放数据的获取。如果网络爬虫获取非开放的数据，便涉嫌违法甚至犯罪；
    二是合法使用的数据爬虫技术不应具有侵入性，可以说，爬虫的侵入性是其违法性的主要体现；
    三是数据爬取应当基于正当目的，对开放数据的获取可能因不符合正当目的而具有违法性。
```