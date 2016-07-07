#-*-coding:utf-8-*-

'总调度程序'
from baike_spider import url_manager,html_downloader,html_parser,html_outputer

__author__ = 'Joan'


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManger()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()


    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s'%(count ,new_url)
                html_cont = self.downloader.downloader(new_url)
                new_urls,new_data = self.parser.parser(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 100:
                    break
                count = count + 1
            except:
                print 'carw failed'
        self.outputer.outputer_html()

if __name__ == "__main__":
    root_url = "http://baike.baidu.com/link?url=GRAuGlZ5mLfjDVwlS4jeNyBRQlnJF4Ff3ualANa-cjJhPFBTdsZuUMH1PpiOB-tV47CGmFokajT968-7E4U5OK"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
