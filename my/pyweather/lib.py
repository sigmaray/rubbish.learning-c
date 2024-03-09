from PyQt5.QtGui import QPixmap, QColor, QPainter, QFont, QIcon
from PyQt5 import QtCore

def drawIcon(strVal="--", textColor="#000", bgColor="#fff"):
    """Render string into QIcon to be shown in tray"""
    pixmap = QPixmap(24, 24)
    pixmap.fill(QColor(bgColor))

    painter = QPainter(pixmap)
    painter.setPen(QColor(textColor))

    if len(strVal) >= 3:
        fontSize = 10
    else:
        fontSize = 12
    painter.setFont(QFont('Arial', fontSize))

    painter.drawText(pixmap.rect(), QtCore.Qt.AlignCenter, strVal)
    painter.end()
    return QIcon(pixmap)
