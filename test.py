import sys
from PySide6 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("titulek okna")
window.setGeometry(100, 100, 400, 300)

window.show(app.exec())
sys.exit(app.exec())

