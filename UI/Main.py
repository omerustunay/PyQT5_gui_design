from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow,  QAction
import sys
from PyQt5.QtGui import QIcon

from UI import DocDB
from UI.DocDB import DocDB
from UI.OpenFile import OpenFile


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "DDVT"
        self.top = 200
        self.left = 300
        self.width = 680
        self.height = 480
        self.setWindowIcon(QtGui.QIcon("../icon/logo_ddvt.jpg"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.CreateMenu()
        self.show()

    def CreateMenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")

        docAddAction = QAction(QIcon("../icon/docAdd.png"), 'Dokuman Ekle', self)
        docAddAction.setShortcut("Ctrl+C")
        docAddAction.triggered.connect(self.docAddWindow)
        fileMenu.addAction(docAddAction)

        docInfoAction = QAction(QIcon("../icon/docInfo.png"), "Eklenen Dokumanlar", self)
        docInfoAction.triggered.connect(self.docInfoWindow)
        docInfoAction.setShortcut("Ctrl+S")
        fileMenu.addAction(docInfoAction)

        icon = QIcon("../icon/exit.png")
        exiteAction = QAction(icon, "Exit", self)
        exiteAction.setShortcut("Ctrl+E")
        exiteAction.triggered.connect(self.exitWindow)
        fileMenu.addAction(exiteAction)

        self.toolbar = self.addToolBar('Toolbar')
        self.toolbar.setMovable(False)
        self.toolbar.addAction(docAddAction)
        self.toolbar.addAction(docInfoAction)
        self.toolbar.addAction(exiteAction)

    def exitWindow(self):
        self.close()

    def docInfoWindow(self):
        self.dlg2 = DocDB()
        self.dlg2.show()

    def docAddWindow(self):
        dlg = OpenFile()
        dlg.exec_()



App = QApplication(sys.argv)
window = Main()
sys.exit(App.exec())