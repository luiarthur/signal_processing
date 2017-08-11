#!/usr/bin/python

import sys
from PyQt4 import QtCore, QtGui, QtSvg
from PyQt4.QtGui import *
from pianoForm import Ui_MainWindow

class MyWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawPiano(qp)
        qp.end()

    def drawPiano(self, qp):
        piano_black_key_width = 10
        piano_black_key_height = 50

        piano_white_key_width = 5
        piano_white_key_height = 30

        piano_xcoord = 50
        piano_ycoord = 50

        # Plot White Keys        
        for i in range(52):
            qp.setBrush(QtGui.QColor(QtCore.Qt.white))
            qp.drawRect(piano_xcoord + i * piano_black_key_width , piano_ycoord, 
                        piano_black_key_width, piano_black_key_height) 

        # Plot Black Keys        
        #for i in range(5):
        #    qp.setBrush(QtGui.QColor(0, 0, 0))
        #    qp.drawRect(piano_xcoord + i * piano_key_width , piano_ycoord, 
        #                piano_key_width, piano_key_height) 


if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)
        myapp = MyWindow()
        myapp.show()
        sys.exit(app.exec_())
