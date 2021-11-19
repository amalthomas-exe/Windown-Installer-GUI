from PyQt5.QtWidgets import QDialog
from pages.showSummary import *

class ShowSummary(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.labelmode = self.ui.labelInstallMode
        self.proceedToInstall = self.ui.pushButtonProceed
        self.show()

