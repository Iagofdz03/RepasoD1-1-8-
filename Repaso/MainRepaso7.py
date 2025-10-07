# MainRepaso7.py
# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from Repaso7 import Ui_MainWindow  # importa la interfaz generada por Qt Designer

class MainRepaso7(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conectamos señales de prueba
        self.ui.lineEdit.textChanged.connect(self.mostrar_texto)
        self.ui.spinBox.valueChanged.connect(self.mostrar_valor_spin)
        self.ui.doubleSpinBox.valueChanged.connect(self.mostrar_valor_double)

    def mostrar_texto(self, texto):
        print(f"Texto cambiado: {texto}")

    def mostrar_valor_spin(self, valor):
        print(f"SpinBox cambiado: {valor}")

    def mostrar_valor_double(self, valor):
        print(f"DoubleSpinBox cambiado: {valor}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainRepaso7()
    window.show()
    sys.exit(app.exec())
