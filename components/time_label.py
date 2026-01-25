from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel
import itertools

class TimeLabel(QLabel):
    fontChanged = pyqtSignal()
    def __init__(self, time_font):
        super().__init__()
        self.setFixedSize(170,70)
        self.time_font = time_font
        self.setAlignment(Qt.AlignCenter)
        self.set_background_transparency(0.5)
        font = QFont(time_font, 25)
        font.setBold(True)
        self.setFont(font)
        self.font_list=[
            "PT Mono",
            "HYWenHei",
            "Stengazeta",
            "Ringus-Regular"
        ]
        self.font_cycle = itertools.cycle(self.font_list)
        current_font = next(self.font_cycle)
        while current_font != time_font:
            current_font = next(self.font_cycle)

    def set_background_transparency(self, value):
        """Значение должно быть от 0.0 до 1.0"""
        self.setStyleSheet(f"""
                                QLabel {{
                                    padding: 10px 20px;
                                    color: #FFFFFF;
                                    border-radius: 35px;
                                    background-color: rgba(0, 0, 0, {value});
                                }}
                                """)

    def get_time_font(self):
        return self.time_font

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.RightButton:
            next_font = next(self.font_cycle)
            font = QFont(next_font, 25)
            font.setBold(True)
            self.setFont(font)
            self.time_font = next_font
            self.fontChanged.emit()
        super().mousePressEvent(event)