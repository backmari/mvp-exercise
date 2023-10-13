"""Model for the Fibonacci Calculations"""

from fibonacci import fibonacci
import statistics
import numpy as np 

class FiboStatsModel:
    """Fiobancci stats model"""

    def __init__(self):
        self.error_callback = None

    def do_calculate(self, small_num, big_num):
        """Do calculation"""

        results = {}
        try:
            sequence = fibonacci(big_num, small_num)
        except ValueError as err:
            if self.error_callback:
                self.error_callback(str(err))

        #results["sequence"] = sequence
        results["stdev"] = round(statistics.stdev(sequence),2)
        results["mean"] = round(statistics.mean(sequence),2)
        results["perc95"] = round(np.percentile(sequence,95),2)
        return results        