from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QLabel, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QSettings

from MovieWindow import Ui_MovieWindow
from DiscordMovieListWindow import Ui_DiscordMovieListWindow
from MovieNameListWindow import Ui_MovieNameListForm
from OptionsWindow import Ui_OptionsForm


import requests
import functools

class UiMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        self.settings = QSettings('JayInc', 'Entertainment Planner')
        self.movie_names_list = []
        self.saved_movie_list = []
        self.movie_list = []
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(990, 670)
        MainWindow.setMinimumSize(QtCore.QSize(990, 670))
        MainWindow.setMaximumSize(QtCore.QSize(990, 670))
        MainWindow.setMouseTracking(False)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 971, 641))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        
        self.movieSearchTab = QtWidgets.QWidget()
        self.movieSearchTab.setObjectName("movieSearchTab")
        
        self.searchMovieButton = QtWidgets.QPushButton(self.movieSearchTab)
        self.searchMovieButton.setGeometry(QtCore.QRect(830, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.searchMovieButton.setFont(font)
        self.searchMovieButton.setObjectName("searchMovieButton")
        
        self.scrollArea = QtWidgets.QScrollArea(self.movieSearchTab)
        self.scrollArea.setGeometry(QtCore.QRect(10, 50, 941, 481))
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(1000, 1000))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 939, 462))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        self.label = QtWidgets.QLabel(self.movieSearchTab)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        
        self.movieNamePlainTextEdit = QtWidgets.QPlainTextEdit(self.movieSearchTab)
        self.movieNamePlainTextEdit.setGeometry(QtCore.QRect(110, 10, 701, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.movieNamePlainTextEdit.setFont(font)
        self.movieNamePlainTextEdit.setObjectName("movieNamePlainTextEdit")
        
        self.showDiscordMovieButton = QtWidgets.QPushButton(self.movieSearchTab)
        self.showDiscordMovieButton.setGeometry(QtCore.QRect(570, 540, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.showDiscordMovieButton.setFont(font)
        self.showDiscordMovieButton.setObjectName("showDiscordMovieButton")
        
        self.movieNameListButton = QtWidgets.QPushButton(self.movieSearchTab)
        self.movieNameListButton.setGeometry(QtCore.QRect(10, 540, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.movieNameListButton.setFont(font)
        self.movieNameListButton.setObjectName("movieNameListButton")
        
        self.saveDiscordMovieListButton = QtWidgets.QPushButton(self.movieSearchTab)
        self.saveDiscordMovieListButton.setGeometry(QtCore.QRect(770, 540, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.saveDiscordMovieListButton.setFont(font)
        self.saveDiscordMovieListButton.setObjectName("saveDiscordMovieListButton")
        
        self.searchNextMovieButton = QtWidgets.QPushButton(self.movieSearchTab)
        self.searchNextMovieButton.setGeometry(QtCore.QRect(200, 540, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.searchNextMovieButton.setFont(font)
        self.searchNextMovieButton.setObjectName("searchNextMovieButton")
        
        self.tabWidget.addTab(self.movieSearchTab, "")
        self.optionsButton = QtWidgets.QPushButton(self.centralwidget)
        self.optionsButton.setGeometry(QtCore.QRect(940, 10, 31, 21))
        self.optionsButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Jayu/Downloads/icons8-settings-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.optionsButton.setIcon(icon)
        self.optionsButton.setObjectName("optionsButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionOptions = QtWidgets.QAction(MainWindow)
        self.actionOptions.setObjectName("actionOptions")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.connect_buttons_manually()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Entertainment Planner"))
        self.searchMovieButton.setText(_translate("MainWindow", "Search Movie"))
        self.label.setText(_translate("MainWindow", "Select A Movie:"))
        self.showDiscordMovieButton.setText(_translate("MainWindow", "Show Discord Movie List"))
        self.movieNameListButton.setText(_translate("MainWindow", "Movie Name List"))
        self.saveDiscordMovieListButton.setText(_translate("MainWindow", "Save Discord Movie List"))
        self.searchNextMovieButton.setText(_translate("MainWindow", "Search Next Movie"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.movieSearchTab), _translate("MainWindow", "Movie Search"))

    def set_ui_main_window(self, ui_main_window):
        self.ui_main_window = ui_main_window

    def connect_buttons_manually(self):
        self.searchMovieButton.clicked.connect(self.populate_with_movie_list)
        self.showDiscordMovieButton.clicked.connect(self.show_discord_movie_list_window)
        self.movieNameListButton.clicked.connect(self.show_movie_name_list_window)
        self.searchNextMovieButton.clicked.connect(self.search_next_movie)
        self.optionsButton.clicked.connect(self.show_options_window)
        self.saveDiscordMovieListButton.clicked.connect(self.save_discord_movie_list)

    def get_movie_by_name(self):
        api_Key = self.settings.value('api_key')
        movie_name = self.movieNamePlainTextEdit.toPlainText().strip()
        request_url = 'https://www.omdbapi.com/?apikey=' + api_Key + '&type=movie&s=' + movie_name
        return requests.get(request_url).json()

    def get_movie_by_imdb_id(self, imdb_id):
        api_Key = self.settings.value('api_key')
        request_url = 'https://www.omdbapi.com/?apikey=' + api_Key + '&type=movie&i=' + imdb_id
        omdb_api_request = requests.get(request_url).json()
        return omdb_api_request
    
    def add_movie_to_list(self, movie_name, movie):
        if movie_name in self.saved_movie_list:
            message_box = QMessageBox()
            message_box.setWindowTitle('Adding Movie To List')
            message_box.setText('Error: Can\'t add movie to list.')
            message_box.setInformativeText('The movie you selected is already in the list.')
            message_box.setIcon(QMessageBox.Warning)
            message_box.setStandardButtons(QMessageBox.Ok)
            message_box.exec_()
        else:
            self.saved_movie_list.append(movie_name)
            self.movie_list.append(movie)
        
    def set_movie_names_list(self, movie_names_list):
        self.movie_names_list = movie_names_list
    
    def clear_layout(self):
        if self.horizontalLayout is not None:
            while self.horizontalLayout.count():
                item = self.horizontalLayout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

    def populate_with_movie_list(self):
        self.clear_layout()
        
        temp_movie_list = self.get_movie_by_name()
        
        if 'Search' not in temp_movie_list:
            message_box = QMessageBox()
            message_box.setWindowTitle('Searching For Movie')
            message_box.setText('Error: Couldn\'t find the movie')
            message_box.setInformativeText('Try again with another name.')
            message_box.setIcon(QMessageBox.Warning)
            message_box.setStandardButtons(QMessageBox.Ok)
            message_box.exec_()
            return
        else:
            temp_movie_list = temp_movie_list['Search']

        for movie in temp_movie_list:
            image = QImage()
            if (movie['Poster'] == 'N/A'): continue
            image.loadFromData(requests.get(movie['Poster']).content)

            testLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            testLabel.setMinimumSize(QtCore.QSize(300, 444))
            testLabel.setMaximumSize(QtCore.QSize(300, 444))
            testLabel.setAlignment(QtCore.Qt.AlignCenter)
            testLabel.setPixmap(QPixmap(image))
            testLabel.mousePressEvent = functools.partial(self.show_movie_window, imdb_id=movie['imdbID'])
            self.horizontalLayout.addWidget(testLabel)
    
    def search_next_movie(self):
        movie_name = self.movie_names_list.pop(0)
        self.movieNamePlainTextEdit.setPlainText(movie_name.strip())
        self.searchMovieButton.click()
        
    def save_discord_movie_list(self):
        movie_name_file_path = QFileDialog.getSaveFileName(self,'QFileDialog.getSaveFileName()', '','All Files (*);Text Files (*.txt)')
        file = open(movie_name_file_path[0],'w+', encoding="utf-8")
        for movie in self.movie_list:
            file.write(str(movie))
            file.write(str('\n'))
            file.write(str('\n'))
        file.close()
    
    def show_movie_window(self, event, imdb_id):
        movie = self.get_movie_by_imdb_id(imdb_id)

        self.movie_window = QtWidgets.QWidget()
        self.movie_window_ui = Ui_MovieWindow()
        self.movie_window_ui.set_ui_main_window(self.ui_main_window)
        self.movie_window_ui.set_movie(movie)
        self.movie_window_ui.setupUi(self.movie_window)
        self.movie_window_ui.populate_movie_details()
        self.movie_window.show()
        
    def show_discord_movie_list_window(self):
        self.discord_movie_list_window = QtWidgets.QWidget()
        self.discord_movie_list_window_ui = Ui_DiscordMovieListWindow()
        self.discord_movie_list_window_ui.setupUi(self.discord_movie_list_window)
        self.discord_movie_list_window_ui.set_movie_list(self.movie_list)
        self.discord_movie_list_window_ui.populate_movie_list()
        self.discord_movie_list_window.show()
        
    def show_movie_name_list_window(self):
        self.movie_name_list_window = QtWidgets.QWidget()
        self.movie_name_list_window_ui = Ui_MovieNameListForm()
        self.movie_name_list_window_ui.setupUi(self.movie_name_list_window)
        self.movie_name_list_window_ui.set_main_window(self.ui_main_window)
        self.movie_name_list_window_ui.set_movie_names_list(self.movie_names_list)
        self.movie_name_list_window_ui.load_list_view_with_movie_names()
        self.movie_name_list_window.show()
        
    def show_options_window(self):
        self.options_window = QtWidgets.QWidget()
        self.options_window_ui = Ui_OptionsForm()
        self.options_window_ui.setupUi(self.options_window)
        self.options_window_ui.set_main_window(self.ui_main_window)
        self.options_window.show()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui_main_window = UiMainWindow()
    ui_main_window.setupUi(MainWindow)
    ui_main_window.set_ui_main_window(ui_main_window)
    MainWindow.show()
    sys.exit(app.exec_())