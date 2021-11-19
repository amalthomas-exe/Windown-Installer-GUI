import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication
from pages.initialMessagePage import *
import psutil
import time
import platform
from licenseVerification import LicenseVerification
from licenseAgreement import LicenseArgeement
from selectInstallationType import SelectInstallationType
from showSummary import ShowSummary
from downloadAndInstall import DownloadAndInstall
from finalMessage import FinalMessage
from quitInstall import QuitWindow
import resources.resource
import webbrowser

class MainWindow(QDialog): #initialise the Qt5 GUI
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonInitialNext.clicked.connect(self.proceedToLicenseActivation)
        self.ui.pushButtonQuit.clicked.connect(self.quitPage)
        self.checkRequirements()
        self.show()

    def checkRequirements(self): #Check whether the PC meets the minimum system requirements
        processorCorrect = True
        enoughMemory = True
        warningMessage = "This PC does not meet the minimum system requirements to run Windows 11.\n\n Please restart the utility after fulfilling the following hardware requirement(s):\n"
        if not(platform.machine() in ["x86_64","AMD64"]): #whether the processor is 64 bit.
            processorCorrect = False
            warningMessage+="* This PC is using a 32 bit processor . Windows 11 only supports 64 bit processors('x86_64','AMD64').\n"

        if psutil.virtual_memory()[0]/1000000000 < 4: # whether the PC has enough RAM
            enoughMemory = False
            warningMessage+="* This PC does not have enough memory. Windows 11 requires memory greater than 4GB to operate properly."

        if not(processorCorrect) or not(enoughMemory): #if any of the requirements is not satisfied
            self.ui.labelInitialMessageTitle.setStyleSheet(r"QLabel{color: red}")
            self.ui.labelInitialMessageTitle.setText("Warning")
            self.ui.labelInitialMessage.setText(warningMessage)

        else: #No requirement issues. Can proceed with the installation
            self.ui.labelInitialMessageTitle.setStyleSheet(r"QLabel{color: rgb(60, 96, 255)}")
            self.ui.labelInitialMessageTitle.setText("Welcome")
            self.ui.labelInitialMessage.setText("This installer will guide you through the various steps to install Windows 11.")
    
    def proceedToLicenseActivation(self): # Proceed to license verification
        pages.setCurrentIndex(pages.currentIndex() + 1)
        licenseverification.nextButton.clicked.connect(self.verifyLicense)
        licenseverification.quit.clicked.connect(self.quitPage)

    def verifyLicense(self):
        '''
        License key verification. Typically we can download an encrypted file with the valid keys and check the entered key against valid keys.
        If the key is valid, it will proceed to the license agreement page.
        '''
        if licenseverification.verify()=="----": 
            pages.setCurrentIndex(pages.currentIndex() + 1) #go to the license agreement page
            licensewindow.pushAgree.clicked.connect(self.selectinstalltype)
            licensewindow.pushDeny.clicked.connect(self.quitPage)
        else:
            print("error") 
            licenseverification.labelincorrect.setText("Incorrect License Code") 

    def selectinstalltype(self): #go to the select installation type page
        pages.setCurrentIndex(pages.currentIndex() + 1) 
        selectinstalltype.radiokeep.toggled.connect(self.getInstallType)
        selectinstalltype.reinstall.toggled.connect(self.getInstallType)
        selectinstalltype.buttonNext.clicked.connect(self.showSummary)

    def getInstallType(self): #function to return the selected install type
        if selectinstalltype.radiokeep.isChecked()==True:
            return "keep"
        else:
            return "reinstall"
    def showSummary(self): #show summary with the selected install type
        pages.setCurrentIndex(pages.currentIndex() + 1)
        if self.getInstallType() =="keep":
            showsummary.labelmode.setText("Keep files and folders")
        else:
            showsummary.labelmode.setText("Delete everything")

        showsummary.proceedToInstall.clicked.connect(self.proceedToInstall)

    def proceedToInstall(self): #proceed to installation
        print("clicked")
        pages.setCurrentIndex(pages.currentIndex() + 1)
        downloadandinstall.quit.clicked.connect(self.quitPage)
        self.downloadAndInstall()

    def downloadAndInstall(self): 
        """boiler script depicting a dowload and install process. The required logic to download and install the installation files can be inserted here"""
        x = 0
        while x < 100:
            x+=0.00001
            downloadandinstall.progressDownload.setValue(x)
        y=0
        while y < 100:
            y+=0.00001
            downloadandinstall.progressInstall.setValue(y)
        pages.setCurrentIndex(pages.currentIndex() + 1)
        self.finalmessage()

    def finalmessage(self):
        finalmessage.buttonRestart.clicked.connect(self.rickRoll)
        
    def rickRoll(self):
        webbrowser.get().open("https://www.youtube.com/watch?v=dQw4w9WgXcQ") #Never gonna give you up :)"

    def quitPage(self):
        print("Clicked")
        pages.setCurrentIndex(7)
        quit.quit.clicked.connect(self.quitapp)

    def quitapp(self):
        sys.exit()

if __name__=="__main__":
    app = QApplication(sys.argv)
    pages = QtWidgets.QStackedWidget()
    pages.setStyleSheet("background-color: white")
    pages.setWindowTitle("Windows Setup")
    quit = QuitWindow()
    mainwindow = MainWindow()
    licenseverification = LicenseVerification()
    licensewindow = LicenseArgeement()
    selectinstalltype = SelectInstallationType()
    showsummary = ShowSummary()
    downloadandinstall = DownloadAndInstall()
    finalmessage = FinalMessage()
    pages.addWidget(mainwindow)
    pages.addWidget(licenseverification)
    pages.addWidget(licensewindow)
    pages.addWidget(selectinstalltype)
    pages.addWidget(showsummary)
    pages.addWidget(downloadandinstall)
    pages.addWidget(finalmessage)
    pages.addWidget(quit)
    pages.setFixedWidth(691)
    pages.setFixedHeight(557)
    pages.show()
    sys.exit(app.exec_())