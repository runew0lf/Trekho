# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_dlgPyRun(object):
    def setupUi(self, dlgPyRun):
        dlgPyRun.setObjectName("dlgPyRun")
        dlgPyRun.setEnabled(True)
        dlgPyRun.resize(400, 300)
        self.listboxFiles = QtWidgets.QListWidget(dlgPyRun)
        self.listboxFiles.setGeometry(QtCore.QRect(10, 10, 271, 211))
        self.listboxFiles.setObjectName("listboxFiles")
        self.listboxFiles.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.btnAdd = QtWidgets.QPushButton(dlgPyRun)
        self.btnAdd.setGeometry(QtCore.QRect(310, 20, 75, 23))
        self.btnAdd.setObjectName("btnAdd")
        self.btnRemove = QtWidgets.QPushButton(dlgPyRun)
        self.btnRemove.setGeometry(QtCore.QRect(310, 50, 75, 23))
        self.btnRemove.setObjectName("btnRemove")
        self.btnExit = QtWidgets.QPushButton(dlgPyRun)
        self.btnExit.setGeometry(QtCore.QRect(310, 260, 75, 23))
        self.btnExit.setObjectName("btnExit")
        self.line = QtWidgets.QFrame(dlgPyRun)
        self.line.setGeometry(QtCore.QRect(300, 80, 91, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btnStart = QtWidgets.QPushButton(dlgPyRun)
        self.btnStart.setGeometry(QtCore.QRect(310, 110, 75, 23))
        self.btnStart.setDefault(False)
        self.btnStart.setFlat(False)
        self.btnStart.setObjectName("btnStart")
        self.btnStop = QtWidgets.QPushButton(dlgPyRun)
        self.btnStop.setGeometry(QtCore.QRect(310, 140, 75, 23))
        self.btnStop.setObjectName("btnStop")

        self.retranslateUi(dlgPyRun)
        QtCore.QMetaObject.connectSlotsByName(dlgPyRun)

    def retranslateUi(self, dlgPyRun):
        _translate = QtCore.QCoreApplication.translate
        dlgPyRun.setWindowTitle(_translate("dlgPyRun", "PyRun"))
        self.btnAdd.setText(_translate("dlgPyRun", "Add"))
        self.btnRemove.setText(_translate("dlgPyRun", "Remove"))
        self.btnExit.setText(_translate("dlgPyRun", "Exit"))
        self.btnStart.setText(_translate("dlgPyRun", "Start"))
        self.btnStop.setText(_translate("dlgPyRun", "Stop"))
