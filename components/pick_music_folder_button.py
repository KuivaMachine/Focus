from PyQt5.QtWidgets import QPushButton

from components.hint_window import HintWidget


class PickMusicFolderButton(QPushButton):
    def __init__(self, root_window, text, width, hint_text):
        super().__init__()
        self.hint_text = hint_text
        self.root_window = root_window
        self.setFixedSize(width, 40)
        self.setText(text)
        self.setStyleSheet("""
        QPushButton {
         border: 1px solid white;
         text-align: center;
         border-radius: 20px;
         padding: 0px 10px;
         color: #E6E6E6;
         font-size: 15px;
         background-color: rgba(0, 0, 0, 0.3);
        }
        QPushButton::hover {
         background-color: rgba(0, 0, 0, 0.5);
         border: 2px solid white;
          padding: 0px 10px;
          text-align: center;
        }
        """)

    def enterEvent(self, e):
        self.hint = HintWidget(self.root_window, self.hint_text)
        self.hint.show()

    def leaveEvent(self, e):
        self.hint.close()
