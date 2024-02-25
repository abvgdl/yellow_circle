import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(560, 480)
        self.button_draw = QtWidgets.QPushButton(main_window)
        self.button_draw.setGeometry(QtCore.QRect(240, 230, 75, 23))
        self.button_draw.setObjectName("button_draw")

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "yellow_circles"))
        self.button_draw.setText(_translate("main_window", "PushButton"))


class CircleDrawer(QWidget, Ui_main_window):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.setWindowTitle('Генератор окружностей')

        self.button_draw.clicked.connect(self.draw_circle)
        self.diameter = 0
        self.color = QColor('white')

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(self.color)
        painter.drawEllipse(50, 50, self.diameter, self.diameter)

    def draw_circle(self):
        self.color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.diameter = random.randint(20, 100)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec_())
