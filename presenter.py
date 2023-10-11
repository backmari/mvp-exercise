class HistogramPresenter:
    """Histogram presenter"""

    def __init__(self, view, model):
        self._view = view
        self._model = model

        # self.view.connect_histogram_submit(self.handle_button)
        # self.view.histogram_btn.clicked.connect(self.submit_histogram_to_make_slice)


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

    def makeslice_finish(self, ws_name, ndims, error=False):
        """Handle the makeslice algorithm finishing"""

        # re-enable histogram UI elements
        self.view.disable_while_running(False)

        # plot the newly generated histogram
        if not error:
            self.view.make_slice_finish(ws_name, ndims)

    def submit_histogram_to_make_slice(self):
        """Submit the histogram to the model"""
        # only submit if the view is valid
        if self.ready_for_histogram():
            # disable Histogram button while running
            self.view.disable_while_running(True)

            # gather the parameters from the view for MakeSlice
            config = self.build_config_for_make_slice()

            # send to model for processing
            self.model.do_make_slice(config)

            # update the plot name in the histogram parameters view
            self.view.histogram_parameters.update_plot_num()

    def ready_for_histogram(self):
        """Check if the view is ready to submit a histogram"""
        # messages from models are passed to views
        if self.view.gather_workspace_data() is None or not self.view.histogram_parameters.is_valid:
            return False
        return True
