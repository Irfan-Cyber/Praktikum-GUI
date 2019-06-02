import sys
from PyQt5.QtWidgets import QApplication

from latihan1 import*

if __name__ == '__main__':
    a = QApplication(sys.argv)

    minform = latihan1()
    minform.show()

    a.exec()
