#!/usr/bin/python
# coding=gbk
import re 

import time
import urllib2
import urllib

def get_urls(url):
    html = urllib2.urlopen(url).read()
   
    picurl = re.compile(r'http://pic\.meizitu\.com/wp-content/uploads.+\.jpg')
    picts = picurl.findall(html)
    
    for urls in picts:
        try:
            print urls
            name = re.sub(':', '_', time.ctime()[10:19] + '.jpg')
            print name
            urllib.urlretrieve(urls, 'E:/Github/meizitu/tu/' + name)
        except urllib.ContentTooShortError as e:
            print name + 'failt' + e
            continue

def get_href(page):
    s = urllib2.urlopen(page)
    hrefs = re.compile(r'http://www\.meizitu\.com/a/\d+\.html')
    s = s.read()
    links = hrefs.findall(s)
    linked=links[1:10]
    return linked

def main():
    for i in xrange(1, 2):
        a = 'http://www.meizitu.com/a/list_1_%d.html' % i
        href = get_href(a)
        time.sleep(1)
        for j in href:
            get_urls(j)
if __name__ == '__main__':
    main()
