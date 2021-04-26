from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QPushButton, QLabel, QWidget, QMessageBox
from PyQt5.QtCore import QSettings
import requests
import re

class Ui_OptionsForm(QWidget):
    
    def __init__(self):
        super().__init__()
        
    def setupUi(self, OptionsForm):
        self.settings = QSettings('JayInc', 'Entertainment Planner')
        self.movie = {
            "Title":"The Shawshank Redemption",
            "Year":"1994",
            "Rated":"R",
            "Released":"14 Oct 1994",
            "Runtime":"142 min",
            "Genre":"Drama",
            "Director":"Frank Darabont",
            "Writer":"Stephen King (short story \"Rita Hayworth and Shawshank Redemption\"),Frank Darabont (screenplay)",
            "Actors":"Tim Robbins, Morgan Freeman, Bob Gunton, William Sadler",
            "Plot":"Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
            "Language":"English",
            "Country":"USA",
            "Awards":"Nominated for 7 Oscars. Another 21 wins & 36 nominations.",
            "Poster":"https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg",
            "Ratings":  [
                            {
                                "Source":"Internet Movie Database",
                                "Value":"9.3/10"
                            },
                            {
                                "Source":"Rotten Tomatoes",
                                "Value":"91%"
                            },
                            {
                                "Source":"Metacritic",
                                "Value":"80/100"
                            }
                        ],
            "Metascore":"80",
            "imdbRating":"9.3",
            "imdbVotes":"2,367,380",
            "imdbID":"tt0111161",
            "Type":"movie",
            "DVD":"15 Aug 2008",
            "BoxOffice":"$28,699,976",
            "Production":"Columbia Pictures, Castle Rock Entertainment",
            "Website":"N/A"
        }
        self.options_form = OptionsForm
        OptionsForm.setObjectName("OptionsForm")
        OptionsForm.resize(580, 491)
        OptionsForm.setMinimumSize(QtCore.QSize(580, 491))
        OptionsForm.setMaximumSize(QtCore.QSize(580, 491))
        self.label = QtWidgets.QLabel(OptionsForm)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.apiLineEdit = QtWidgets.QLineEdit(OptionsForm)
        self.apiLineEdit.setGeometry(QtCore.QRect(70, 10, 61, 21))
        self.apiLineEdit.setInputMask("")
        self.apiLineEdit.setObjectName("apiLineEdit")
        self.validateApiButton = QtWidgets.QPushButton(OptionsForm)
        self.validateApiButton.setGeometry(QtCore.QRect(140, 10, 81, 23))
        self.validateApiButton.setObjectName("validateApiButton")
        self.validateApiLabel = QtWidgets.QLabel(OptionsForm)
        self.validateApiLabel.setGeometry(QtCore.QRect(230, 10, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.validateApiLabel.setFont(font)
        self.validateApiLabel.setTextFormat(QtCore.Qt.AutoText)
        self.validateApiLabel.setObjectName("validateApiLabel")
        self.line = QtWidgets.QFrame(OptionsForm)
        self.line.setGeometry(QtCore.QRect(6, 440, 571, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.saveButton = QtWidgets.QPushButton(OptionsForm)
        self.saveButton.setGeometry(QtCore.QRect(290, 460, 281, 23))
        self.saveButton.setObjectName("saveButton")
        self.autoSaveCheckBox = QtWidgets.QCheckBox(OptionsForm)
        self.autoSaveCheckBox.setGeometry(QtCore.QRect(10, 50, 371, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.autoSaveCheckBox.setFont(font)
        self.autoSaveCheckBox.setObjectName("autoSaveCheckBox")
        self.autoCloseCheckBox = QtWidgets.QCheckBox(OptionsForm)
        self.autoCloseCheckBox.setGeometry(QtCore.QRect(10, 90, 301, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.autoCloseCheckBox.setFont(font)
        self.autoCloseCheckBox.setObjectName("autoCloseCheckBox")
        self.customMovieFormatCheckBox = QtWidgets.QCheckBox(OptionsForm)
        self.customMovieFormatCheckBox.setGeometry(QtCore.QRect(10, 130, 451, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.customMovieFormatCheckBox.setFont(font)
        self.customMovieFormatCheckBox.setObjectName("customMovieFormatCheckBox")
        self.customFormatPlainTextEdit = QtWidgets.QPlainTextEdit(OptionsForm)
        self.customFormatPlainTextEdit.setGeometry(QtCore.QRect(10, 160, 561, 131))
        self.customFormatPlainTextEdit.setObjectName("customFormatPlainTextEdit")
        self.checkJsonListButton = QtWidgets.QPushButton(OptionsForm)
        self.checkJsonListButton.setGeometry(QtCore.QRect(490, 130, 81, 21))
        self.checkJsonListButton.setObjectName("checkJsonListButton")
        self.customFormatResultsPlainTextEdit = QtWidgets.QPlainTextEdit(OptionsForm)
        self.customFormatResultsPlainTextEdit.setGeometry(QtCore.QRect(10, 300, 561, 141))
        self.customFormatResultsPlainTextEdit.setPlainText("")
        self.customFormatResultsPlainTextEdit.setObjectName("customFormatResultsPlainTextEdit")
        self.clearOptionsButton = QtWidgets.QPushButton(OptionsForm)
        self.clearOptionsButton.setGeometry(QtCore.QRect(10, 460, 271, 23))
        self.clearOptionsButton.setObjectName("clearOptionsButton")

        self.retranslateUi(OptionsForm)
        QtCore.QMetaObject.connectSlotsByName(OptionsForm)
        
        self.connect_buttons_manually()
        self.load_options()

    def retranslateUi(self, OptionsForm):
        _translate = QtCore.QCoreApplication.translate
        OptionsForm.setWindowTitle(_translate("OptionsForm", "Options"))
        self.apiLineEdit.setText(_translate("OptionsForm", ""))
        self.label.setText(_translate("OptionsForm", "OmdbApi:"))
        self.validateApiButton.setText(_translate("OptionsForm", "Validate API"))
        self.saveButton.setText(_translate("OptionsForm", "Save"))
        self.autoSaveCheckBox.setText(_translate("OptionsForm", "Auto save movie to file when \"Save Movie To List\" is clicked."))
        self.autoSaveCheckBox.setChecked(False)
        self.autoCloseCheckBox.setText(_translate("OptionsForm", "Auto close movie window when movie is saved."))
        self.autoCloseCheckBox.setChecked(False)
        self.customMovieFormatCheckBox.setText(_translate("OptionsForm", "Use custom format for movie save."))
        self.customMovieFormatCheckBox.setChecked(False)
        self.customFormatPlainTextEdit.setPlainText(_translate("OptionsForm", "For Example:\n"
        "\n"
        "\'[ {Title} | ⌚ {Runtime} | ⭐ {Genre} | 📅 {Released} | {Rated} ]\n"
        "\n"
        "OR\n"
        "\n"
        "           (IMDB): {imdbID}\n"
        "             Name: {Title}\n"
        "        Duration: {Runtime} ⌚\n"
        "Release Date: {Released} 📅\n"
        "            Rated: {Rated}\n"
        "\n"
        "OR\n"
        "\n"
        "The movies name is {Title} and it runs for {Runtime} long. The rating is amazing at {Rating} stars in IMDB."))
        self.checkJsonListButton.setText(_translate("OptionsForm", "JSON Keys"))
        self.clearOptionsButton.setText(_translate("OptionsForm", "Clear Options"))
        
    def connect_buttons_manually(self):
        self.validateApiButton.clicked.connect(self.validate_api_button_click)
        self.saveButton.clicked.connect(self.save_options)
        self.checkJsonListButton.clicked.connect(self.available_json_list)
        self.clearOptionsButton.clicked.connect(self.clear_options)
        self.customFormatPlainTextEdit.textChanged.connect(self.show_format_text)
        self.customMovieFormatCheckBox.stateChanged.connect(self.custom_movie_format_checkbox)

    def validate_api_button_click(self):
        api_Key = self.apiLineEdit.text().strip()
        request_url = 'https://www.omdbapi.com/?apikey=' + api_Key
        result = requests.get(request_url).json()
        if(result['Error'] == 'Incorrect IMDb ID.'):
            self.validateApiLabel.setText('<font color="green">Valid API key!</font>')
        if(result['Error'] == 'Invalid API key!'):
            self.validateApiLabel.setText('<font color="red">Invalid API key!</font>')
        
    def custom_movie_format_checkbox(self):
        if (self.customMovieFormatCheckBox.isChecked()):
            self.checkJsonListButton.setEnabled(True)
            self.customFormatPlainTextEdit.setEnabled(True)
            self.customFormatResultsPlainTextEdit.setEnabled(True)
        else:
            self.checkJsonListButton.setEnabled(False)
            self.customFormatPlainTextEdit.setEnabled(False)
            self.customFormatResultsPlainTextEdit.setEnabled(False)
    
    def available_json_list(self):
        self.json_format_window = QtWidgets.QWidget()
        self.json_format_window_ui = Ui_JsonFormatForm()
        self.json_format_window_ui.setupUi(self.json_format_window)
        self.json_format_window.show()
            
    def show_format_text(self):
        custom_format_text = self.customFormatPlainTextEdit.toPlainText()
        tokens = re.split(r'\{(.*?)\}', custom_format_text)
        keywords = tokens[1::2]
        try:
            values = {k:self.movie.get(k, '') for k in keywords}
            self.customFormatResultsPlainTextEdit.setPlainText(custom_format_text.format(**values))
        except (ValueError):
            pass
    
    def load_options(self):
        if (self.settings.value('api_key')):
            self.apiLineEdit.setText(self.settings.value('api_key'))
        if (self.settings.value('auto_save_check_box')):
            self.autoSaveCheckBox.setChecked(self.value_to_bool(self.settings.value('auto_save_check_box')))
        if (self.settings.value('auto_close_check_box')):
            self.autoCloseCheckBox.setChecked(self.value_to_bool(self.settings.value('auto_close_check_box')))
        if (self.settings.value('custom_format_check_box')):
            self.customMovieFormatCheckBox.setChecked(self.value_to_bool(self.settings.value('custom_format_check_box')))
        if (self.settings.value('custom_format_text')):    
            self.customFormatPlainTextEdit.setPlainText(self.settings.value('custom_format_text'))
    
    def save_options(self):
        self.settings.setValue('api_key', self.apiLineEdit.text().strip())
        self.settings.setValue('auto_save_check_box', self.autoSaveCheckBox.isChecked())
        self.settings.setValue('auto_close_check_box', self.autoCloseCheckBox.isChecked())
        self.settings.setValue('custom_format_check_box', self.customMovieFormatCheckBox.isChecked())
        self.settings.setValue('custom_format_text', self.customFormatPlainTextEdit.toPlainText())
        
        message_box = QMessageBox()
        message_box.setWindowTitle('Save Options')
        message_box.setText('Options has been saved.')
        message_box.setIcon(QMessageBox.Information)
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.exec_()
        
    def clear_options(self):
        self.settings.clear()
        self.retranslateUi(self.options_form)
        
    def value_to_bool(self, value):
        return value.lower() == 'true' if isinstance(value, str) else bool(value)
        

class Ui_JsonFormatForm(QWidget):
    
    def __init__(self):
        super().__init__()
        
    def setupUi(self, JsonFormatForm):
        JsonFormatForm.setObjectName("JsonFormatForm")
        JsonFormatForm.resize(713, 633)
        JsonFormatForm.setMinimumSize(QtCore.QSize(713, 633))
        JsonFormatForm.setMaximumSize(QtCore.QSize(713, 633))
        self.jsonPlainTextEdit = QtWidgets.QPlainTextEdit(JsonFormatForm)
        self.jsonPlainTextEdit.setGeometry(QtCore.QRect(10, 80, 691, 541))
        self.jsonPlainTextEdit.setObjectName("jsonPlainTextEdit")
        self.firstLabel = QtWidgets.QLabel(JsonFormatForm)
        self.firstLabel.setGeometry(QtCore.QRect(10, 10, 691, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.firstLabel.setFont(font)
        self.firstLabel.setTextFormat(QtCore.Qt.AutoText)
        self.firstLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.firstLabel.setWordWrap(False)
        self.firstLabel.setObjectName("firstLabel")
        self.omdbApiLinkLabel = QtWidgets.QLabel(JsonFormatForm)
        self.omdbApiLinkLabel.setGeometry(QtCore.QRect(10, 40, 691, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.omdbApiLinkLabel.setFont(font)
        self.omdbApiLinkLabel.setTextFormat(QtCore.Qt.AutoText)
        self.omdbApiLinkLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.omdbApiLinkLabel.setWordWrap(False)
        self.omdbApiLinkLabel.setObjectName("omdbApiLinkLabel")
        self.omdbApiLinkLabel.setOpenExternalLinks(True)

        self.retranslateUi(JsonFormatForm)
        QtCore.QMetaObject.connectSlotsByName(JsonFormatForm)

    def retranslateUi(self, JsonFormatForm):
        _translate = QtCore.QCoreApplication.translate
        JsonFormatForm.setWindowTitle(_translate("JsonFormatForm", "Json Movie Keys Window"))
        self.jsonPlainTextEdit.setPlainText(_translate("JsonFormatForm", "{\n"
        "    \"Title\":\"The Shawshank Redemption\",\n"
        "    \"Year\":\"1994\",\n"
        "    \"Rated\":\"R\",\n"
        "    \"Released\":\"14 Oct 1994\",\n"
        "    \"Runtime\":\"142 min\",\n"
        "    \"Genre\":\"Drama\",\n"
        "    \"Director\":\"Frank Darabont\",\n"
        "    \"Writer\":\"Stephen King (short story \\\"Rita Hayworth and Shawshank Redemption\\\"),Frank Darabont (screenplay)\",\n"
        "    \"Actors\":\"Tim Robbins, Morgan Freeman, Bob Gunton, William Sadler\",\n"
        "    \"Plot\":\"Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.\",\n"
        "    \"Language\":\"English\",\n"
        "    \"Country\":\"USA\",\n"
        "    \"Awards\":\"Nominated for 7 Oscars. Another 21 wins & 36 nominations.\",\n"
        "    \"Poster\":\"https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg\",\n"
        "    \"Ratings\":  [\n"
        "                    {\n"
        "                        \"Source\":\"Internet Movie Database\",\n"
        "                        \"Value\":\"9.3/10\"\n"
        "                    },\n"
        "                    {\n"
        "                        \"Source\":\"Rotten Tomatoes\",\n"
        "                        \"Value\":\"91%\"\n"
        "                    },\n"
        "                    {\n"
        "                        \"Source\":\"Metacritic\",\n"
        "                        \"Value\":\"80/100\"\n"
        "                    }\n"
        "                ],\n"
        "    \"Metascore\":\"80\",\n"
        "    \"imdbRating\":\"9.3\",\n"
        "    \"imdbVotes\":\"2,367,380\",\n"
        "    \"imdbID\":\"tt0111161\",\n"
        "    \"Type\":\"movie\",\n"
        "    \"DVD\":\"15 Aug 2008\",\n"
        "    \"BoxOffice\":\"$28,699,976\",\n"
        "    \"Production\":\"Columbia Pictures, Castle Rock Entertainment\",\n"
        "    \"Website\":\"N/A\"\n"
        "}"))
        self.firstLabel.setText(_translate("JsonFormatForm", "All available keys to use for your custom format:"))
        self.omdbApiLinkLabel.setText(_translate("JsonFormatForm", '<a href="http://www.omdbapi.com/">Link To Example For API </a>'))