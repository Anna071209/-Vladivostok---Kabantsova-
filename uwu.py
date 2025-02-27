import sys
import random

from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QPainter, QColor, QPolygonF
from PyQt6.QtCore import QPointF, QRectF, Qt


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('oi.ui', self)
        self.button.clicked.connect(self.paintEvent)

    def paintEvent(self, event):
        painter = QPainter(self)
        self.current_size = random.randint(20, 100)
        painter.setBrush(QColor(255, 255, 0))
        painter.drawEllipse(QPointF(200, 200), self.current_size, self.current_size,)
        self.update()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Suprematism()
    window.show()
    sys.exit(app.exec())