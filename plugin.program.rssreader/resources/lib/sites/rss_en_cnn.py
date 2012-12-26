# -*- coding: utf-8 -*-

def rss_info():
    rss_info = {'sitename':'CNN', 'regexp':"<!--endclickprintexclude--><!--google_ad_section_start--><!--startclickprintinclude-->(.+?)<!--endclickprintinclude-->", 'rootlist':
        [
            {'listname':'INTERNATIONAL', 'sublist':
                [
                    {'rssname':'Top Stories', 'xml':'http://rss.cnn.com/rss/edition.rss'},
                    {'rssname':'World', 'xml':'http://rss.cnn.com/rss/edition_world.rss'},
                    {'rssname':'Africa', 'xml':'http://rss.cnn.com/rss/edition_africa.rss'},
                    {'rssname':'Americas', 'xml':'http://rss.cnn.com/rss/edition_americas.rss'},
                    {'rssname':'Asia', 'xml':'http://rss.cnn.com/rss/edition_asia.rss'},
                    {'rssname':'Europe', 'xml':'http://rss.cnn.com/rss/edition_europe.rss'},
                    {'rssname':'Middle East', 'xml':'http://rss.cnn.com/rss/edition_meast.rss'},
                    {'rssname':'U.S.', 'xml':'http://rss.cnn.com/rss/edition_us.rss'},
                    {'rssname':'World Business', 'xml':'http://rss.cnn.com/rss/edition_business.rss'},
                    {'rssname':'Technology', 'xml':'http://rss.cnn.com/rss/edition_technology.rss'},
                    {'rssname':'Science & Space', 'xml':'http://rss.cnn.com/rss/edition_space.rss'},
                    {'rssname':'Entertainment', 'xml':'http://rss.cnn.com/rss/edition_entertainment.rss'},
                    {'rssname':'World Sport', 'xml':'http://rss.cnn.com/rss/edition_sport.rss'},
                    {'rssname':'Football', 'xml':'http://rss.cnn.com/rss/edition_football.rss'},
                    {'rssname':'Golf', 'xml':'http://rss.cnn.com/rss/edition_golf.rss'},
                    {'rssname':'Motorsport', 'xml':'http://rss.cnn.com/rss/edition_motorsport.rss'},
                    {'rssname':'Tennis', 'xml':'http://rss.cnn.com/rss/edition_tennis.rss'},
                    {'rssname':'Travel', 'xml':'http://rss.cnn.com/rss/edition_travel.rss'},
                    {'rssname':'Video', 'xml':'http://rss.cnn.com/rss/cnn_freevideo.rss'},
                    {'rssname':'Most Recent', 'xml':'http://rss.cnn.com/rss/cnn_latest.rss'},
                    {'rssname':'Business 360', 'xml':'http://rss.cnn.com/rss/edition_business360.rss'},
                    {'rssname':'Connect The World', 'xml':'http://rss.cnn.com/rss/edition_connecttheworld.rss'},
                    {'rssname':'In the Field', 'xml':'http://rss.cnn.com/rss/edition_inthefield.rss'},
                    {'rssname':'Inside the Middle East', 'xml':'http://rss.cnn.com/rss/edition_ime.rss'},
                    {'rssname':'International Desk', 'xml':'http://rss.cnn.com/rss/edition_idesk.rss'},
                    {'rssname':'Prism', 'xml':'http://rss.cnn.com/rss/edition_prismblog.rss'},
                    {'rssname':'Quest Means Business', 'xml':'http://rss.cnn.com/rss/edition_questmeansbusiness.rss'},
                    {'rssname':'The Screening Room', 'xml':'http://rss.cnn.com/rss/edition_screeningroom.rss'},
                    {'rssname':'World Sport', 'xml':'http://rss.cnn.com/rss/edition_worldsportblog.rss'},
                    {'rssname':'UK Election', 'xml':'http://rss.cnn.com/rss/edition_ukelectionblog.rss'}
                ]
            },
            {'listname':'U.S.', 'sublist':
                [
                    {'rssname':'Top Stories', 'xml':'http://rss.cnn.com/rss/cnn_topstories.rss'},
                    {'rssname':'World', 'xml':'http://rss.cnn.com/rss/cnn_world.rss'},
                    {'rssname':'U.S.', 'xml':'http://rss.cnn.com/rss/cnn_us.rss'},
                    {'rssname':'Sports (SI.com)', 'xml':'http://rss.cnn.com/rss/si_topstories.rss'},
                    {'rssname':'Business (CNNMoney.com)', 'xml':'http://rss.cnn.com/rss/money_latest.rss'},
                    {'rssname':'Politics', 'xml':'http://rss.cnn.com/rss/cnn_allpolitics.rss'},
                    {'rssname':'Crime', 'xml':'http://rss.cnn.com/rss/cnn_crime.rss'},
                    {'rssname':'Technology', 'xml':'http://rss.cnn.com/rss/cnn_tech.rss'},
                    {'rssname':'Health', 'xml':'http://rss.cnn.com/rss/cnn_health.rss'},
                    {'rssname':'Entertainment', 'xml':'http://rss.cnn.com/rss/cnn_showbiz.rss'},
                    {'rssname':'Travel', 'xml':'http://rss.cnn.com/rss/cnn_travel.rss'},
                    {'rssname':'Living', 'xml':'http://rss.cnn.com/rss/cnn_living.rss'},
                    {'rssname':'Video', 'xml':'http://rss.cnn.com/rss/cnn_freevideo.rss'},
                    {'rssname':'CNN Student News', 'xml':'http://rss.cnn.com/rss/cnn_studentnews.rss'},
                    {'rssname':'Most Popular', 'xml':'http://rss.cnn.com/rss/cnn_mostpopular.rss'},
                    {'rssname':'Most Recent', 'xml':'http://rss.cnn.com/rss/cnn_latest.rss'},
                    {'rssname':'iReports on CNN', 'xml':'http://rss.ireport.com/feeds/oncnn.rss'},
                    {'rssname':'CNN.com Behind the Scenes Blog', 'xml':'http://rss.cnn.com/rss/cnn_behindthescenes.rss'}
                ]
            },
        ]
    }
    return rss_info