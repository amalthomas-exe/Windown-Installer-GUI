from PyQt5.QtWidgets import QDialog
from pages.finalMessagePage import *

class FinalMessage(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.buttonRestart = self.ui.pushButton
        self.buttonQuit = self.ui.pushButtonQuit
        self.show()
