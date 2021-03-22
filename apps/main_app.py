from PyQt5 import QtWidgets
from src.forms import main_window
from apps.Config import CONSTANTS
from PyQt5.QtGui import QIcon

class Main_App(QtWidgets.QMainWindow, main_window.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.setupUiFeatures()  # добавление в дизайн новых фичей


    def setupUiFeatures(self):
        self.setWindowIcon(QIcon(CONSTANTS.ICON_PATH))
        self.setFixedSize(self.size())

    def __connectHandler(self):
        pass
