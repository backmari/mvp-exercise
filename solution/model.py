"""Model for the Fibonacci Calculations"""

from fibonacci import fibonacci
import statistics
import numpy as np 

class FiboStatsModel:
    """Fiobancci stats model"""

    def __init__(self):
        self.error_callback = None

    def connect_error_message(self, callback):
        """Set the callback function for error messages"""
        self.error_callback = callback

    def do_calculate(self, small_num, big_num):
        """Do calculation"""

        try:
            results = {}
            sequence = fibonacci(end=big_num,start=small_num)

            results["stdev"] = round(statistics.stdev(sequence),2)
            results["mean"] = round(statistics.mean(sequence),2)
            results["perc95"] = round(np.percentile(sequence,95),2)
            #typeerror
            #results["perc95"] = round(str(np.percentile(sequence,95)),2)
            return results        
        except (RuntimeError,TypeError, ValueError) as err:
            if self.error_callback:
                self.error_callback(str(err))
            return None

