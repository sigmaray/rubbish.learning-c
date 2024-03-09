import sys
# from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QListWidget,QGridLayout,QLabel
from PyQt5.QtCore import QTimer,QDateTime

from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 

class WinForm(QWidget):
    def __init__(self,parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle('QTimer demonstration')

        self.listFile=QListWidget()
        self.label=QLabel('Label')
        self.startBtn=QPushButton('Start')
        self.endBtn=QPushButton('Stop')
        self.tray = QSystemTrayIcon() 

        icon = QIcon("icon.png") 
        self.tray.setIcon(icon) 
        self.tray.setVisible(True)  

        layout=QGridLayout()

        self.timer=QTimer()
        # self.timer.timeout.connect(self.showTime)
        self.timer.timeout.connect(self.onTimer)        
        # <
        self.timer.start(1000)
        # >

        layout.addWidget(self.label,0,0,1,2)
        layout.addWidget(self.startBtn,1,0)
        layout.addWidget(self.endBtn,1,1)

        # self.startBtn.clicked.connect(self.startTimer)
        # self.endBtn.clicked.connect(self.endTimer)

        self.setLayout(layout)

    def onTimer(self):
        # current_time=QDateTime.currentDateTime()
        # formatted_time=current_time.toString('yyyy-MM-dd hh:mm:ss dddd')
        # self.label.setText(formatted_time)
        print("ontimer")

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
