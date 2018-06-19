'''
Created on Jun 19, 2018

@author: xiongan2
'''
import sys
import random
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QUrl, QCoreApplication
from PySide2 import QtWidgets, QtGui
from PySide2.QtWebEngineWidgets import QWebEngineView

def test():
    url = 'https://github.com/tody411/PyIntroduction'

    #QCoreApplication.setAttribute()
    app = QApplication(sys.argv)
    browser = QWebEngineView()
    browser.load(QUrl(url))
    browser.resize(1024, 750)
    browser.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    test()