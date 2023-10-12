class HistogramPresenter:
    """Histogram presenter"""

    def __init__(self, view, model):
        self._view = view
        self._model = model

        self.view.histogram_btn.clicked.connect(self.submit_histogram_to_make_slice)

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

    def submit_histogram_to_make_slice(self):
        """Submit the histogram to the model"""

        # get values from view
        a = self.view.start.value()
        b = self.view.end.value()

        # send to model for processing
        sequence = self.model.do_calculate(a, b)

        self.view.update_result(sequence)
