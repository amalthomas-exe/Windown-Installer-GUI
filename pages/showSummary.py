# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pages/showSummary.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(691, 557)
        Dialog.setStyleSheet("QDialog{\n"
"    background-color: white\n"
"}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 81, 61))
        self.label.setStyleSheet("QLabel{\n"
"    \n"
"    background-image: url(:/newPrefix/win11.png);\n"
"}")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/win11.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 40, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"    color: rgb(64, 64, 255)\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"    color:rgb(106, 141, 255)\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 170, 631, 191))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
"    color: black\n"
"}")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.labelInstallMode = QtWidgets.QLabel(Dialog)
        self.labelInstallMode.setGeometry(QtCore.QRect(40, 360, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelInstallMode.setFont(font)
        self.labelInstallMode.setStyleSheet("QLabel{\n"
"    color:black\n"
"}")
        self.labelInstallMode.setObjectName("labelInstallMode")
        self.pushButtonProceed = QtWidgets.QPushButton(Dialog)
        self.pushButtonProceed.setGeometry(QtCore.QRect(553, 499, 101, 31))
        self.pushButtonProceed.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 254, 226);\n"
"    border-radius: 0px;\n"
"    color: black;\n"
"    border: 1px dotted rgb(60,96,255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(60, 96, 255)\n"
"}")
        self.pushButtonProceed.setObjectName("pushButtonProceed")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 510, 141, 31))
        self.label_5.setStyleSheet("QLabel{\n"
"    \n"
"    background-image: url(:/newPrefix/microsoft.png);\n"
"}")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/newPrefix/microsoft.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(170, 510, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(250, 500, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Windows 11"))
        self.label_3.setText(_translate("Dialog", "Ready to install"))
        self.label_4.setText(_translate("Dialog", "You will be able to use your PC during downloading. However, before restarting your PC, it is recommended  save and close your files before you begin.\n"
"\n"
"Plug in your PC to be sure that your battery doesn\'t run down during the installation.\n"
"\n"
"In recap, you have chosen to\n"
"\n"
"Install Windows 11"))
        self.labelInstallMode.setText(_translate("Dialog", "Keep personal files and folders"))
        self.pushButtonProceed.setText(_translate("Dialog", "Proceed "))
        self.label_6.setText(_translate("Dialog", "<a style=\"color:black; text-decoration:none\" href=\"https://www.aka.ms/support\">Support</a>"))
        self.label_7.setText(_translate("Dialog", "<a style=\"color:black; text-decoration:none\" href=\"https://www.microsoft/en-us/legal\">Legal</a>"))

