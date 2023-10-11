from qtpy.QtWidgets import QWidget, QTabWidget, QVBoxLayout

from model import HistogramModel
from presenter import HistogramPresenter
from view import Histogram

class MainWindow(QWidget):
    """Main shiver widget"""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.tabs = QTabWidget()
        histogram = Histogram(self)
        histogram_model = HistogramModel()
        self.histogram_presenter = HistogramPresenter(histogram, histogram_model)
        self.tabs.addTab(histogram, "Main")

        layout = QVBoxLayout()
        layout.addWidget(self.tabs)

        self.setLayout(layout)

        # register child widgets to make testing easier
        self.histogram = histogram
