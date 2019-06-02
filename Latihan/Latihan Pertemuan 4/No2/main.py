import sys

from PyQt5.QtWidgets import QApplication

from latian2 import*

if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = latian2()
    form.show()
    a.exec_()
