import requests
import json
import lib

url = "https://api.openweathermap.org/data/2.5/weather?q=Berlin&lang=ru&units=metric&appid=5a043a1bd95bf3ee500eb89de107b41e"
#  url = "http://download.thinkbroadband.com/10MB.zip"
r = requests.get(url)
str = r.content
parsed_json = json.loads(str)
temp = parsed_json['main']['temp']
print(temp)

 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
  
  
app = QApplication([]) 
app.setQuitOnLastWindowClosed(False) 
  
# Adding an icon 
# icon = QIcon("icon.png") 
text = f'{temp:.0f}'
icon = lib.drawIcon(text)
  
# Adding item on the menu bar 
tray = QSystemTrayIcon() 
tray.setIcon(icon) 
tray.setVisible(True) 
  
# Creating the options 
menu = QMenu()
option1 = QAction("Geeks for Geeks") 
option2 = QAction("GFG") 
menu.addAction(option1) 
menu.addAction(option2) 
  
# To quit the app 
quit = QAction("Quit") 
quit.triggered.connect(app.quit) 
menu.addAction(quit) 
  
# Adding options to the System Tray 
tray.setContextMenu(menu) 
  
app.exec_() 