'''
Created on Jun 19, 2018

@author: xiongan2
'''
from PySide2.QtWidgets import QApplication
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtCore import QUrl, QEventLoop, QTimer
import lxml.html
import chapter03.downloader

def main():
    app = QApplication([])
    webview = QWebEngineView()
    loop = QEventLoop()
    webview.loadFinished.connect(loop.quit)
    webview.load(QUrl('http://example.webscraping.com/places/default/search'))
    loop.exec_()

    webview.show()
    frame = webview.page().mainFrame()
    frame.findFirstElement('#search_term').setAttribute('value', '.')
    frame.findFirstElement('#page_size option:checked').setPlainText('1000')
    frame.findFirstElement('#search').evaluateJavaScript('this.click()')

    elements = None
    while not elements:
        app.processEvents()
        elements = frame.findAllElements('#results a')
    countries = [e.toPlainText().strip() for e in elements]
    print(countries)


if __name__ == '__main__':
    main()