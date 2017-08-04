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

 
if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)
        myapp = MyWindow()
        myapp.show()
        sys.exit(app.exec_())
