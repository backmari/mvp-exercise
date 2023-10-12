class HistogramPresenter:
    """Histogram presenter"""

    def __init__(self, view, model):
        self._view = view
        self._model = model

        self.view.connect_histogram_submit(self.handle_button)
        self.view.histogram_btn.clicked.connect(self.submit_histogram_to_make_slice)

    @property
    def view(self):
        """Return the view for this presenter"""
        return self._view

    @property
    def model(self):
        """Return the model for this presenter"""
        return self._model

    def handle_button(self, params_dict):
        """Validate symmetry histogram parameter"""
        symmetry = params_dict["SymmetryOperations"]
        return self.model.symmetry_operations(symmetry)

    def error_message(self, msg, **kwargs):
        """Pass error message to the view"""
        self.view.show_error_message(msg, **kwargs)

    def submit_histogram_to_make_slice(self):
        """Submit the histogram to the model"""

        # get values from view, e.g. self.view.symmetry.value
        # and pass to do_make_slice

        # send to model for processing
        self.model.do_make_slice()
