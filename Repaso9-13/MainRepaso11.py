# MainRepaso11.py
# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QMessageBox, QLabel
)
from Repaso11 import Ui_MainWindow  # Asegúrate de que el archivo generado por Qt Designer se llama así


class MainRepaso11(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # ======== Barra de estado personalizada ========
        # QLabel normal (desaparece cuando se muestra un mensaje temporal)
        self.lbl_info = QLabel("Listo")
        self.ui.statusbar.addWidget(self.lbl_info)

        # QLabel permanente (siempre visible en el extremo derecho)
        self.lbl_permanente = QLabel("Usuario: Admin")
        self.ui.statusbar.addPermanentWidget(self.lbl_permanente)

        # Mostrar un mensaje temporal durante 3 segundos
        self.ui.statusbar.showMessage("Bienvenido a la aplicación", 3000)
        # =================================================

        # Conexiones de acciones
        self.ui.actAbrir.triggered.connect(self.abrir_archivo)
        self.ui.actGuardar.triggered.connect(self.guardar_archivo)
        self.ui.actSalir.triggered.connect(self.salir_aplicacion)

    def abrir_archivo(self):
        """Abre un cuadro de diálogo para seleccionar un archivo."""
        archivo, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Todos los archivos (*)")
        if archivo:
            self.ui.statusbar.showMessage(f"Archivo abierto: {archivo}", 4000)
            QMessageBox.information(self, "Archivo abierto", f"Has abierto:\n{archivo}")
        else:
            self.ui.statusbar.showMessage("Apertura cancelada", 2000)

    def guardar_archivo(self):
        """Abre un cuadro de diálogo para guardar un archivo."""
        archivo, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Todos los archivos (*)")
        if archivo:
            self.ui.statusbar.showMessage(f"Archivo guardado como: {archivo}", 4000)
            QMessageBox.information(self, "Archivo guardado", f"Archivo guardado como:\n{archivo}")
        else:
            self.ui.statusbar.showMessage("Guardado cancelado", 2000)

    def salir_aplicacion(self):
        """Cierra la aplicación."""
        self.ui.statusbar.showMessage("Saliendo de la aplicación...", 2000)
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainRepaso11()
    window.show()
    sys.exit(app.exec())
