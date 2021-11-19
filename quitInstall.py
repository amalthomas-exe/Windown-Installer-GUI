from PyQt5.QtWidgets import QDialog
from pages.quitPage import *

class QuitWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.quit = self.ui.pushButtonNext
        self.show()