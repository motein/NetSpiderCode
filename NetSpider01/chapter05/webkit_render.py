'''
Created on Jun 19, 2018

@author: xiongan2
'''

from PySide2.QtWidgets import QApplication
from PySide2.QtWebEngineWidgets import QWebEngineView
import lxml.html
import chapter03.downloader


def direct_download(url):
    download = chapter03.downloader.Downloader()
    return download(url)

def webkit_download(url):
    app = QApplication([])
    webview = QWebEngineView()
    webview.loadFinished.connect(app.quit)
    webview.load(url)
    app.exec_() # delay here until download finished
    return webview.page().mainFrame().toHtml()


def parse(html):
    tree = lxml.html.fromstring(html)
    print(tree.cssselect('#results')[0].text_content())


def main(): 
    url = 'http://example.webscraping.com/dynamic'
    parse(direct_download(url))
    parse(webkit_download(url))
    return


if __name__ == '__main__':
    main()