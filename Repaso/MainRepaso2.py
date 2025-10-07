import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot
from formulario import Ui_MainWindow   # archivo generado desde Qt Designer

class Repaso2(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conectar botón
        self.pushButton.clicked.connect(self.enviar_formulario)

    @Slot()
    def enviar_formulario(self):
        nombre = self.lineEdit.text()        # QLineEdit
        rol = self.comboBox.currentText()    # QComboBox
        acepta = self.checkBox.isChecked()   # QCheckBox

        if not nombre or not acepta:
            print("Faltan datos")
        else:
            print(f"Nombre: {nombre} | Rol: {rol} | Acepta: Sí")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Repaso2()
    ventana.show()
    sys.exit(app.exec())
