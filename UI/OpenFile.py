

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QTextEdit

class OpenFile(QFileDialog):
    def __init__(self, *args, **kwargs):
        super(OpenFile, self).__init__(*args, **kwargs)

        self.title = "PyQt5 Open File"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300

        self.InitWindow()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("../icon/logo_ddvt.jpg"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()

        self.btn1 = QPushButton("Open Image")
        # self.btn1.clicked.connect(self.getImage)
        self.close()








