
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(458, 146)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 30, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.hallo = QtWidgets.QPushButton(Form)
        self.hallo.setGeometry(QtCore.QRect(175, 80, 56, 17))
        self.hallo.setObjectName("hallo")
        self.NameEdit = QtWidgets.QLineEdit(Form)
        self.NameEdit.setGeometry(QtCore.QRect(110, 50, 251, 16))
        self.NameEdit.setObjectName("NameEdit")
        self.clear = QtWidgets.QPushButton(Form)
        self.clear.setGeometry(QtCore.QRect(240, 80, 51, 16))
        self.clear.setObjectName("clear")
        self.exit = QtWidgets.QPushButton(Form)
        self.exit.setGeometry(QtCore.QRect(210, 120, 56, 17))
        self.exit.setObjectName("exit")

        self.retranslateUi(Form)
        self.exit.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Masukkan Nama Anda:"))
        self.hallo.setText(_translate("Form", "Hallo"))
        self.clear.setText(_translate("Form", "Clear"))
        self.exit.setText(_translate("Form", "Exit"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
