import sys

from PyQt5.QtWidgets import QApplication

from latian3Main import*

if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = latian3Main()
    form.show()
    a.exec_()
