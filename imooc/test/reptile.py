#!/usr/bin/python
# coding=utf-8
import re 
import os
import time
import urllib2
import urllib

def get_urls(url):
    html = urllib2.urlopen(url).read()
    picurl = re.compile(r'<img alt=".+?" src="(.+?)" /><br />')
    picts = picurl.findall(html)
    for urls in picts:
        try:
            name = re.sub(':', '_', time.ctime()[10:19] + '.jpg')
            print name
            urllib.urlretrieve(urls, 'E:/Github/meizitu/tu/' + name)
        except urllib.ContentTooShortError as e:
            print name + 'failt' + e
            continue

def get_href(page):
    s = urllib2.urlopen(page)
    hrefs = re.compile(r'<h2><a href="(.+?)".+?</a></h2>')
    s = s.read()
    links = hrefs.findall(s)
    return links

def main():
    for i in xrange(1, 67):
        a = 'http://www.meizitu.com/a/list_1_%d.html' % i
        href = get_href(a)
        time.sleep(1)
        for j in href:
            get_urls(j)
if __name__ == '__main__':
    os.chdir('E:/Github/meizitu/tu/') 
    main()
