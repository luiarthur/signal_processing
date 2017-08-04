#!/usr/bin/python

import sys
from PyQt4.QtGui import *

######### INIT ######################################

# Create an PyQT4 application object.
a = QApplication(sys.argv)
 
# The QWidget widget is the base class of all user interface objects in PyQt4.
#w = QWidget()
w = QMainWindow()

######## CHANGE STUFF ################################
 
# Set window size.
w.resize(320, 240)
 
# Set window title
w.setWindowTitle("Hello World!")
 
# Add a button
btn = QPushButton('Hello World!', w)
btn.setToolTip('Click to quit!')
btn.clicked.connect(exit)
#btn.resize(btn.sizeHint())
btn.move(100, 80)

# Create main menu
mainMenu = w.menuBar()
mainMenu.setNativeMenuBar(False)
fileMenu = mainMenu.addMenu('File')
EditMenu = mainMenu.addMenu('Edit')

#### CLOSING ##########################################

# Show window
w.show()

#Wait for signal. Exit on cue.
sys.exit(a.exec_())
