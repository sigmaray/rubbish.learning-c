import sys
import json
import requests
# from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QListWidget,QGridLayout,QLabel
from PyQt5.QtCore import QTimer,QDateTime, QThread, QEventLoop

from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 



class DataCaptureThread(QThread):
    def fetch(self):
      url = "https://api.openweathermap.org/data/2.5/weather?q=Berlin&lang=ru&units=metric&appid=5a043a1bd95bf3ee500eb89de107b41e"
      # url = "https://httpstat.us/200?sleep=5000"
      # url = "https://httpstat.us/200"
      #  url = "http://download.thinkbroadband.com/10MB.zip"
      print("l14 starting get")
      r = requests.get(url)
      print("l16 ended get")
      str = r.content
      parsed_json = json.loads(str)
      temp = parsed_json['main']['temp']
      # import time
      # time.sleep(5)
      return f'{temp:.0f}'
      # # print(temp)

    def collectProcessData(self):
        print ("Collecting Process Data")
        # self.callback("l25")
        try:
          from datetime import datetime
          now = datetime.now()

          dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
          print("date and time =", dt_string)
          temp = self.fetch()
          # self.text_edit.append(dt_string + " " + temp + "C")
          self.callback(temp)
        except Exception as e:
          print("An exception occurred: " + str(e))

    def __init__(self, callback, *args, **kwargs):
        QThread.__init__(self, *args, **kwargs)        
        self.callback = callback
        # self.dataCollectionTimer = QTimer()
        # self.dataCollectionTimer.moveToThread(self)
        # self.dataCollectionTimer.timeout.connect(self.collectProcessData)

    def run(self):
        # self.collectProcessData()
        # self.dataCollectionTimer.start(1000)
        # loop = QEventLoop()
        # loop.exec_()
       while True:
          self.collectProcessData()
          import time
          time.sleep(3)

class WinForm(QWidget):
    def __init__(self,parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle('QTimer demonstration')

        # self.listFile=QListWidget()
        # self.label=QLabel('Label')
        # self.startBtn=QPushButton('Start')
        # self.endBtn=QPushButton('Stop')
        self.tray = QSystemTrayIcon() 
        self.text_edit = QTextEdit()


        icon = QIcon("icon.png") 
        self.tray.setIcon(icon) 
        self.tray.setVisible(True)  

        layout=QGridLayout()

        # self.thread = QThread()
        # self.thread.finished.connect(self.thread.deleteLater)
        # self.timer=QTimer()       
        # # self.timer.moveToThread(self)
        # self.timer.moveToThread(self.thread)
        # # self.timer.timeout.connect(self.showTime)
        # self.timer.timeout.connect(self.onTimer)        
        # # <
        # self.onTimer()
        # # self.timer.start(1000)
        # # self.timer.start(5000)
        # self.timer.start(1000)
        # # >
        # self.thread = QThread()
        # self.thread.start()
        # # Step 3: Create a worker object
        # # self.worker = Worker()
        # # Step 4: Move worker to the thread
        # self.timer.moveToThread(self.thread)
        # # Step 5: Connect signals and slots
        # # self.thread.started.connect(self.worker.run)
        # # self.worker.finished.connect(self.thread.quit)
        # # self.worker.finished.connect(self.worker.deleteLater)
        # # self.thread.finished.connect(self.thread.deleteLater)
        # # self.worker.progress.connect(s/elf.reportProgress)
        # # Step 6: Start the thread

        def callback(text):
          #  print("l82")
          self.onTimer(text)

        self.dataCollectionThread = DataCaptureThread(callback)
        self.dataCollectionThread.start()
        

        layout.addWidget(self.text_edit,0,0,1,2)
        # layout.addWidget(self.label,0,0,1,2)
        # layout.addWidget(self.startBtn,1,0)
        # layout.addWidget(self.endBtn,1,1)

        # self.startBtn.clicked.connect(self.startTimer)
        # self.endBtn.clicked.connect(self.endTimer)

        self.setLayout(layout)

    def onTimer(self, temp):
      # pass
      current_time=QDateTime.currentDateTime()
      formatted_time=current_time.toString('yyyy-MM-dd hh:mm:ss dddd')
      # self.label.setText(formatted_time + " | " + text)
      self.text_edit.append(formatted_time + " " + temp + "C")
      # print("ontimer")
      ##############
      # try:
      #   from datetime import datetime
      #   now = datetime.now()

      #   dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
      #   print("date and time =", dt_string)
      #   temp = fetch()
      #   self.text_edit.append(dt_string + " " + temp + "C")
      # except:
      #   print("An exception occurred")

    # def showTime(self):
    #     current_time=QDateTime.currentDateTime()
    #     formatted_time=current_time.toString('yyyy-MM-dd hh:mm:ss dddd')
    #     self.label.setText(formatted_time)

    # def startTimer(self):
    #     self.timer.start(1000)
    #     self.startBtn.setEnabled(False)
    #     self.endBtn.setEnabled(True)

    # def endTimer(self):
    #     self.timer.stop()
    #     self.startBtn.setEnabled(True)
    #     self.endBtn.setEnabled(False)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    form=WinForm()
    form.show()
    sys.exit(app.exec_())
