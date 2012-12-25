# -*- coding: utf-8 -*-

def rss_info():
    rss_info = {'sitename':'网易', 'regexp':'<div id=\"endText\">(.+?)<a href=\"http://news.163.com/\">', 'rootlist':
        [
            {'listname':'新闻', 'sublist':
                [
                    {'rssname':'头条新闻', 'xml':'http://news.163.com/special/00011K6L/rss_newstop.xml'},
                    {'rssname':'国内新闻', 'xml':'http://news.163.com/special/00011K6L/rss_gn.xml'},
                    {'rssname':'国际新闻', 'xml':'http://news.163.com/special/00011K6L/rss_gj.xml'},
                    {'rssname':'社会新闻', 'xml':'http://news.163.com/special/00011K6L/rss_sh.xml'},
                    {'rssname':'军事新闻', 'xml':'http://news.163.com/special/00011K6L/rss_war.xml'},
                    {'rssname':'深度新闻', 'xml':'http://news.163.com/special/00011K6L/rss_hotnews.xml'},
                    {'rssname':'评论新闻', 'xml':'http://news.163.com/special/00011K6L/rss_newsspecial.xml'},
                    {'rssname':'图片新闻', 'xml':'http://news.163.com/special/00011K6L/rss_photo.xml'},
                    {'rssname':'探索新闻', 'xml':'http://news.163.com/special/00011K6L/rss_discovery.xml'}
                ]
            },
            {'listname':'科技', 'sublist':
                [
                    {'rssname':'科技头条', 'xml':'http://tech.163.com/special/000944OI/headlines.xml'},
                    {'rssname':'互联网', 'xml':'http://tech.163.com/special/000944OI/hulianwang.xml'},
                    {'rssname':'要闻', 'xml':'http://tech.163.com/special/000944OI/yaowen.xml'},
                    {'rssname':'通信', 'xml':'http://tech.163.com/special/000944OI/kejitongxin.xml'},
                    {'rssname':'IT业界', 'xml':'http://tech.163.com/special/000944OI/kejiyejie.xml'},
                    {'rssname':'视频', 'xml':'http://tech.163.com/special/000944OI/kejishipin.xml'},
                    {'rssname':'深度阅读', 'xml':'http://tech.163.com/special/000944OI/shenduyuedu.xml'},
                    {'rssname':'高端访谈', 'xml':'http://tech.163.com/special/000944OI/kejifangtan.xml'},
                    {'rssname':'IT碰碰车', 'xml':'http://tech.163.com/special/000944OI/ITpengpengche.xml'},
                    {'rssname':'专题', 'xml':'http://tech.163.com/special/000944OI/kejizhuanti.xml'}
                ]
            },
        ]
    }
    return rss_info