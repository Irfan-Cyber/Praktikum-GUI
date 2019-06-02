import sys
from PyQt5.QtWidgets import QApplication

from FromSederhana import*

if __name__ == '__main__':
    a = QApplication(sys.argv)

    minform = FromSederhana()
    minform.show()

    a.exec()
