from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QPushButton, QLabel, QWidget
from PyQt5.QtCore import QSettings

import requests

class Ui_OptionsForm(QWidget):
    
    def __init__(self):
        super().__init__()
        
    def setupUi(self, OptionsForm):
        self.settings = QSettings('JayInc', 'Entertainment Planner')
        
        OptionsForm.setObjectName("OptionsForm")
        OptionsForm.resize(350, 93)
        self.label = QtWidgets.QLabel(OptionsForm)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.apiLineEdit = QtWidgets.QLineEdit(OptionsForm)
        self.apiLineEdit.setGeometry(QtCore.QRect(70, 10, 71, 20))
        self.apiLineEdit.setInputMask("")
        self.apiLineEdit.setObjectName("apiLineEdit")
        self.validateApiButton = QtWidgets.QPushButton(OptionsForm)
        self.validateApiButton.setGeometry(QtCore.QRect(150, 10, 81, 23))
        self.validateApiButton.setObjectName("validateApiButton")
        self.validateApiLabel = QtWidgets.QLabel(OptionsForm)
        self.validateApiLabel.setGeometry(QtCore.QRect(240, 10, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.validateApiLabel.setFont(font)
        self.validateApiLabel.setTextFormat(QtCore.Qt.AutoText)
        self.validateApiLabel.setObjectName("validateApiLabel")
        self.line = QtWidgets.QFrame(OptionsForm)
        self.line.setGeometry(QtCore.QRect(0, 40, 351, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.saveButton = QtWidgets.QPushButton(OptionsForm)
        self.saveButton.setGeometry(QtCore.QRect(254, 60, 81, 23))
        self.saveButton.setObjectName("saveButton")

        self.retranslateUi(OptionsForm)
        QtCore.QMetaObject.connectSlotsByName(OptionsForm)
        
        self.connect_buttons_manually()
        self.load_options()

    def retranslateUi(self, OptionsForm):
        _translate = QtCore.QCoreApplication.translate
        OptionsForm.setWindowTitle(_translate("OptionsForm", "Options"))
        self.label.setText(_translate("OptionsForm", "OmdbApi:"))
        self.validateApiButton.setText(_translate("OptionsForm", "Validate API"))
        self.saveButton.setText(_translate("OptionsForm", "Save"))
        
    def connect_buttons_manually(self):
        self.validateApiButton.clicked.connect(self.validate_api_button_click)
        self.saveButton.clicked.connect(self.save_options)

    def validate_api_button_click(self):
        api_Key = self.apiLineEdit.text().strip()
        request_url = 'https://www.omdbapi.com/?apikey=' + api_Key
        result = requests.get(request_url).json()
        
        if(result['Error'] == 'Incorrect IMDb ID.'):
            self.validateApiLabel.setText('<font color="green">Valid API key!</font>')
        if(result['Error'] == 'Invalid API key!'):
            self.validateApiLabel.setText('<font color="red">Invalid API key!</font>')
    
    def load_options(self):
        self.apiLineEdit.setText(self.settings.value('api_key'))
    
    def save_options(self):
        self.settings.setValue('api_key', self.apiLineEdit.text().strip())
