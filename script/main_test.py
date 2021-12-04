import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import time
from AdamTest_func import TestAtestWindow
import os
import threading

class AtestWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.Atest = TestAtestWindow()
        self.Atest.setupUi(self)

        self.setWindowTitle("Adam Test Mode")
        # MAIN WINDOW LABEL
        # self.setWindowIcon(QIcon(QPixmap(os.path.join('icons',self.ui.project_path + 'images/caseLab.png'))))
        
        # Frameless and Background
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)



        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #window = SplashScreen()
    # window = MainWindow()
    window = AtestWindow()
    sys.exit(app.exec_())
    