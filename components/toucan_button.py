from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QPainterPath, QPen, QPixmap
from PyQt5.QtWidgets import QWidget



class ToucanButton(QWidget):
    clicked = pyqtSignal()

    def __init__(self, image_path):
        super().__init__()
        self.hover = False
        self.is_current = False
        self.toucan = QPixmap(image_path)
        self.setStyleSheet("""
                                QWidget{
                               background-color: #FFFFFF;
                               border: none;
                                padding: 0px;
                               }
                               """)

        self.setFixedSize(46, 46)



    def get_is_current(self):
        return self.is_current

    def set_is_current(self, is_current):
        self.is_current = is_current

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()
            self.is_current = True


    def handle_color_change(self):
        self.clicked.emit()
        self.update()

    def enterEvent(self, e):
        if not self.hover:
            self.hover = True
            self.update()
        super().enterEvent(e)

    def leaveEvent(self, e):
        if self.hover:
            self.hover = False
            self.update()
        super().leaveEvent(e)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Параметры квадрата
        square_size = 40
        corner_radius = 10
        x = (self.width() - square_size) // 2
        y = (self.height() - square_size) // 2
        border_width = 4 if self.hover else 3
        # Создаем скругленный квадрат
        square_path = QPainterPath()
        square_path.addRoundedRect(x, y, square_size, square_size, corner_radius, corner_radius)

        # Черная обводка
        pen = QPen(QColor("#000000" if not self.is_current else "#FFFFFF"))
        pen.setWidth(border_width)
        painter.setPen(pen)
        painter.setBrush(QColor("#FFCC00"))
        painter.drawRoundedRect(x, y, square_size, square_size, corner_radius, corner_radius)

        # Рисуем изображение
        if self.toucan:
            # Масштабируем под размер виджета
            scaled_pixmap = self.toucan.scaled(
                square_size, square_size,
                Qt.IgnoreAspectRatio,
                Qt.SmoothTransformation
            )
            painter.drawPixmap(x, y, scaled_pixmap)
