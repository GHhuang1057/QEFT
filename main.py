import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.qeft_start_window import Ui_MainWindow

class MainWindow(Ui_MainWindow):
    def __init__(self, window):
        super().__init__()
        self.setupUi(window)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = MainWindow(window)
    window.show()
    sys.exit(app.exec_())
