# MainRepaso66.py
# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from Repaso6 import Ui_MainWindow  # Importa tu clase generada

class MainRepaso66(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conectar los botones a funciones de prueba
        self.ui.pushButton.clicked.connect(lambda: print("Botón (0,0) pulsado"))
        self.ui.pushButton_4.clicked.connect(lambda: print("Botón (0,1) pulsado"))
        self.ui.pushButton_3.clicked.connect(lambda: print("Botón (0,2) pulsado"))
        self.ui.pushButton_2.clicked.connect(lambda: print("Botón (0,3) pulsado"))
        self.ui.pushButton_5.clicked.connect(lambda: print("Botón (1,0-3) pulsado"))
        self.ui.pushButton_6.clicked.connect(lambda: print("Botón (2,0-1) pulsado"))
        self.ui.pushButton_7.clicked.connect(lambda: print("Botón (2,2-3) pulsado"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainRepaso66()
    window.show()
    sys.exit(app.exec())
