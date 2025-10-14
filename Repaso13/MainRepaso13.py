from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
from Repaso13 import Ui_MainWindow  # tu archivo generado del .ui


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # --- Layout central (para que el QLabel sea responsive) ---
        layout = QVBoxLayout()
        layout.addWidget(self.ui.lblTitulo)
        self.ui.centralwidget.setLayout(layout)

        # --- Layout del Dock ---
        dock_layout = QVBoxLayout()
        dock_layout.addWidget(self.ui.listWidget)
        self.ui.dockWidgetContents.setLayout(dock_layout)

        # --- Conexiones ---
        self.ui.actionAbrir.triggered.connect(self.abrir_archivo)
        self.ui.actionSalir.triggered.connect(self.close)

        self.ui.actPlay.triggered.connect(lambda: self.cambiar_estado("▶ Reproduciendo"))
        self.ui.actPause.triggered.connect(lambda: self.cambiar_estado("⏸ Pausado"))
        self.ui.actStop.triggered.connect(lambda: self.cambiar_estado("⏹ Detenido"))

        self.ui.listWidget.itemDoubleClicked.connect(self.cambiar_titulo)

        # --- Mensaje inicial ---
        self.ui.statusbar.showMessage("Listo para usar")

    def abrir_archivo(self):
        archivo, _ = QFileDialog.getOpenFileName(
            self, "Abrir archivo", "", "Archivos de audio (*.mp3 *.wav *.ogg)"
        )
        if archivo:
            self.ui.lblTitulo.setText(f"Abierto: {archivo.split('/')[-1]}")
            self.ui.statusbar.showMessage(f"Archivo abierto: {archivo}")

    def cambiar_estado(self, estado):
        self.ui.lblTitulo.setText(estado)
        self.ui.statusbar.showMessage(estado)

    def cambiar_titulo(self, item):
        self.ui.lblTitulo.setText(item.text())
        self.ui.statusbar.showMessage(f"Reproduciendo: {item.text()}")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
