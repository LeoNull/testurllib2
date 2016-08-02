#!/usr/bin/python
# coding=gbk
import re 

import time
import urllib2
import urllib
import socket

def get_urls(url):
    headers={'User-agent' : 'Mozilla/5.0'}
    rep=urllib2.Request(url,None,headers)
    try:
        timeout = 20
        socket.setdefaulttimeout(timeout)#这里对整个socket层设置超时时间。后续文件中如果再使用到socket，不必再设置
        sleep_download_time = 2
        time.sleep(sleep_download_time) 
        request = urllib2.urlopen(rep)#这里是要读取内容的url
        html = request.read()#读取，一般会在这里报异常
        request.close()#记得要关闭#这里时间自己设定
    except UnicodeDecodeError as e:

        print('-----UnicodeDecodeErrorurl:',url)

                
                
    picurl = re.compile(r'http://pic\.meizitu\.com/wp-content/uploads.+\.jpg')
    
    picts = picurl.findall(html)
    
    for urls in picts:
        try:
            print urls
            name = re.sub(':', '_', time.ctime()[10:19] + '.jpg')
            print name
            urllib.urlretrieve(urls, 'E:/meizitu/' + name)
        except urllib.ContentTooShortError as e:
            print name + 'failt' + e
            continue

def get_href(page):
    headers={'User-agent' : 'Mozilla/5.0'}
    rep=urllib2.Request(page,None,headers)

    s = urllib2.urlopen(rep)
    hrefs = re.compile(r'http://www\.meizitu\.com/a/\d+\.html')
    s = s.read()
    links = hrefs.findall(s)
    linked=links[1:10]
    return linked

def main():
    for i in xrange(1,2):
        a = 'http://www.meizitu.com/a/list_1_%d.html' % i
        href = get_href(a)
        time.sleep(1)
        for j in href:
            get_urls(j)
if __name__ == '__main__':
    main()
