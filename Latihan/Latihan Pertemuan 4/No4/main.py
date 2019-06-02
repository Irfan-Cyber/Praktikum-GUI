import sys
from PyQt5.QtWidgets import QApplication

from latian4Main import*

if __name__ == '__main__':
    a = QApplication(sys.argv)

    minform = latian4Other()
    minform.show()

    a.exec()
