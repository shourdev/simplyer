## simplyer
A simple browser.Open source and simple.This browser is made using python<br> 
## Download version 1.0.0 
<a href="https://github.com/shourgamer2/simplyer/releases/download/normalinstaller/simplyer.exe">Download Normal Installer</a> <br>
<a href="https://github.com/shourgamer2/simplyer/releases/download/Portable/simplyer.exe">Download Portable  </a>
## portable
portable version is a version which can be used on a pendrive without installing just download the file move it to your pendrive and your done ! 
## Copy
Fork the repo by clicking on the fork button
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
## If you copy
If you fork this project then please mention my repo in your credits section
## Virus ?
This is not a virus it is marked as virus because it is made in python and python is not made for pc apps so don't worry it is 100% safe
## Support 
For support please join my <a href="https://discord.gg/4Ekyvrkyxn">Discord Server</a>
