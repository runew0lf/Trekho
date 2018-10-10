from PyRun_UI import Ui_dlgPyRun
import sys
import os
import os.path
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAction, QMenu, QSystemTrayIcon, QStyle, qApp
from PyQt5.QtGui import QColor
from PyQt5.QtCore import pyqtSlot, Qt

import subprocess
from dotenv import load_dotenv


def getPythonPath(currentpath):
    for dirpath, dirnames, filenames in os.walk(currentpath):
        for filename in [f for f in filenames if f.lower() == "python.exe"]:
            return os.path.join(dirpath, filename)
    return "python"


class ApplicationWindow(QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_dlgPyRun()
        self.ui.setupUi(self)
        self.process_id = None
        self.originalBG = None

        # Add Capture Events for Buttons
        self.ui.btnExit.clicked.connect(self.on_btnExit)
        self.ui.btnAdd.clicked.connect(self.on_btnAdd)
        self.ui.btnRemove.clicked.connect(self.on_btnRemove)
        self.ui.btnStart.clicked.connect(self.on_btnStart)
        self.ui.btnStop.clicked.connect(self.on_btnStop)

        # Init QSystemTrayIcon
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(
            self.style().standardIcon(QStyle.SP_ComputerIcon))

        '''
            Define and add steps to work with the system tray icon
            show - show window
            hide - hide window
            exit - exit from application
        '''
        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        hide_action = QAction("Hide", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(qApp.quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        # Listview context menu
        self.ui.listboxFiles.setContextMenuPolicy(Qt.CustomContextMenu) 
        self.ui.listboxFiles.customContextMenuRequested.connect(self.showMenu)
    
    def showMenu(self, pos):
        menu = QMenu()
        quitAction = menu.addAction("Quit")
        action = menu.exec_(self.ui.listboxFiles.viewport().mapToGlobal(pos))
        if action == quitAction:
            pass


    # Override closeEvent, to intercept the window closing event
    # The window will be closed only if there is no check mark in the check box
    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.tray_icon.showMessage(
            "Tray Program",
            "Application was minimized to Tray",
            QSystemTrayIcon.Information,
            2000
        )

    def addFiles(self, files):
        files = map(lambda s: s.strip(), files)
        self.ui.listboxFiles.addItems(files)

    @pyqtSlot()
    def on_btnExit(self):
        self.tray_icon.hide()
        # Check to see if process is still running before we terminate it
        poll = self.process_id.poll()
        if poll is None:
            self.process_id.terminate()
        exit(0)

    @pyqtSlot()
    def on_btnStop(self):
        self.ui.listboxFiles.currentItem().setBackground(self.originalBG)
        # Check to see if process is still running before we terminate it
        poll = self.process_id.poll()
        if poll is None:
            self.process_id.terminate()
        print("Stopped")

    @pyqtSlot()
    def on_btnStart(self):
        print("started")
        self.originalBG = self.ui.listboxFiles.currentItem().background()

        full_path = str(self.ui.listboxFiles.currentItem().text())
        self.ui.listboxFiles.currentItem().setBackground(QColor('#7fc97f'))
        dir_path = os.path.dirname(os.path.abspath(full_path))
        std_out = open(f"{full_path}.log", "w")
        env_path = f"{dir_path}/.env"
        load_dotenv(dotenv_path=env_path)
        self.process_id = subprocess.Popen([f"{getPythonPath(dir_path)}",
                                            str(self.ui.listboxFiles.currentItem().text())],
                                           stdout=std_out,
                                           cwd=dir_path)

    @pyqtSlot()
    def on_btnRemove(self):
        a_list = self.ui.listboxFiles.selectedItems()
        for item in a_list:
            self.ui.listboxFiles.takeItem(self.ui.listboxFiles.row(item))
        with open("file.txt", "w") as fh:
            itemsTextList = [str(self.ui.listboxFiles.item(i).text())
                             for i in range(self.ui.listboxFiles.count())]
            fh.write("\n".join(itemsTextList))

    @pyqtSlot()
    def on_btnAdd(self):
        filename = self.openFileNameDialog()
        self.ui.listboxFiles.addItem(filename)
        with open("file.txt", "w") as fh:
            itemsTextList = [str(self.ui.listboxFiles.item(i).text())
                             for i in range(self.ui.listboxFiles.count())]
            fh.write("\n".join(itemsTextList))

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(
            self, "QFileDialog.getOpenFileName()", "", "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            return fileName


def main():
    with open("file.txt", "r") as fh:
        files = fh.readlines()
    app = QApplication(sys.argv)
    application = ApplicationWindow()
    application.addFiles(files)
    application.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        pass


if __name__ == "__main__":
    main()
