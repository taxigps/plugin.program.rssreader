# -*- coding: utf-8 -*-
import xbmc, xbmcaddon, xbmcplugin, xbmcgui
import urllib,urllib2,re,os,string
from xml.dom import minidom

# Script constants
__addon__     = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('name')
__cwd__       = xbmc.translatePath(__addon__.getAddonInfo('path')).decode("utf-8")
__profile__   = xbmc.translatePath(__addon__.getAddonInfo('profile')).decode("utf-8")
__language__  = __addon__.getLocalizedString

# Shared resources
BASE_RESOURCE_PATH =  os.path.join(__cwd__, 'resources', 'lib')
RSS_SITE_DIR = os.path.join(__cwd__, "resources", "lib", "sites")
sys.path.append (BASE_RESOURCE_PATH)

RSS_LIST = []
for item in os.listdir(RSS_SITE_DIR):
    if item[:4] == 'rss_' and item[-3:] == '.py':
        filename = item[:-3]
        exec ( "from sites import %s" % (filename))
        exec ( "RSS_LIST.append(%s.rss_info())" % (filename))

class GUI( xbmcgui.WindowXMLDialog ):
    # Constants
    ACTION_EXIT_SCRIPT = ( 9, 10, )

    def __init__( self, *args, **kwargs ):
        # Show dialog window...
        xbmcgui.WindowXML.__init__( self )

        # File parameter
        self.title = kwargs[ "info" ]
        self.cont = kwargs[ "text" ]

    def onInit( self ):
        self.getControl( 4 ).setLabel("[B]" +self.title + "[/B]")
        self.getControl( 30 ).setText(self.cont)

    def onFocus( self, controlId ):
        pass

    def onAction( self, action ):
        if ( action in self.ACTION_EXIT_SCRIPT ):
            # File changed, save?
            # Close window...
            self.close()
        if ( action == 4 ):
            xbmc.executebuiltin('XBMC.PageDown(61)')
        if ( action == 3 ):
            xbmc.executebuiltin('XBMC.PageUp(61)')

    def onClick( self, controlId ):
        pass

def GetHttpData(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
    try:
        response = urllib2.urlopen(req)
        httpdata = response.read()
        if response.headers.get('content-encoding', None) == 'gzip':
            httpdata = gzip.GzipFile(fileobj=StringIO.StringIO(httpdata)).read()
        charset = response.headers.getparam('charset')
        response.close()
    except:
        print 'GetHttpData Error: %s' % url
        return ''
    match = re.compile('<meta http-equiv=["]?[Cc]ontent-[Tt]ype["]? content="text/html;[\s]?charset=(.+?)"').findall(httpdata)
    if len(match)>0:
        charset = match[0]
    if charset:
        charset = charset.lower()
        if (charset != 'utf-8') and (charset != 'utf8'):
            httpdata = httpdata.decode(charset, 'ignore').encode('utf8', 'ignore')
    return httpdata

def siteList():
    i = 0
    for site in RSS_LIST:
        i += 1
        sitename = site['sitename']
        li=xbmcgui.ListItem(str(i) + '. ' + sitename)
        u=sys.argv[0]+"?mode=1&sitename="+urllib.quote_plus(sitename)
        xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def rootList(sitename):
    for site in RSS_LIST:
        if sitename == site['sitename']:
            i = 0
            for item in site['rootlist']:
                i += 1
                listname = item['listname']
                li=xbmcgui.ListItem(str(i) + '. ' + listname)
                u=sys.argv[0]+"?mode=2&sitename="+urllib.quote_plus(sitename)+"&listname="+urllib.quote_plus(listname)
                xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
            xbmcplugin.endOfDirectory(int(sys.argv[1]))
            return

def subList(sitename, listname):
    for site in RSS_LIST:
        if sitename == site['sitename']:
            regexp = site['regexp']
            for item in site['rootlist']:
                if listname == item['listname']:
                    i = 0
                    for rss in item['sublist']:
                        i += 1
                        rssname = rss['rssname']
                        url = rss['xml']
                        li=xbmcgui.ListItem(str(i) + '. ' + rssname)
                        u=sys.argv[0]+"?mode=3&url="+urllib.quote_plus(url)+"&regexp="+urllib.quote_plus(regexp)
                        xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
                    xbmcplugin.endOfDirectory(int(sys.argv[1]))
                    return

def getTagText(root, tag):
    node = root.getElementsByTagName(tag)[0]
    rc = ""
    for node in node.childNodes:
        if node.nodeType in ( node.TEXT_NODE, node.CDATA_SECTION_NODE):
            rc = rc + node.data
    return rc

def INDEX(url,regexp):
    link = GetHttpData(url)
    dom = minidom.parseString(link)
    root = dom.documentElement
    items = root.getElementsByTagName('item')
    i = 0
    for item in items:
        i += 1
        name = getTagText(item, 'title').encode('utf-8').strip()
        url = getTagText(item, 'link').encode('utf-8').strip()
        li=xbmcgui.ListItem(str(i) + '. ' + name)
        u=sys.argv[0]+"?mode=4&url="+urllib.quote_plus(url)+"&regexp="+urllib.quote_plus(regexp)+"&name="+urllib.quote_plus(name)
        xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,False)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def RSSLINKS(url,name,regexp):
    link = GetHttpData(url).replace('\n','').replace('\r','')
    match=re.compile(regexp, re.DOTALL).findall(link)
    if (len(match) > 0):
        cont=re.sub('</p>','\n', match[0])
        cont=re.sub('</P>','\n', cont)
        cont=re.sub('<style(.+?)</style>','', cont)
        cont=re.sub('<script(.+?)</script>','', cont)
        cont=re.sub('&nbsp;',' ', cont)
        cont=re.sub('\t',' ', cont)
        cont=re.sub('<.+?>','', cont)
        mydisplay = GUI( "script-RSSReader.xml", __cwd__, "Default", info=name, text=cont)
        mydisplay.doModal()
        del mydisplay
    else:
        dialog = xbmcgui.Dialog()
        dialog.ok(__addonname__, '解析页面出错。')

def get_params():
    param=[]
    paramstring=sys.argv[2]
    if len(paramstring)>=2:
        params=sys.argv[2]
        cleanedparams=params.replace('?','')
        if (params[len(params)-1]=='/'):
            params=params[0:len(params)-2]
        pairsofparams=cleanedparams.split('&')
        param={}
        for i in range(len(pairsofparams)):
            splitparams={}
            splitparams=pairsofparams[i].split('=')
            if (len(splitparams))==2:
                param[splitparams[0]]=splitparams[1]
    return param

params = get_params()
sitename = None
listname = None
name = None
url = None
mode = None
regexp = None

try:
    sitename = urllib.unquote_plus(params["sitename"])
except:
    pass
try:
    listname = urllib.unquote_plus(params["listname"])
except:
    pass
try:
    name = urllib.unquote_plus(params["name"])
except:
    pass
try:
    url = urllib.unquote_plus(params["url"])
except:
    pass
try:
    mode = int(params["mode"])
except:
    pass
try:
    regexp = urllib.unquote_plus(params["regexp"])
except:
    pass

if mode == None:
    siteList()
elif mode == 1:
    rootList(sitename)
elif mode == 2:
    subList(sitename, listname)
elif mode == 3:
    INDEX(url, regexp)
elif mode == 4:
    RSSLINKS(url, name, regexp)
