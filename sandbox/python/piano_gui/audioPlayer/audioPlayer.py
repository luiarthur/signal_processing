import sys
from PyQt4 import QtCore, QtGui
from PyQt4.phonon import Phonon
from mutagen.id3 import ID3

class Frederic(QtGui.QDialog):

    def __init__(self):
        QtGui.QWidget.__init__(self)

        vbox = QtGui.QVBoxLayout(self)

        self.setWindowTitle("Frederic Music Player")
        self.move(400, 200)

        self.label = QtGui.QLabel(self)
        self.status = QtGui.QLabel(self)
        self.play = QtGui.QPushButton("Play")
        self.pause = QtGui.QPushButton("Pause")
        self.stop = QtGui.QPushButton("Stop")
        self.siguiente = QtGui.QPushButton("Siguiente")
        self.anterior = QtGui.QPushButton("Anterior")
        self.listWidget = QtGui.QListWidget(self)

        self.agregar = QtGui.QPushButton("Agregar")
        self.eliminar = QtGui.QPushButton("Eliminar")
        self.artist = None
        self.song = None

        # Phonon settings

        self.player = Phonon.createPlayer(Phonon.MusicCategory)
        self.player.setTickInterval(100)
        self.player.tick.connect(self.ticking)
        self.spin = Phonon.SeekSlider(self.player, self)

        # Implementing the layout

        vbox.addWidget(self.label)
        vbox.addWidget(self.status)

        hbox0 = QtGui.QHBoxLayout(self)

        hbox0.addWidget(self.play)
        hbox0.addWidget(self.pause)
        hbox0.addWidget(self.stop)
        hbox0.addWidget(self.anterior)
        hbox0.addWidget(self.siguiente)

        vbox.addLayout(hbox0)

        vbox.addWidget(self.listWidget)

        hbox = QtGui.QHBoxLayout(self)

        hbox.addWidget(self.agregar)
        hbox.addWidget(self.eliminar)

        vbox.addLayout(hbox)
        vbox.addWidget(self.spin)

        self.setLayout(vbox)

        self.play.clicked.connect(self.funcPlay)
        self.agregar.clicked.connect(self.funcAgregar)
        self.eliminar.clicked.connect(self.funcEliminar)
        self.pause.clicked.connect(lambda: self.player.pause())
        self.stop.clicked.connect(lambda: self.player.stop())
        self.player.aboutToFinish.connect(self.nextSongQueued)
        self.siguiente.clicked.connect(self.nextSong)
        self.anterior.clicked.connect(self.previousSong)

        self.file_name = None
        self.data = None
        self.songs = {}
        self.SongPlaying = None
        self.SongQueued = None

    def funcPlay(self):
        self.label.setText(self.listWidget.currentItem().text())
        CurrentSong = (self.listWidget.currentItem().text())
        self.SongPlaying = CurrentSong
        SongToPlay = self.songs[CurrentSong]
        self.player.setCurrentSource(Phonon.MediaSource(SongToPlay))
        self.player.play()

    def funcPause(self):
        self.player.pause()

    def ticking(self, time):
        displayTime = QtCore.QTime(0, (time / 60000) % 60, (time / 1000) % 60)
        self.status.setText(displayTime.toString('mm:ss'))

    def funcAgregar(self):
        self.file_name = QtGui.QFileDialog.getOpenFileName(
            self, "Open Data File", "", "MP3 (*.mp3)")

        id3 = ID3(self.file_name)

        try:
            self.data = self.artist = id3['TPE1'].text[0] + " - " + id3["TIT2"].text[0]
            self.songs[self.data] = self.file_name
            self.listWidget.addItem(self.data)
        except:
            self.data
            self.songs[self.file_name] = self.file_name
            self.listWidget.addItem(self.data)
            d = QtGui.QMessageBox()
            d.setWindowTitle('Error!')
            d.setText("El archivo que ha elegido no funciona. Seleccione otro archivo por favor.")
            d.exec_()

    def funcEliminar(self):
        self.listWidget.takeItem(self.ui.listWidget.currentRow())

    def nextSongQueued(self):
        next = self.listWidget.currentRow() + 1
        nextSong = self.listWidget.item(next).text()
        self.SongQueued = nextSong
        SongToPlay = self.songs[nextSong]
        self.player.enqueue(Phonon.MediaSource(SongToPlay))
        self.label.setText(self.SongQueued)
        self.SongPlaying = self.SongQueued

    def nextSong(self):
        next = self.listWidget.currentRow() + 1
        nextSong = self.listWidget.item(next).text()
        self.SongQueued = nextSong
        SongToPlay = self.songs[nextSong]
        self.label.setText(self.SongQueued)
        self.SongPlaying = self.SongQueued
        self.player.setCurrentSource(Phonon.MediaSource(SongToPlay))
        self.player.play()
        self.listWidget.setCurrentRow(next)

    def previousSong(self):
        next = self.listWidget.currentRow() - 1
        nextSong = self.listWidget.item(next).text()
        self.SongQueued = nextSong
        SongToPlay = self.songs[nextSong]
        self.label.setText(self.SongQueued)
        self.SongPlaying = self.SongQueued
        self.player.setCurrentSource(Phonon.MediaSource(SongToPlay))
        self.player.play()
        self.listWidget.setCurrentRow(next)

app = QtGui.QApplication(sys.argv)
w = Frederic()
w.show()
sys.exit(app.exec_())
