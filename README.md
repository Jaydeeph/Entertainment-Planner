# Entertainment Planner
## Created using PYQT5, QT Designer, and Python. 

I created this because I had a movie list channel on my discord server with friends, and wanted an easier way to search and keep a list of movies. 
Therefore, I created this just to that.

## Images
![Main Window](/images/main_window.png)
![Movie Window](/images/movie_window.png)

C# version I created before I found out about PYQT:
**Link will be provided later**

## Prerequisites

### Have a virtual environment
```
python3 -m venv venv
source venv/bin/activate # or "call venv\Scripts\activate.bat" on Windows
```

### Install PyQt5
```
pip install PyQt5
pip install pyqt5-tools
```

### QT Designer
~~For some reason, pyqt5-tools didn't download the designer for me and no idea why it didn't work. So I downloaded it from here.~~
[QT Designer](https://build-system.fman.io/qt-designer-download)

Seems like the designer is in the '\Scripts\designer.exe'.
[Package Information](https://pypi.org/project/pyqt5-tools/)

### Convert .ui files to .py
Example:
```
pyuic5 -x .\MainWindow.ui -o .\Converted_MainWindow.py
```

## To Do:
- [x] Add options window to save personal API key. 
- [x] Add a Window to see all discord movie list.
- [ ] Add a list of movies and search movies by that.
- [ ] Add a way to export the discord movie list. 
- [ ] Add the ability to save the movies into different formats.
- [ ] Add TV-Series/Anime search options.

