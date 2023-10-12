"""Model for the Histogram tab"""

from fibonacci import fibonacci


class HistogramModel:
    """Histogram model"""

    def __init__(self):
        pass

    def do_calculate(self, a, b):
        """Do calculation"""
        # return fibonacci(int(a), int(b))
        sequence = fibonacci(b, a)
        return sequence
