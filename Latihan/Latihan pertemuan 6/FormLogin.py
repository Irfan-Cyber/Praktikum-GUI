import sys

from PyQt5.QtGui import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from FormPendaftaran import*

class MainForm (QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 100)
        self.move(300, 300)
        self.setWindowTitle('Kuis Pemograman GUI')
        self.Username = QLabel('Username')
        self.Pass = QLabel('Password')
        self.Username1 = QLineEdit()
        self.Pass1 = QLineEdit()
        self.Pass1.setEchoMode(QLineEdit.Password)
        self.buttLogin =QPushButton('Login')
        self.buttClear =QPushButton('Clear')

        layout =QGridLayout()
        layout.addWidget(self.Username)
        layout.addWidget(self.Username1, 0,1,1,2)
        layout.addWidget(self.Pass)
        layout.addWidget(self.Pass1, 1,1,1,2)
        layout.addWidget(self.buttLogin, 2,1)
        layout.addWidget(self.buttClear, 2,2)
        self.setLayout(layout)

        self.buttLogin.clicked.connect(self.buttonLogin)
        self.buttClear.clicked.connect(self.buttonClear)

    def buttonLogin(self):
        user = self.Username1.text()
        passwrd = self.Pass1.text()

        if not user or not passwrd :
            QMessageBox.information(self,'Perhatian!','Username atau Password Harus di Isi')
        else:
            if user == 'kukuhpr' and passwrd =='17104009':
                self.form = FormPendaftaran()
                self.form.show()
                self.close()
            else:
                QMessageBox.information(self,'Perhatian!','Username atau password Salah')

    def buttonClear (self):
            self.Username1.clear()
            self.Pass1.clear()

if __name__ =='__main__':
        a =QApplication(sys.argv)

        form =MainForm()
        form.show()

        a.exec_()
