from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTime, QTimer, Qt
from time import time

class Zegarek(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent,Qt.WindowStaysOnTopHint)
        self.resize(200, 75)
        self.setWindowTitle("Zegarek")
        self.setStyleSheet("background-color: black; color: white; font-size: 43px")
        self.layout = QVBoxLayout()
        self.timelabel = QLabel(QTime.currentTime().toString('hh:mm:ss'))
        self.layout.addWidget(self.timelabel)
        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)
        self.timer = QTimer()
        self.timer.timeout.connect(self.setTime)
        self.timer.start(1000)
        self.show()
    def setTime(self):
        self.timelabel.setText(QTime.currentTime().toString('hh:mm:ss'))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    okno = Zegarek()
    sys.exit(app.exec_())