from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QImage, QPixmap
import requests, pyperclip, functools

class Ui_DiscordMovieListWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
    def setupUi(self, DiscordMovieListForm):
        DiscordMovieListForm.setObjectName("DiscordMovieListForm")
        DiscordMovieListForm.setWindowModality(QtCore.Qt.NonModal)
        DiscordMovieListForm.resize(684, 372)
        self.scrollArea = QtWidgets.QScrollArea(DiscordMovieListForm)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 681, 371))
        self.scrollArea.setMinimumSize(QtCore.QSize(681, 371))
        self.scrollArea.setMaximumSize(QtCore.QSize(681, 371))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 679, 369))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(DiscordMovieListForm)
        QtCore.QMetaObject.connectSlotsByName(DiscordMovieListForm)

    def retranslateUi(self, DiscordMovieListForm):
        _translate = QtCore.QCoreApplication.translate
        DiscordMovieListForm.setWindowTitle(_translate("DiscordMovieListForm", "Discord Movie List"))
        
    def setMovieList(self, movieList):
        self.movieList = movieList
        
    def populateMovieList(self):
        for movie in self.movieList:
            self.plainTextEdit = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
            self.plainTextEdit.setMinimumSize(QtCore.QSize(641, 121))
            self.plainTextEdit.setMaximumSize(QtCore.QSize(641, 121))
            self.plainTextEdit.setAutoFillBackground(False)
            self.plainTextEdit.setLineWidth(1)
            self.plainTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.plainTextEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.WidgetWidth)
            self.plainTextEdit.setReadOnly(True)
            self.plainTextEdit.setPlainText(movie)
            self.verticalLayout.addWidget(self.plainTextEdit)
            