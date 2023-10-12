"""PyQt QGroupBox for the fibonacci parameters"""
from qtpy.QtWidgets import (
    QWidget,
    QPushButton,
    QFormLayout,
    QLineEdit,
    QSpinBox,
    QLabel
)


class Histogram(QWidget):
    """Histogram widget"""

    def __init__(self, parent=None):
        super().__init__(parent)

        # button callbacks
        self.btn_submit_callback = None

        layout = QFormLayout()

        self.name = QLineEdit(f"Fibonacci Stats")
        layout.addRow("Name", self.name)

        self.start = QSpinBox()
        self.start.setRange(0, 1_000)
        layout.addRow("Start", self.start)

        self.end = QSpinBox()
        self.end.setRange(0, 1_000)
        layout.addRow("End", self.end)

        self.result = QLabel("Results")        
        layout.addWidget(self.result)

        self.mean = QLineEdit("")
        self.mean.setReadOnly(True)
        self.mean_label = QLabel("Mean")        
        layout.addRow(self.mean_label, self.mean)

        self.stdev = QLineEdit("")
        self.stdev.setReadOnly(True)
        self.stdev_label = QLabel("StDev")        
        layout.addRow(self.stdev_label, self.stdev)        

        self.perc95 = QLineEdit("")
        self.perc95.setReadOnly(True)
        self.perc95_label = QLabel("95th perc")        
        layout.addRow(self.perc95_label, self.perc95)    

        self.fib_btn = QPushButton("Calculate")
        layout.addWidget(self.fib_btn)

        self.setLayout(layout)
        self.set_result_visible(False)

        #onclick events
        #way 2 definitions here
        self.fib_btn.clicked.connect(self.btn_submit)

    def update_result(self, data):
        # display the Fibonacci sequence statistics
        self.mean.setText(str(data["mean"]))
        self.stdev.setText(str(data["stdev"]))
        self.perc95.setText(str(data["perc95"]))
        self.set_result_visible(True)

    def set_result_visible(self, flag):
        # show/hide the statistics fields and labels
        
        self.mean_label.setVisible(flag)
        self.mean.setVisible(flag)

        self.stdev_label.setVisible(flag)
        self.stdev.setVisible(flag)

        self.perc95_label.setVisible(flag)
        self.perc95.setVisible(flag)

    def btn_submit(self):
        #submit_fib
        # get values from view
        a = self.start.value()
        b = self.end.value()
        if self.btn_submit_callback:
            results = self.btn_submit_callback(a,b)
        self.update_result(results)

    def connect_btn_submit(self, callback):
        """callback for the apply submit button"""
        self.btn_submit_callback = callback

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


