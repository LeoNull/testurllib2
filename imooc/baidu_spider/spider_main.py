#coding:utf-8
from baidu_spider import url_manager, html_downloader, html_outputer


class SpiderMain(object):
    
    def _init_(self):
        self.urls=url_manager.__name__
        self.downloader=html_downloader.__name__
        self.parser=html_outputer.__name__
        
    def crawl(self, root_url):
        pass
    
    



if _name_=="_main_":
    root_url="http://baike.baidu.com/view/21087.htm"
    obj_spider=SpiderMain()
    obj_spider.crawl(root_url)
