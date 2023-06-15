import sys

from PyQt5.QtWidgets import QApplication

from GUI import PokeDex

def main():
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    
    gui = PokeDex()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()