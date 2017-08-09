# Installing Dependencies

To use this package, a couple of external dependencies are required

- sip
- pyqt

follow these instructions to install on Ubuntu:

- Download the latest sip from [here][1].
- Download the latest pyqt4 from [here][2].
- Place the `tar.gz` in some directory (e.g. ~/lib)
- unzip them with `tar -zxvf`
- Go into the unzipped sip directory, and do:
    1. `python configure.py`
    2. `make`
    3. `make install`
- Go into the unzipped PyQT4 directory, and do:
    1. `python configure-ng.py`
    2. `make`
    3. `make install`
- Remove the two `tar.gz`'s

# To Do:
Draw interactive piano keyboard on [SVG canvas][4].

# Alternative GUI development for PyQT

Try [this][3]


[1]: http://www.riverbankcomputing.com/software/sip/download
[2]: http://www.riverbankcomputing.com/software/pyqt/download
[3]: https://pythonspot.com/en/pyqt4-gui-tutorial/
[4]: http://doc.qt.io/qt-4.8/qtwebkit-guide-canvas.html
