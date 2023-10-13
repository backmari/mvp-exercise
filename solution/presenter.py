"""Presenter for the Fibonacci Calculations"""

class FiboStatsPresenter:
    """FiboStats presenter"""

    def __init__(self, view, model):
        self._view = view
        self._model = model

        #error message from model to view
        self.model.connect_error_message(self.error_message)

        #way 1 presenter definition
        #include the button click definition here
        self.view.fib_btn.clicked.connect(self.submit_fib)

        #way 2 use callbacks
        #self.view.connect_btn_submit(self.submit_fib_cal)

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

    #way 1 presenter definition
    def submit_fib(self):
        """Submit the parameters to the model"""

        # get values from view
        a,b = self.view.get_parameters()

        # send to model for processing
        data = self.model.do_calculate(a, b)
        #update the results
        if data is not None: 
            self.view.update_result(data)


    # way 2 button callback 
    # def submit_fib_cal(self, a,b):
    #     """Submit the parameters to the model"""

    #     # send to model for processing
    #     sequence = self.model.do_calculate(a, b)
    #     #update the results
    #     return sequence 
