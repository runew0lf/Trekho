# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Python\Trekho\trek_log.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_dlgLogs(object):
    def setupUi(self, dlgLogs):
        dlgLogs.setObjectName("dlgLogs")
        dlgLogs.resize(475, 381)
        self.textEdit = QtWidgets.QTextEdit(dlgLogs)
        self.textEdit.setGeometry(QtCore.QRect(20, 10, 431, 331))
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                    "color: rgb(0, 170, 0);")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(dlgLogs)
        QtCore.QMetaObject.connectSlotsByName(dlgLogs)

    def retranslateUi(self, dlgLogs):
        _translate = QtCore.QCoreApplication.translate
        dlgLogs.setWindowTitle(_translate("dlgLogs", "Log Viewer"))
