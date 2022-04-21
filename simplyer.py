import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from requests import get, request
from tkinter import * 
from tkinter import messagebox
from requests import *
import urllib.request
import subprocess


latestversion = get('https://shourgamer2.tk/simplyer/version.txt').text
download = "https://github.com/shourgamer2/simplyer/releases/download/updater/update.exe"
version = "1.1.1"


filename = 'update.exe'  


if (latestversion.strip() == version):
    print("You are on the latest version")
  
    
else:
    messagebox.showinfo("Version outdated", "This version is outdated ! We have downloaded the latest setup for you all you have to do is uninstall this version and install the latest one which we downloaded and opened for you")
    urllib.request.urlretrieve(download, filename) 
    subprocess.call('update.exe')


    
  
         
      
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
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
        self.browser.setUrl(QUrl('https://github.com/shourgamer2/simplyer'))

 

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('simplyer')


window = MainWindow()
app.exec_()