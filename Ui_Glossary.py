# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Glossary.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Glossary(object):
    def setupUi(self, Glossary):
        Glossary.setObjectName("Glossary")
        Glossary.setWindowModality(QtCore.Qt.WindowModal)
        Glossary.resize(1018, 520)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Glossary.sizePolicy().hasHeightForWidth())
        Glossary.setSizePolicy(sizePolicy)
        Glossary.setSizeGripEnabled(False)
        Glossary.setModal(False)
        self.label = QtWidgets.QLabel(Glossary)
        self.label.setGeometry(QtCore.QRect(460, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(2)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Glossary)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 1001, 391))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setLineWidth(3)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.glossaryClose = QtWidgets.QPushButton(Glossary)
        self.glossaryClose.setGeometry(QtCore.QRect(460, 480, 81, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.glossaryClose.setFont(font)
        self.glossaryClose.setObjectName("glossaryClose")

        self.retranslateUi(Glossary)
        self.glossaryClose.clicked.connect(Glossary.closeGlossary)
        QtCore.QMetaObject.connectSlotsByName(Glossary)

    def retranslateUi(self, Glossary):
        _translate = QtCore.QCoreApplication.translate
        Glossary.setWindowTitle(_translate("Glossary", "Glossary"))
        self.label.setText(_translate("Glossary", "Glossary"))
        self.label_2.setText(_translate("Glossary", "<html><head/><body><p>Allow Any : Anyone logged in from anywhere<br/><br/>Allow Inactive : Users logged in remotely<br/><br/>Allow Active : Users logged in at a system terminal</p><p><br/></p><p>no : Not authorized.<br/><br/>yes : Authorized.<br/><br/>auth_self : Authentication by the owner of the session that the client originates from is required.<br/><br/>auth_admin : Authentication by an administrative user is required.<br/><br/>auth_self_keep : Like auth_self but the authorization is kept for a brief period.<br/><br/>auth_admin_keep : Like auth_admin but the authorization is kept for a brief period.</p></body></html>"))
        self.glossaryClose.setText(_translate("Glossary", "Close"))

