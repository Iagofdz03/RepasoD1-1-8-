from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QListWidget, QVBoxLayout
from PySide6.QtCore import Qt
from Repaso12 import Ui_MainWindow  # tu archivo generado del .ui

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # --- Barra de estado ---
        self.ui.statusbar.showMessage("Aplicación iniciada", 3000)
        self.status_label = QLabel("Versión 1.0")
        self.ui.statusbar.addPermanentWidget(self.status_label)

        # --- Conectar acciones ---
        self.ui.actSalir.triggered.connect(self.close)
        self.ui.actionMostrar.triggered.connect(lambda: self.ui.dockPlaylist.show())
        self.ui.actionOcultar.triggered.connect(lambda: self.ui.dockPlaylist.hide())

        # --- Arreglar layout del dock ---
        layout = QVBoxLayout()
        layout.addWidget(self.ui.lstPlaylist)
        self.ui.dockWidgetContents.setLayout(layout)  # ahora QListWidget se ve

        # Mostrar dock al inicio
        self.ui.dockPlaylist.show()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
