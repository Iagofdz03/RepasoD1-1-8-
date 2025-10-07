import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
from Arrancado import Ui_MainWindow  # Si quieres usar tu UI de Qt Designer

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana con etiqueta centrada")
        self.setGeometry(100, 100, 300, 200)

        etiqueta = QLabel("Arrancado")
        etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(etiqueta)
        self.setLayout(layout)

def main():
    print("Arrancado")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
