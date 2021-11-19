from PyQt5.QtWidgets import QDialog
from pages.licenseAgreementPage import *

class LicenseArgeement(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.pushAgree = self.ui.pushButtonAgree
        self.pushDeny = self.ui.pushButtonDeny
        self.show()
    
