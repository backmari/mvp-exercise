import sys
from qtpy.QtWidgets import QApplication, QMainWindow
from model import HistogramModel
from presenter import HistogramPresenter
from view import Histogram


class MVPExercise(QMainWindow):
    """Main window"""

    __instance = None

    def __new__(cls):
        if MVPExercise.__instance is None:
            MVPExercise.__instance = QMainWindow.__new__(cls)
        return MVPExercise.__instance

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"MVP exercise")
        self.histogram_widget = Histogram(self)
        self.histogram_model = HistogramModel()
        self.histogram_presenter = HistogramPresenter(self.histogram_widget, self.histogram_model)
        self.setCentralWidget(self.histogram_widget)


if __name__ == "__main__":
    # start widget
    app = QApplication(sys.argv)
    window = MVPExercise()
    window.show()
    sys.exit(app.exec_())
