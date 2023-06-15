import sys

from PyQt5 import QtGui

from GUI import PokeDex

def main():
    app = QtGui.QGuiApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    
    gui = PokeDex()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()