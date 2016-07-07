import urllib2

__author__ = 'Joan'


class HtmlDownloader(object):
    def downloader(self, url):
        if url is None:
            return
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()