# MainRepaso8.py
# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from Repaso8 import Ui_MainWindow  # Importa tu clase generada por Qt Designer

class MainRepaso8(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conexión de botones con las capas del stackedWidget
        self.ui.pushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButton_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainRepaso8()
    window.show()
    sys.exit(app.exec())
