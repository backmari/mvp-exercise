import sys
from qtpy.QtWidgets import QApplication, QMainWindow
from mainwindow import MainWindow

# from model import HistogramModel
# from presenter import HistogramPresenter
# from view import HistogramParameter


class Shiver(QMainWindow):
    """Main Shiver window"""

    __instance = None

    def __new__(cls):
        if Shiver.__instance is None:
            Shiver.__instance = QMainWindow.__new__(cls)  # pylint: disable=no-value-for-parameter
        return Shiver.__instance

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"SHIVER")
        self.main_window = MainWindow(self)
        self.setCentralWidget(self.main_window)


if __name__ == "__main__":
    # start widget
    app = QApplication(sys.argv)
    window = Shiver()
    window.show()
    sys.exit(app.exec_())
