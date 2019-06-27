# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenghitungLuas.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(502, 331)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 171, 131))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 171, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.RadioPersegi = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.RadioPersegi.setFont(font)
        self.RadioPersegi.setObjectName("RadioPersegi")
        self.verticalLayout.addWidget(self.RadioPersegi)
        self.radioPersegiPanjang = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.radioPersegiPanjang.setFont(font)
        self.radioPersegiPanjang.setObjectName("radioPersegiPanjang")
        self.verticalLayout.addWidget(self.radioPersegiPanjang)
        self.radioJajarGenjang = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.radioJajarGenjang.setFont(font)
        self.radioJajarGenjang.setObjectName("radioJajarGenjang")
        self.verticalLayout.addWidget(self.radioJajarGenjang)
        self.radioBelahKetupat = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.radioBelahKetupat.setFont(font)
        self.radioBelahKetupat.setObjectName("radioBelahKetupat")
        self.verticalLayout.addWidget(self.radioBelahKetupat)
        self.radioTrapesium = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.radioTrapesium.setFont(font)
        self.radioTrapesium.setObjectName("radioTrapesium")
        self.verticalLayout.addWidget(self.radioTrapesium)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(260, 20, 221, 151))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.lblPjg = QtWidgets.QLabel(self.groupBox_2)
        self.lblPjg.setGeometry(QtCore.QRect(10, 10, 61, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lblPjg.setFont(font)
        self.lblPjg.setObjectName("lblPjg")
        self.lblLbr = QtWidgets.QLabel(self.groupBox_2)
        self.lblLbr.setGeometry(QtCore.QRect(10, 50, 51, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lblLbr.setFont(font)
        self.lblLbr.setObjectName("lblLbr")
        self.lblTingi = QtWidgets.QLabel(self.groupBox_2)
        self.lblTingi.setGeometry(QtCore.QRect(10, 100, 51, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lblTingi.setFont(font)
        self.lblTingi.setObjectName("lblTingi")
        self.linePanjang = QtWidgets.QLineEdit(self.groupBox_2)
        self.linePanjang.setGeometry(QtCore.QRect(10, 30, 201, 20))
        self.linePanjang.setObjectName("linePanjang")
        self.lineLebar = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineLebar.setGeometry(QtCore.QRect(10, 70, 201, 20))
        self.lineLebar.setObjectName("lineLebar")
        self.lineTinggi = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineTinggi.setGeometry(QtCore.QRect(10, 120, 201, 20))
        self.lineTinggi.setObjectName("lineTinggi")
        self.btnhitung = QtWidgets.QPushButton(self.centralwidget)
        self.btnhitung.setGeometry(QtCore.QRect(350, 250, 121, 20))
        self.btnhitung.setObjectName("btnhitung")
        self.labelHasil = QtWidgets.QLabel(self.centralwidget)
        self.labelHasil.setGeometry(QtCore.QRect(270, 180, 211, 21))
        self.labelHasil.setText("")
        self.labelHasil.setObjectName("labelHasil")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(275, 250, 71, 20))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 502, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.btnhitung.clicked.connect(self.hitung)
        self.pushButton.clicked.connect(self.clear)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Pilih Bangun Datar :"))
        self.RadioPersegi.setText(_translate("MainWindow", "Persegi"))
        self.radioPersegiPanjang.setText(_translate("MainWindow", "Persegi Panjang"))
        self.radioJajarGenjang.setText(_translate("MainWindow", "Jajar Genjang"))
        self.radioBelahKetupat.setText(_translate("MainWindow", "Belah Ketupat"))
        self.radioTrapesium.setText(_translate("MainWindow", "Trapesium"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Masukkan Angka :"))
        self.lblPjg.setText(_translate("MainWindow", "Panjang : (cm)"))
        self.lblLbr.setText(_translate("MainWindow", "Lebar : (cm)"))
        self.lblTingi.setText(_translate("MainWindow", "Tinggi : (cm)"))
        self.btnhitung.setText(_translate("MainWindow", "Hitung"))
        self.pushButton.setText(_translate("MainWindow", "Refresh"))


    def hitung(self):

        x = self.linePanjang.text()
        y = self.lineLebar.text()
        z = self.lineTinggi.text()


        if self.RadioPersegi.isChecked():
            panjang = eval(x)
            luasP = panjang * panjang
            self.labelHasil.setText('Hasilnya adalah :' + str(luasP))

        elif self.radioPersegiPanjang.isChecked():
            panjang = eval(x)
            lebar = eval(y)
            luasPP = panjang * lebar
            self.labelHasil.setText('Hasilnya adalah :' + str(luasPP))

        elif self.radioBelahKetupat.isChecked():
            panjang = eval(x)
            lebar = eval(y)
            luasBK = 0.5 * panjang * lebar
            self.labelHasil.setText('Hasilnya adalah :' + str(luasBK))


        elif self.radioTrapesium.isChecked():
            panjang = eval(x)
            lebar = eval(y)
            tinggi = eval(z)
            luasTP = (panjang + lebar)*tinggi/2
            self.labelHasil.setText('Hasilnya adalah :' + str(luasTP))


        elif self.radioJajarGenjang.isChecked():
            panjang = eval(x)
            tinggi = eval(z)
            luasJG = panjang * tinggi
            self.labelHasil.setText('Hasilnya adalah :' + str(luasJG) + ' cm2')


        else:
            self.labelHasil.setText('ANDA HARUS MEMILIH SALAH SATU BANGUN DATA')

    def clear(self):
        self.lineLebar.setText("")
        self.lineTinggi.setText("")
        self.linePanjang.setText("")
        self.labelHasil.setText("")
        if self.radioTrapesium.isChecked():
            self.lblPjg.setText('Sisi atas :')
            self.lblLbr.setText('Sisi bawah :')
        elif self.radioBelahKetupat.isChecked():
            self.lblPjg.setText('Diagonal 1 :')
            self.lblLbr.setText('Diagonal 2 :')
        elif self.radioJajarGenjang.isChecked():
            self.lblPjg.setText('Alas :')
        else:
            self.lblPjg.setText('Panjang :')
            self.lblLbr.setText('Lebar :')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
