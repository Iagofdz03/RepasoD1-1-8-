# MainRepaso10.py
# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from Repaso10 import Ui_MainWindow  # Asegúrate de que el archivo .ui convertido se llama Repaso10.py

class MainRepaso10(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conexiones de las acciones
        self.ui.actAbrir.triggered.connect(self.abrir_archivo)
        self.ui.actGuardar.triggered.connect(self.guardar_archivo)
        self.ui.actSalir.triggered.connect(self.salir_aplicacion)

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

    def salir_aplicacion(self):
        """Cierra la aplicación."""
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainRepaso10()
    window.show()
    sys.exit(app.exec())
