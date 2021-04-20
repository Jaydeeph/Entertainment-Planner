from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QInputDialog, QLineEdit, QFileDialog


class Ui_MovieNameListForm(QWidget):
    
    def __init__(self):
        super().__init__()
        
    def setupUi(self, MovieNameForm):
        MovieNameForm.setObjectName("MovieNameForm")
        MovieNameForm.resize(481, 410)
        MovieNameForm.setMinimumSize(QtCore.QSize(481, 410))
        MovieNameForm.setMaximumSize(QtCore.QSize(481, 16777215))
        self.listView = QtWidgets.QListView(MovieNameForm)
        self.listView.setGeometry(QtCore.QRect(0, 0, 481, 341))
        self.listView.setMinimumSize(QtCore.QSize(481, 341))
        self.listView.setMaximumSize(QtCore.QSize(481, 341))
        self.listView.setObjectName("listView")
        self.loadMovieNamesButton = QtWidgets.QPushButton(MovieNameForm)
        self.loadMovieNamesButton.setGeometry(QtCore.QRect(10, 350, 461, 51))
        self.loadMovieNamesButton.setObjectName("loadMovieNamesButton")

        self.retranslateUi(MovieNameForm)
        QtCore.QMetaObject.connectSlotsByName(MovieNameForm)
        
        self.connect_buttons_manually()

    def retranslateUi(self, MovieNameForm):
        _translate = QtCore.QCoreApplication.translate
        MovieNameForm.setWindowTitle(_translate("MovieNameForm", "Movie Names List"))
        self.loadMovieNamesButton.setText(_translate("MovieNameForm", "Load Movie Names"))
        
    def connect_buttons_manually(self):
        self.loadMovieNamesButton.clicked.connect(self.load_movie_name_list)
    
    def set_main_window(self, main_window):
        self.main_window = main_window
        
    def set_movie_names_list(self, movie_names_list):
        self.movie_names_list = movie_names_list
        
    def load_list_view_with_movie_names(self):
        
        if self.movie_names_list is None:
            return
        
        model = QtGui.QStandardItemModel()
        self.listView.setModel(model)
        
        for movie_name in self.movie_names_list:
            item = QtGui.QStandardItem(movie_name)
            model.appendRow(item)
    
    def load_movie_name_list(self):
        self.movie_name_list = []
        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        movie_name_file_path, _ = QFileDialog.getOpenFileName(self,'QFileDialog.getOpenFileName()', '','All Files (*);Text Files (*.txt)')
        if movie_name_file_path:
            movie_name_file = open(movie_name_file_path, 'r')
            self.movie_names_list = movie_name_file.readlines()
            self.main_window.set_movie_names_list(self.movie_names_list)
            self.load_list_view_with_movie_names()