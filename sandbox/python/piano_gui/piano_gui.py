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
        # Insert svgWidget
        #print self.ui.menuFile.title()
        svgWidget = QtSvg.QSvgWidget('Zeichen_123.svg')
        svgWidget.setGeometry(50,50,759,668)
        svgWidget.show()

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawPiano(qp)
        qp.end()

    def drawPiano(self, qp):
        #color = QtGui.QColor(0, 0, 0)
        #color.setNamedColor('#d4d4d4')
        #qp.setPen(color)

        #qp.setBrush(QtGui.QColor(255, 255, 255))
        #qp.drawRect(10, 50, 10, 60)

        #qp.setBrush(QtGui.QColor(0, 0, 0))
        #qp.drawRect(130, 50, 10, 60)

        #qp.setBrush(QtGui.QColor(255, 255, 255))
        #qp.drawRect(250, 50, 10, 60) 
        
        piano_key_width = 10
        piano_key_height = 50
        piano_xcoord = 50
        piano_ycoord = 50

        # Plot White Keys        
        for i in range(52):
            qp.setBrush(QtGui.QColor(255, 255, 255))
            qp.drawRect(piano_xcoord + i * piano_key_width , piano_ycoord, 
                        piano_key_width, piano_key_height) 

        # Plot Black Keys        
        for i in range(52):
            qp.setBrush(QtGui.QColor(255, 255, 255))
            qp.drawRect(piano_xcoord + i * piano_key_width , piano_ycoord, 
                        piano_key_width, piano_key_height) 


if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)
        myapp = MyWindow()
        myapp.show()
        sys.exit(app.exec_())
