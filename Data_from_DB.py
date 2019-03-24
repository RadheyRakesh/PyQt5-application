import sys
import sqlite3
from DatabaseHelper import DatabaseHelper
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QLabel, QPushButton,QHBoxLayout,QComboBox,QTableWidgetItem,QVBoxLayout
from PyQt5.QtSql import (QSqlDatabase, QSqlQuery)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Input Dialog"
        self.top = 100
        self.left = 100
        self.width = 1000
        self.height = 500
        self.InitWindow()
        
        

    def InitWindow(self):

        self.addAngle = QPushButton("Add New Angle", self)
        self.addAngle.clicked.connect(self.on_clickAngle)
        self.addBeam = QPushButton("Add New Beam", self)
        self.addBeam.clicked.connect(self.on_clickBeam)
        self.addChannel = QPushButton("Add New Channel", self)
        self.addChannel.clicked.connect(self.on_clickChannel)
        self.angles = QLabel("Angles", self)
        self.beams = QLabel("Beams", self)
        self.channels = QLabel("Channels", self)
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.cb = QComboBox(self)
        databaseHelper = DatabaseHelper('steel_sections.sqlite')
        angles = databaseHelper.GetAllDimesions()
        self.cb.addItem('Please select')
        for angle in angles:
            self.cb.addItem(angle[0])

        self.cb.currentIndexChanged.connect(self.selectionchange)

        self.createAngleTable()
        self.createBeamsTable()
        self.createChannelsTable()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.cb)
        
        self.layout.addWidget(self.angles)
        self.layout.addWidget(self.angletableWidget)
        self.layout.addWidget(self.addAngle)
        
        
        self.layout.addWidget(self.beams)
        self.layout.addWidget(self.beamstableWidget)
        self.layout.addWidget(self.addBeam)
                
        self.layout.addWidget(self.channels)
        self.layout.addWidget(self.channelstableWidget)
        self.layout.addWidget(self.addChannel)
        
        self.setLayout(self.layout) 
        
        self.show()

    def selectionchange(self,i):
        selectedDesignation = self.cb.currentText()
        databaseHelper = DatabaseHelper('steel_sections.sqlite')
        anglesData = databaseHelper.GetAnglesDataForADesignation(selectedDesignation)
        beamsData = databaseHelper.GetBeamsDataForADesignation(selectedDesignation)
        channelsData = databaseHelper.GetChannelsDataForADesignation(selectedDesignation)
        for row in anglesData:
            inx = anglesData.index(row)
            self.angletableWidget.insertRow(inx)
            for i in range(24):
                self.angletableWidget.setItem(inx,i,QTableWidgetItem(str(row[i])))

        for row in beamsData:
            inx = beamsData.index(row)
            self.beamstableWidget.insertRow(inx)
            for i in range(20):
                self.beamstableWidget.setItem(inx,i,QTableWidgetItem(str(row[i])))

        for row in channelsData:
            inx = channelsData.index(row)
            self.channelstableWidget.insertRow(inx)
            for i in range(21):
                self.channelstableWidget.setItem(inx,i,QTableWidgetItem(str(row[i])))
        

    def createAngleTable(self):
        self.angletableWidget = QTableWidget()
        self.angletableWidget.setRowCount(0)
        self.angletableWidget.setColumnCount(24)
        header_labels = ['ID', 'Designation', 'Mass', 'Area','AXB','t','R1','R2','Cz','Cy','Tan?','Iz','Iy','Iu(max)',
                         'Iv(min)','rz','ry','ru(max)','rv(min)','Zz','Zy','Zpz','Zpy','Source']  
        self.angletableWidget.setHorizontalHeaderLabels(header_labels)

    def createBeamsTable(self):
        self.beamstableWidget = QTableWidget()
        self.beamstableWidget.setRowCount(0)
        self.beamstableWidget.setColumnCount(20)
        header_labels = ['ID', 'Designation', 'Mass', 'Area','D','B','tW','T','FlangeSlope','R1','R2','Iz','Iy','rz',
                         'ry','Zz','Zy','Zpz','Zpy','Source']  
        self.beamstableWidget.setHorizontalHeaderLabels(header_labels)
        
    def createChannelsTable(self):
        self.channelstableWidget = QTableWidget()
        self.channelstableWidget.setRowCount(0)
        self.channelstableWidget.setColumnCount(21)
        header_labels = ['ID', 'Designation', 'Mass', 'Area','D','B','tw','T','FlangeSlope','R1','R2','Cy','Iz','Iy',
                         'rz','ry','Zz','Zy','Zpz','Zpy','Source']  
        self.channelstableWidget.setHorizontalHeaderLabels(header_labels)


    def on_clickAngle(self):
        rowCount = self.angletableWidget.rowCount()
        self.angletableWidget.insertRow(rowCount)

    def on_clickBeam(self):
        rowCount = self.beamstableWidget.rowCount()
        self.beamstableWidget.insertRow(rowCount)


    def on_clickChannel(self):
        rowCount = self.channelstableWidget.rowCount()
        self.channelstableWidget5.insertRow(rowCount)

    def on_clickSaveAngle(self):
        print('Inside Save')
        rowCount = self.angletableWidget.rowCount()
        print(rowCount)
        if(rowCount == 0):
            return
        newAngle = []
        for i in range(24):
            item = self.angletableWidget.item(rowCount-1, i)
            newAngle.append(item.text())

        print(newAngle)
        databaseHelper = DatabaseHelper('steel_sections.sqlite')
        databaseHelper.SaveNewAngle(newAngle)
        print('DOnE')
    
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
