# MainRepaso9.py
# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from Repaso9 import Ui_MainWindow  # Importa la clase generada por Qt Designer

class MainRepaso9(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conectar las acciones del menú a sus funciones
        self.ui.actAbrir.triggered.connect(self.abrir_archivo)
        self.ui.actGuardar.triggered.connect(self.guardar_archivo)
        self.ui.actSalir.triggered.connect(self.salir_app)

    def abrir_archivo(self):
        """Abre un cuadro de diálogo para seleccionar un archivo."""
        archivo, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Todos los archivos (*)")
        if archivo:
            QMessageBox.information(self, "Archivo abierto", f"Has abierto:\n{archivo}")

    def guardar_archivo(self):
        """Abre un cuadro de diálogo para guardar un archivo."""
        archivo, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Todos los archivos (*)")
        if archivo:
            QMessageBox.information(self, "Archivo guardado", f"Archivo guardado como:\n{archivo}")

    def salir_app(self):
        """Cierra la aplicación."""
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainRepaso9()
    window.show()
    sys.exit(app.exec())
