from PyQt5.QtWidgets import QPushButton


class ServiceButton(QPushButton):
    def __init__(self, text, width):
        super().__init__()
        self.setFixedSize(width, 30)
        self.setText(text)
        self.setStyleSheet("""
        QPushButton {
            font-size: 18px;
            font-weight: light;
            font-family: 'PT Mono';
            color: white;
             background-color: rgba(0, 0, 0, 0.3);
            border-radius: 15px;
            padding: 3px;
            
        }
        QPushButton:hover{
            background-color: rgba(0, 0, 0, 0.5);
        }
        QPushButton:pressed{
            background-color: rgba(0, 0, 0, 0.9);
        }
        """)
