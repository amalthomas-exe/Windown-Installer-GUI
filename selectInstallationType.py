from PyQt5.QtWidgets import QDialog
from pages.selectInstallationType import *

class SelectInstallationType(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.radiokeep = self.ui.radioButtonKeepFiles
        self.reinstall = self.ui.radioButtonReinstall
        self.buttonNext = self.ui.pushButtonNext
        self.show()


    