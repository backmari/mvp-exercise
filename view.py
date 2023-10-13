"""PyQt Widget for the fibonacci parameters"""
from qtpy.QtWidgets import (
    QWidget,
    QPushButton,
    QFormLayout,
    QLineEdit,
    QSpinBox,
    QLabel
)

from invalid_styles import INVALID_QSPINBOX

class FiboStatsView(QWidget):
    """FiboStats widget"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.field_errors = []
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
        
        #initial state
        #hide results
        self.set_result_visible(False)
        #deactivate the button
        self.fib_btn.setEnabled(False)
        
        #onclick events
        # check min<max
        self.start.valueChanged.connect(lambda: self.min_max_compare(self.start, self.end))
        self.end.valueChanged.connect(lambda: self.min_max_compare(self.start, self.end))

        #way 2 definitions here
        #self.fib_btn.clicked.connect(self.btn_submit)

    def update_result(self, data):
        # display the Fibonacci sequence statistics
        self.mean.setText(str(data["mean"]))
        self.stdev.setText(str(data["stdev"]))
        self.perc95.setText(str(data["perc95"]))
        self.set_result_visible(True)

    def set_result_visible(self, flag):
        # show/hide the statistics fields and labels
        
        self.result.setVisible(flag)

        self.mean_label.setVisible(flag)
        self.mean.setVisible(flag)

        self.stdev_label.setVisible(flag)
        self.stdev.setVisible(flag)

        self.perc95_label.setVisible(flag)
        self.perc95.setVisible(flag)

    def get_parameters(self):
        a = self.start.value()
        b = self.end.value()
        return a,b
    
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


    def min_max_compare(self, cmin, cmax):
        """Ensure Minimum and Maximum value pairs are:
        Minimum < Maximum """

        self.set_field_valid_state(cmin)
        self.set_field_valid_state(cmax)

        min_value = int(cmin.text())
        max_value = int(cmax.text())

        #check: min<max
        valid = min_value < max_value
        if not valid:
            self.set_field_invalid_state(cmin)
            self.set_field_invalid_state(cmax)


    def set_field_invalid_state(self, item):
        """include the item in the field_error list and disable the corresponding button"""
        if item not in self.field_errors:
            self.field_errors.append(item)
        self.fib_btn.setEnabled(False)
        item.lineEdit().setStyleSheet(INVALID_QSPINBOX)

    def set_field_valid_state(self, item):
        """remove the item from the field_error list and enable the corresponding button"""
        if item in self.field_errors:
            self.field_errors.remove(item)
        if len(self.field_errors) == 0:
            self.fib_btn.setEnabled(True)
        item.lineEdit().setStyleSheet("")