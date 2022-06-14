import sys
from PyQt5.QtWidgets import  *
from PyQt5.QtCore import *

class Signal(QObject):
     signal = pyqtSignal()

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initWindow()



    def initWindow(self):
        self.sig = Signal()
        self.sig.signal.connect(self.close) #프로그램종료

        self.setGeometry(50,50,300,300)
        self.show()

    def mousePressEvent(self, QMouseEvent):
        self.sig.signal.emit() #에밋메서드


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())