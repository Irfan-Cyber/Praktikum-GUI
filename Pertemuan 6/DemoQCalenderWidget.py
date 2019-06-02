import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(400, 100)
        self.move(300, 300)
        self.setWindowTitle('Demo QCalenderWidget')

        self.calender = QCalendarWidget()
        self.calender.setGridVisible(True)
        self.calender.setHorizontalHeaderFormat(QCalendarWidget.LongDayNames)

        self.shortNamesCheck = QCheckBox('Nama Hari Pendek')

        self.dateEdit = QDateEdit()
        self.dateEdit.setDisplayFormat('dd/MM/yyyy')
        self.dateEdit.setDate(QDate.currentDate())

        self.setButton = QPushButton('Tentukan Tanggal')
        self.getButton = QPushButton('Ambil Tanggal')

        hbox = QHBoxLayout()
        hbox.addWidget(self.dateEdit)
        hbox.addWidget(self.setButton)
        hbox.addWidget(self.getButton)

        layout = QVBoxLayout()
        layout.addWidget(self.calender)
        layout.addWidget(self.shortNamesCheck)
        layout.addLayout(hbox)
        self.setLayout(layout)

        self.shortNamesCheck.clicked.connect(self.shortNamesCheckClick)
        self.setButton.clicked.connect(self.setButtonClick)
        self.getButton.clicked.connect(self.getButtonClick)

    def shortNamesCheckClick(self):
        if self.shortNamesCheck.clicked.connect(self.shortNamesCheckClick):
            self.calender.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
        else:
            self.calender.setHorizontalHeaderFormat(QCalendarWidget.LongDayNames)

    def setButtonClick(self):
        self.calender.setSelectedDate(self.dateEdit.date())

    def getButtonClick(self):
        QMessageBox.information(self,'Informasi',
        'Tanggal Aktif :' + self.calender.selectedDate().toString())

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
