"""PyQt QGroupBox for the histogram parameters"""
from qtpy.QtCore import Signal
from qtpy.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QGroupBox,
    QFormLayout,
    QLineEdit,
    QDoubleSpinBox,
)
from invalid_styles import INVALID_QLINEEDIT


class Histogram(QWidget):
    """Histogram widget"""

    error_message_signal = Signal(str)
    makeslice_finish_signal = Signal(str, int)
    msg_queue = []

    plot_num = 1
    name_base = "Histogram"

    def __init__(self, parent=None):
        super().__init__(parent)

        # check the state of the required fields
        # based on the fields states
        self.field_errors = []
        self.plot_display_name_callback = None

        # self.histogram_parameters = HistogramParameter(self)

        self.histogram_parameters = QGroupBox()

        self.histogram_parameters.setTitle("Histogram parameters")

        hlayout = QVBoxLayout()
        self.projections = QWidget()
        playout = QFormLayout()

        self.name = QLineEdit(f"{self.name_base} {self.plot_num}")
        plot_name_layout = QHBoxLayout()
        plot_name_layout.addWidget(self.name)
        playout.addRow("Name", plot_name_layout)

        self.projections.setLayout(playout)
        hlayout.addWidget(self.projections)

        symmetry = QWidget()

        slayout = QFormLayout()
        self.symmetry_operations = QLineEdit()
        slayout.addRow("Symmetry operations", self.symmetry_operations)

        # smoothing can't exceed 1_000 and can't be negative
        self.smoothing = QDoubleSpinBox()
        self.smoothing.setRange(0, 1_000)
        slayout.addRow("Smoothing", self.smoothing)
        symmetry.setLayout(slayout)

        hlayout.addWidget(symmetry)

        hlayout.addStretch()

        self.histogram_btn = QPushButton("Histogram")
        hlayout.addWidget(self.histogram_btn)

        self.histogram_parameters.setLayout(hlayout)

        # submit button
        self.histogram_callback = None

        layout = QHBoxLayout()
        layout.addWidget(self.histogram_parameters)
        self.setLayout(layout)

        # self.error_message_signal.connect(self._show_error_message)
        # self.makeslice_finish_signal.connect(self._make_slice_finish)

        # self.buttons.connect_error_msg(self.show_error_message)

#     def set_field_invalid_state(self, item):
#         """if parent exists then call the corresponding function and update the color"""
#         if self.parent():
#             self.parent().set_field_invalid_state(item)
#         item.setStyleSheet(INVALID_QLINEEDIT)

#     def set_field_valid_state(self, item):
#         """remove the item from the field_error list and its invalid style, if it was previously invalid
#         and enable the corresponding button"""
#         if self.parent():
#             self.parent().set_field_valid_state(item)
#         item.setStyleSheet("")

#     def validate_symmentry_once(self):
#         """validate symmetry once the current invalid text is updated. Note: the actual validation happens in models"""
#         self.set_field_valid_state(self.symmetry_operations)
#         self.symmetry_operations.disconnect()

#     @property
#     def is_valid(self) -> bool:
#         """Checks if the histogram parameters are valid

#         Returns
#         -------
#             bool -- True if valid, False otherwise
#         """

#         # check if symmetry is valid
#         # NOTE: the symmetry checking is done in histogram_callback and border colors/state are updapted, and the
#         #       actual checking is done in histogram.model.
#         #       the current design requires packing the data as a dictionary,
#         #       so we pack it here.
#         parameters = {}
#         parameters["SymmetryOperations"] = self.symmetry_operations.text()
#         self.set_field_valid_state(self.symmetry_operations)
#         sym_valid_state = self.histogram_callback(parameters) if self.histogram_callback else False
#         if not sym_valid_state:
#             self.set_field_invalid_state(self.symmetry_operations)
#             self.symmetry_operations.textEdited.connect(self.validate_symmentry_once)

#         return sym_valid_state

    def connect_histogram_submit(self, callback):
        """callback for the histogram submit button"""
        self.histogram_callback = callback