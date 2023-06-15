import urllib.request
import pandas as pd

from urllib.request import HTTPError, Request
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QComboBox, QLabel, QDesktopWidget
from data_set import url

class PokeDex(QWidget):
    def __init__(self):
      super(PokeDex, self).__init__()
      self.initUI()
      
    def initUI(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        
        self.df = pd.read_json('PokemonData.json')
        self.df = self.df.set_index(['#'])
        
        self.dropdown = QComboBox(self)
        self.names = self.df['Name'].values
        self.dropdown.addItems(self.names)
        self.grid.addWidget(self.dropdown, 0, 0, 1, 1)
        
        self.btn = QPushButton('Search', self)
        self.btn.clicked.connect(self.runSearch)
        self.grid.addWidget(self.btn, 0, 1, 1, 1)
        
        self.img = QLabel(self)
        self.grid.addWidget(self.img, 1, 1, 1, 1)
        
        self.label = QLabel(self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText('\nName:\n\nType:\n\nHP:\n\nAttack\n\nSp. Attack\n\n Defense:\n\nSp. Defense:\n\nSpeed:\n\nTotal:')
        self.label.setAlignment(QtCore.Qt.AlignLeft)
        self.grid.addWidget(self.label, 1, 0, 1, 1)
        
        self.resize(500, 250)
        self.center()
        self.setWindowTitle('Pokedex')
        self.show()
        
    def runSearch(self):
        index = self.dropdown.currentIndex()
        val = self.names[index]
        cond = self.df['Name']== val
        
        base = 'https://img.pokemondb.net/artwork/'
        img_url = base + val.lower() + '.jpg'
        req = Request(url = img_url.replace(' ', ''), headers = {'User-Agent': 'Mozilla/5.0'})
        try:
            data = urllib.request.urlopen(req).read()
        except HTTPError as e:
            if e.code != 404:
                raise HTTPError(e.url, e.code, "Unexpected HTTP Error", e.headers, e.fp)
            pass
        
        image = QtGui.QImage()
        try:
            image.loadFromData(data)
        except:
            image.load('image_not_available', format = 'png')
            self.img.setFixedSize(360, 314)   
        self.img.setPixmap(QtGui.QPixmap(image))

        name = 'Name:\t\t\t'+val+'\n\n'
        ty = 'Type:\t\t\t'+ ', '.join(self.df[cond]['Type'].values[0])+'\n\n'
        hp = 'HP:\t\t\t'+ str(self.df[cond]['HP'].values[0])+'\n\n'
        atk = 'Attack:\t\t\t'+str(self.df[cond]['Attack'].values[0])+'\n\n'
        satk = 'Sp. Attack:\t\t'+str(self.df[cond]['Sp. Atk'].values[0])+'\n\n'
        deff = 'Defense:\t\t\t'+str(self.df[cond]['Defense'].values[0])+'\n\n'
        sdef = 'Sp. Defense:\t\t'+str(self.df[cond]['Sp. Def'].values[0])+'\n\n'
        speed = 'Speed:\t\t\t'+str(self.df[cond]['Speed'].values[0])+'\n\n'
        total = 'Total:\t\t\t'+str(self.df[cond]['Total'].values[0])+'\n\n'

        final = name+ty+hp+atk+satk+deff+sdef+speed+total
        self.label.setText(final)
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        

        