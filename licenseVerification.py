from PyQt5.QtWidgets import QDialog
from pages.licenceActivation import *

class LicenseVerification(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.nextButton = self.ui.pushButtonNext
        self.labelincorrect = self.ui.labelIncorrectCode
        self.quit = self.ui.pushButtonQuit
        self.show()
    def verify(self):
        codeList = [self.ui.lineEditCode1.text(),self.ui.lineEditCode2.text(),self.ui.lineEditCode3.text(),self.ui.lineEditCode4.text(),self.ui.lineEditCode5.text()]
        activationCode = "-".join(codeList)
        return activationCode