# MainRepaso6.py
# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from Repaso5 import Ui_MainWindow  # Importa la interfaz generada por Qt Designer

class MainRepaso6(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Opcional: conectar los botones a funciones para probar
        self.ui.pushButton.clicked.connect(lambda: print("Botón 1 pulsado"))
        self.ui.pushButton_2.clicked.connect(lambda: print("Botón 2 pulsado"))
        self.ui.pushButton_3.clicked.connect(lambda: print("Botón 3 pulsado"))
        self.ui.pushButton_4.clicked.connect(lambda: print("Botón 4 pulsado"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainRepaso6()
    window.show()
    sys.exit(app.exec())
