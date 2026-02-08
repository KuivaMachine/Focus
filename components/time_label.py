from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel
import itertools

class TimeLabel(QLabel):
    fontChanged = pyqtSignal()
    def __init__(self, time_font):
        super().__init__()
        self.setFixedSize(170,70)
        self.setAlignment(Qt.AlignCenter)
        self.set_background_transparency(0.5)
        # Словарь с оптимальными размерами шрифтов для разного количества символов
        self.font_sizes = {
            "PT Mono": {5: 28, 6: 25},
            "MMHBounce": {5: 28, 6: 22},
            "Monte Summa C": {5: 34, 6: 30},
            "Hexcore": {5: 34, 6: 32},
            "Type Light Sans": {5: 32, 6: 26},
            "Audex": {5: 30, 6: 24},
            "Leporid": {5: 34, 6: 30},
            "Divagon": {5: 32, 6: 26},
            "BUSE letters 16х8": {5: 28, 6: 25},
            "SK Nigar RUS": {5: 32, 6: 30},
            "Tilda Grande": {5: 34, 6: 30},
            "Screpka": {5: 44, 6: 44},
            "Goudy Old Style Bold": {5:34, 6: 30},
            "OpenLukyanov": {5: 26, 6: 23},
            "Manasco (sherbackoffalex)": {5: 24, 6: 20},
            "Educational Gothic": {5: 34, 6: 30},
            "Genzsch Antiqua Bold": {5: 28, 6: 26},
            "HYWenHei": {5: 26, 6: 22},
            "Stengazeta": {5: 34, 6: 32},
            "NeeNoo": {5: 28, 6: 24},
            "Kvadrat": {5: 28, 6: 24},
            "Strogo": {5: 26, 6: 22},
            "Belarus": {5: 34, 6: 30},
            "Quantor": {5: 26, 6: 20},
        }

        self.font_list = list(self.font_sizes.keys())
        self.time_font = time_font if time_font in self.font_list else "PT Mono"
        self.font_cycle = itertools.cycle(self.font_list)

        # Синхронизируем цикл с текущим шрифтом
        current_font = next(self.font_cycle)
        while current_font != self.time_font :
            current_font = next(self.font_cycle)

    def setText(self, text):
        super().setText(text)
        # Устанавливаем шрифт
        font = QFont(self.time_font, self.font_sizes[self.time_font][len(text)])
        font.setBold(True)
        self.setFont(font)

    def set_background_transparency(self, value):
        """Значение должно быть от 0.0 до 1.0"""
        self.setStyleSheet(f"""
                                QLabel {{
                                    padding: 10px 10px;
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
            self.time_font = next_font
            font = QFont(self.time_font, self.font_sizes[self.time_font][len(self.text())])
            font.setBold(True)
            self.setFont(font)
            self.fontChanged.emit()
        super().mousePressEvent(event)