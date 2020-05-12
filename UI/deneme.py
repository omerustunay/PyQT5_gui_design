from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3


class SearchDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(SearchDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Push Data")

        self.setWindowTitle("Eklemek istediginiz veriye bir isim veriniz")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.on_click)
        layout = QVBoxLayout()

        self.textbox = QLineEdit()

        #self.onlyInt = QIntValidator()
        #self.textbox.setValidator(self.onlyInt)
        self.textbox.setPlaceholderText("secili alanın ismini giriniz")
        layout.addWidget(self.textbox)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def on_click(self):
        text = ""
        text = self.textbox.text()
        QMessageBox.question(self, 'Ekleme İşlemi', "Eklendi: " + str(text), QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")
        #self.setVisible(False)

    def center(self):
        # geometry of the main window

        qr = self.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

         # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())