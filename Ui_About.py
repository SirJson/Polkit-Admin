# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.setWindowModality(QtCore.Qt.NonModal)
        About.resize(400, 386)
        self.frame = QtWidgets.QFrame(About)
        self.frame.setGeometry(QtCore.QRect(9, 9, 381, 371))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 0, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setLineWidth(3)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 180, 361, 151))
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")
        self.closeAboutButton = QtWidgets.QPushButton(self.frame)
        self.closeAboutButton.setGeometry(QtCore.QRect(150, 340, 87, 29))
        self.closeAboutButton.setObjectName("closeAboutButton")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(120, 40, 151, 141))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("PKEIconV001.png"))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(About)
        self.closeAboutButton.clicked.connect(About.aboutClose)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About Polkit Explorer"))
        self.label.setText(_translate("About", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Polkit Explorer</span></p></body></html>"))
        self.label_2.setText(_translate("About", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Author : Kevin Cave.</span></p><p><span style=\" font-size:11pt; font-weight:600;\">Version : 1.0</span></p><p><span style=\" font-size:11pt; font-weight:600;\">Allows a user to load polkit-1 .policy files and explore their contents in a human-readable format.</span></p></body></html>"))
        self.closeAboutButton.setText(_translate("About", "Close"))

