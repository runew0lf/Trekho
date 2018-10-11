# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_dlgTrekho(object):
    def setupUi(self, dlgTrekho):
        dlgTrekho.setObjectName("dlgTrekho")
        dlgTrekho.setEnabled(True)
        dlgTrekho.resize(400, 300)
        self.listboxFiles = QtWidgets.QListWidget(dlgTrekho)
        self.listboxFiles.setGeometry(QtCore.QRect(10, 10, 271, 211))
        self.listboxFiles.setObjectName("listboxFiles")
        self.listboxFiles.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.btnAdd = QtWidgets.QPushButton(dlgTrekho)
        self.btnAdd.setGeometry(QtCore.QRect(310, 20, 75, 23))
        self.btnAdd.setObjectName("btnAdd")
        self.btnRemove = QtWidgets.QPushButton(dlgTrekho)
        self.btnRemove.setGeometry(QtCore.QRect(310, 50, 75, 23))
        self.btnRemove.setObjectName("btnRemove")
        self.btnExit = QtWidgets.QPushButton(dlgTrekho)
        self.btnExit.setGeometry(QtCore.QRect(310, 260, 75, 23))
        self.btnExit.setObjectName("btnExit")
        self.line = QtWidgets.QFrame(dlgTrekho)
        self.line.setGeometry(QtCore.QRect(300, 80, 91, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btnStart = QtWidgets.QPushButton(dlgTrekho)
        self.btnStart.setGeometry(QtCore.QRect(310, 110, 75, 23))
        self.btnStart.setDefault(False)
        self.btnStart.setFlat(False)
        self.btnStart.setObjectName("btnStart")
        self.btnStop = QtWidgets.QPushButton(dlgTrekho)
        self.btnStop.setGeometry(QtCore.QRect(310, 140, 75, 23))
        self.btnStop.setObjectName("btnStop")

        self.retranslateUi(dlgTrekho)
        QtCore.QMetaObject.connectSlotsByName(dlgTrekho)

    def retranslateUi(self, dlgTrekho):
        _translate = QtCore.QCoreApplication.translate
        dlgTrekho.setWindowTitle(_translate("dlgTrekho", "Trekho"))
        self.btnAdd.setText(_translate("dlgTrekho", "Add"))
        self.btnRemove.setText(_translate("dlgTrekho", "Remove"))
        self.btnExit.setText(_translate("dlgTrekho", "Exit"))
        self.btnStart.setText(_translate("dlgTrekho", "Start"))
        self.btnStop.setText(_translate("dlgTrekho", "Stop"))
