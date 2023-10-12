class HistogramPresenter:
    """Histogram presenter"""

    def __init__(self, view, model):
        self._view = view
        self._model = model

        #way 1
        #include the button click definition here
        #self.view.fib_btn.clicked.connect(self.submit_fib)

        #way 2 use callbacks
        self.view.connect_btn_submit(self.submit_fib_cal)

    @property
    def view(self):
        """Return the view for this presenter"""
        return self._view

    @property
    def model(self):
        """Return the model for this presenter"""
        return self._model

    def error_message(self, msg, **kwargs):
        """Pass error message to the view"""
        self.view.show_error_message(msg, **kwargs)

    def submit_fib(self):
        """Submit the parameters to the model"""

        # get values from view
        a = self.view.start.value()
        b = self.view.end.value()

        # send to model for processing
        sequence = self.model.do_calculate(a, b)
        #update the results
        self.view.update_result(sequence)


    def submit_fib_cal(self, a,b):
        """Submit the parameters to the model"""

        # send to model for processing
        sequence = self.model.do_calculate(a, b)
        #update the results
        return sequence 
