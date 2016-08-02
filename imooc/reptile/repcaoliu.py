#!/usr/bin/python
# coding=gbk
import re 
import time
import urllib2
import urllib

def get_urls(url):
    urlhead='http://www.t66y.com/'
    newurl=urlhead+url
    proxy = "9.0.153.11:3128"

    proxies = {"http":"http://%s" % proxy}
    url = newurl
    headers={'User-agent' : 'Mozilla/5.0'}

    proxy_support = urllib2.ProxyHandler(proxies)
    opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler(debuglevel=1))
    urllib2.install_opener(opener)
    req = urllib2.Request(url, None, headers)
    
    html = urllib2.urlopen(req).read()
    time.sleep(1)
    picurl = re.compile(r'http://funkyimg\.com/i/.+\.jpg')
    picts = picurl.findall(html)
    
    for urls in picts:
        try:
            name = re.sub(':', '_', time.ctime()[10:19] + '.jpg')
            print name
            urllib.urlretrieve(urls, 'E:/Github/meizitu/caoliu/' + name)
            time.sleep(1)
        except urllib.ContentTooShortError as e:
            print name + 'failt' + e
            continue

def get_href(page):
    #proxy_support = urllib2.ProxyHandler({"http":"http://9.0.153.11:3128"})
    #opener = urllib2.build_opener(proxy_support)
    #urllib2.install_opener(opener)
    proxy = "9.0.153.11:3128"

    proxies = {"http":"http://%s" % proxy}
    url = page
    headers={'User-agent' : 'Mozilla/5.0'}

    proxy_support = urllib2.ProxyHandler(proxies)
    opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler(debuglevel=1))
    urllib2.install_opener(opener)
    req = urllib2.Request(url, None, headers)
    s = urllib2.urlopen(req).read()
    time.sleep(1)
    hrefs = re.compile(r'htm_data/2/1608/\d+\.html')
    links = hrefs.findall(s)
    linked = links[1:15]
    
    return linked

def main():
   
    a = 'http://www.t66y.com/thread0806.php?fid=2'
    
    href = get_href(a)
 
  
    time.sleep(1)
    for j in href:
        get_urls(j)
        time.sleep(1)
if __name__ == '__main__':
    main()
