## simplyer
A simple browser.Open source and simple<br> 
## download version 1.0.0 
<a href="https://github.com/shourgamer2/simplyer/releases/download/normalinstaller/simplyer.exe">Download Normal Installer</a> <br>
<a href="https://github.com/shourgamer2/simplyer/releases/download/Portable/simplyer.exe">Download Portable  </a>
## portable
portable version is a version which can be used on a pendrive without installing just download the file move it to your pendrive and your done ! 
## Installation
```sh
python3 -m pip install git+https://github.com/shourgamer2/simplyer.git
```
## Modify
```py
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('yoursearch.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('yourwebsite.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('yourappname')
window = MainWindow()
app.exec_()
```
## Fork
If you fork this project then please mention my repo in your credits section
## Virus ?
This is not a virus it is marked as virus because it is made in python and python is not made for pc apps so don't worry it is 100% safe

