"""Presenter for the Fibonacci Calculations"""

class FiboStatsPresenter:
    """FiboStats presenter"""

    def __init__(self, view, model):
        self._view = view
        self._model = model

        #TODO connections missing



    @property
    def view(self):
        """Return the view for this presenter"""
        return self._view

    @property
    def model(self):
        """Return the model for this presenter"""
        return self._model

    #TODO functions missing