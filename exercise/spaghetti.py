"""PyQt Widget for the fibonacci parameters"""
from qtpy.QtWidgets import (
    QWidget,
    QPushButton,
    QFormLayout,
    QLineEdit,
    QSpinBox,
    QLabel,
    QErrorMessage
)

from fibonacci import fibonacci
import statistics
import numpy as np 

INVALID_QSPINBOX = """
QLineEdit {
color: red;
background-color: pink;

}
"""
class FiboStats(QWidget):
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

        self.fib_btn.clicked.connect(self.btn_submit)


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
        start = self.start.value()
        end = self.end.value()
        return start,end
    
    def btn_submit(self):
        #submit_fib
        # get values
        small_num = self.start.value()
        big_num = self.end.value()

        #run fibonacci
        try:        
            sequence = fibonacci(big_num, small_num)

            # to cause TypeError
            #data_perc95 = round(str(np.percentile(sequence,95)),2)

            #gather data statistics
            data_stdev = round(statistics.stdev(sequence),2)
            data_mean = round(statistics.mean(sequence),2)
            data_perc95 = round(np.percentile(sequence,95),2)

            # display the Fibonacci sequence statistics
            self.stdev.setText(str(data_stdev))
            self.mean.setText(str(data_mean))
            self.perc95.setText(str(data_perc95))
            self.set_result_visible(True)
        
        except (RuntimeError,TypeError, ValueError) as err:
            self.show_error_message(str(err))

    def min_max_compare(self, cmin, cmax):
        """Ensure cmin and cmax value pairs are:
        cmin < cmax """

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
        """include the item in the field_error list, update background color 
        and disable the corresponding button"""
        
        if item not in self.field_errors:
            self.field_errors.append(item)
        self.fib_btn.setEnabled(False)
        item.lineEdit().setStyleSheet(INVALID_QSPINBOX)

    def set_field_valid_state(self, item):
        """remove the item from the field_error list, update background color 
        and enable the corresponding button"""

        if item in self.field_errors:
            self.field_errors.remove(item)
        if len(self.field_errors) == 0:
            self.fib_btn.setEnabled(True)
        item.lineEdit().setStyleSheet("")


    def show_error_message(self, msg):
        """Will show a error dialog with the given message"""
        error = QErrorMessage(self)
        error.showMessage(msg)
        error.exec_()                