# -*- coding: utf-8 -*-

def rss_info():
    rss_info = {'sitename':'新浪', 'regexp':"<!-- publish_helper name='原始正文'.*?-->(.+?)<!-- publish_helper_end -->", 'rootlist':
        [
            {'listname':'新闻中心', 'sublist':
                [
                    {'rssname':'新闻要闻', 'xml':'http://rss.sina.com.cn/news/marquee/ddt.xml'},
                    {'rssname':'国内要闻', 'xml':'http://rss.sina.com.cn/news/china/focus15.xml'},
                    {'rssname':'国际要闻', 'xml':'http://rss.sina.com.cn/news/world/focus15.xml'},
                    {'rssname':'社会新闻', 'xml':'http://rss.sina.com.cn/news/society/focus15.xml'},
                    {'rssname':'港澳台新闻', 'xml':'http://rss.sina.com.cn/news/china/hktaiwan15.xml'},
                    {'rssname':'社会与法', 'xml':'http://rss.sina.com.cn/news/society/law15.xml'},
                    {'rssname':'社会万象', 'xml':'http://rss.sina.com.cn/news/society/misc15.xml'},
                    {'rssname':'真情时刻', 'xml':'http://rss.sina.com.cn/news/society/feeling15.xml'},
                    {'rssname':'奇闻逸事', 'xml':'http://rss.sina.com.cn/news/society/wonder15.xml'}
                ]
            },
            {'listname':'科技新闻', 'sublist':
                [
                    {'rssname':'科技要闻汇总', 'xml':'http://rss.sina.com.cn/tech/rollnews.xml'},
                    {'rssname':'焦点新闻', 'xml':'http://rss.sina.com.cn/news/allnews/tech.xml'},
                    {'rssname':'互联网新闻', 'xml':'http://rss.sina.com.cn/tech/internet/home28.xml'},
                    {'rssname':'手机资讯', 'xml':'http://rss.sina.com.cn/tech/mobile/mobile_6.xml'},
                    {'rssname':'3G新闻', 'xml':'http://rss.sina.com.cn/tech/3G/guonei.xml'},
                    {'rssname':'笔记本新闻', 'xml':'http://rss.sina.com.cn/tech/notebook/193_1.xml'},
                    {'rssname':'电信新闻', 'xml':'http://rss.sina.com.cn/tech/tele/gn37.xml'},
                    {'rssname':'业界新闻', 'xml':'http://rss.sina.com.cn/tech/it/gn37.xml'},
                    {'rssname':'科技下载', 'xml':'http://rss.sina.com.cn/tech/down/down20.xml'},
                    {'rssname':'科普要闻', 'xml':'http://rss.sina.com.cn/tech/discovery/discovery.xml'},
                    {'rssname':'数码资讯', 'xml':'http://rss.sina.com.cn/tech/number/new_camera.xml'},
                    {'rssname':'家电资讯', 'xml':'http://rss.sina.com.cn/tech/elec/buy_elec.xml'}
                ]
            },
        ]
    }
    return rss_info