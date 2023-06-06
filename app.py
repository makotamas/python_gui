import sys
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Minimal App")

        self.label = QLabel("Write your name:", self)
        self.label.move(20, 20)

        self.text_field = QLineEdit(self)
        self.text_field.move(20, 50)

        self.button = QPushButton("OK", self)
        self.button.move(20, 80)
        self.button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        text = self.text_field.text()
        print(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.setGeometry(100, 100, 200, 150)
    window.show()

    sys.exit(app.exec_())

