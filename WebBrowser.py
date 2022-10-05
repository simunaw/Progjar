from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import requests
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

#mengguakan library request python, beuty soup

#meggunakan library 

hostName = "localhost"
serverPort = 8000


class MyWebBrowser ():

    def __init__(self) :
       
        self.window = QWidget()
        self.window.setWindowTitle("Simple Web Browser")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)

        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(30)

        self.back_btn = QPushButton("<")
        self.back_btn.setMinimumHeight(30)

        self.forward_btn = QPushButton(">")
        self.forward_btn.setMinimumHeight(30)

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)

        self.browser = QWebEngineView()

        self.go_btn.clicked.connect(lambda: self.navigator(self.url_bar.toPlainText))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("http://google.com"))

        self.window.setLayout(self.layout)
        self.window.show()

        def navigate(self, url):
            if not url.startswith("http"):
                url = "http://" + url
                self.url_bar.setText(url)
            self.browser.setUrl(QUrl(url))

app = QApplication([])
window = MyWebBrowser()
app.exec_()


