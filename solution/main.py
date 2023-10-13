import sys
from qtpy.QtWidgets import QApplication, QMainWindow
from model import FiboStatsModel
from presenter import FiboStatsPresenter
from view import FiboStatsView


class MVPExercise(QMainWindow):
    """Main window"""

    __instance = None

    def __new__(cls):
        if MVPExercise.__instance is None:
            MVPExercise.__instance = QMainWindow.__new__(cls)
        return MVPExercise.__instance

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Statistics")
        self.fibostats_view = FiboStatsView(self)
        self.figostats_model = FiboStatsModel()
        self.fibostats_presenter = FiboStatsPresenter(self.fibostats_view, self.figostats_model)
        self.setCentralWidget(self.fibostats_view)


if __name__ == "__main__":
    # start window
    app = QApplication(sys.argv)
    window = MVPExercise()
    window.show()
    sys.exit(app.exec_())
