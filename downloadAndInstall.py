from PyQt5.QtWidgets import QDialog
from pages.downloadAndInstallpage import *

class DownloadAndInstall(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.labeldownload = self.ui.labelDownloading
        self.progressDownload = self.ui.progressBarDownload
        self.labelinstall = self.ui.labelInstalling
        self.progressInstall = self.ui.progressBarInstall
        self.quit = self.ui.pushButtonQuit
        self.show()


        

