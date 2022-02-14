## Simplyer
A simple browser.Open source and simple.This browser is made using python.It is very easy to make your own version ! Please read the whole markdown.<br> 
## Download version 1.1.0
<a href="https://github.com/shourgamer2/simplyer/releases/download/normalinstallerv1.1.0/Simplyer_Setup_Version_1.1.0.exe">Download Normal Installer</a> <br>
<a href="https://github.com/shourgamer2/simplyer/releases/download/porable1.1.0/simplyer.exe">Download Portable  </a>
## Download version 1.0.0 
<a href="https://github.com/shourgamer2/simplyer/releases/download/normalinstaller/simplyer.exe">Download Normal Installer</a> <br>
<a href="https://github.com/shourgamer2/simplyer/releases/download/Portable/simplyer.exe">Download Portable  </a>
## portable
portable version is a version which can be used on a pendrive without installing just download the file move it to your pendrive and your done ! 
## Copy
Fork the repo by clicking on the fork button
## All the packages needed
Install these packages to modify and make your own version of simplyer <br>
PyQtWebEngine
``` sh
pip install PyQtWebEngine
```
PyQt5
``` sh
pip install PyQt5
```
## Modify
Change the deafult search
```py
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('yoursearch.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
      
  ```
  Change the home url
  ```py
      def navigate_home(self):
        self.browser.setUrl(QUrl('yourwebsite.com'))
```
Change the app name 
  ```py
app = QApplication(sys.argv)
QApplication.setApplicationName('yourappname')
window = MainWindow()
app.exec_()
```
Edit the navbar
```py
 # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

      

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back) # gets back to the previous url
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward) # moves to the next url
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload) # realods the current page
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home) # goes to the home 
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url) # goes to the url
        navbar.addWidget(self.url_bar) 

        self.browser.urlChanged.connect(self.update_url) # updates the url
```
Edit and add more pages
```py 
def navigate_home(self):
        self.browser.setUrl(QUrl('YourHome.com')) #The home

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url)) #Used To Update The Url 

    def update_url(self, q):
        self.url_bar.setText(q.toString()) #Used To Update The Url 
   ```
## If you copy
If you fork this project then please mention my repo in your credits section <br>
Read the whole markdown if you want to make your own version. <br>
Also check out 
<a href="https://github.com/shourgamer2/simplyer#all-the-packages-needed">All the packages needed</a> and 
<a href="https://github.com/shourgamer2/simplyer#modify">Modify</a>
## Virus ?
This is not a virus it is marked as virus because it is made in python and python is not made for pc apps so don't worry it is 100% safe
## Support 
For support please join my <a href="https://discord.gg/4Ekyvrkyxn">Discord Server</a>
## Copyright 
© 2022 all rights reserved - Shourjjo Majumder. <br>
Please mention my repo if you copy it. <br>

