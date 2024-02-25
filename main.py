import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.uic import loadUi


class CircleDrawer(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('UI.ui', self)
        self.setWindowTitle('Генератор окружностей')

        self.button_draw.clicked.connect(self.draw_circle)
        self.diameter = 0

    def paintEvent(self, event):
        painter = QPainter(self)
        color = QColor('yellow')
        painter.setBrush(color)
        painter.drawEllipse(50, 50, self.diameter, self.diameter)

    def draw_circle(self):
        self.diameter = random.randint(20, 100)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec_())
