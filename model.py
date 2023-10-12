"""Model for the Histogram tab"""

class HistogramModel:
    """Histogram model"""

    def __init__(self):
        pass

    def symmetry_operations(self, symmetry):
        """Validate the symmetry value with mantid"""
        # if len(symmetry) != 0:
        #     try:
        #         if SpaceGroupFactory.isSubscribedSymbol(symmetry) or PointGroupFactory.isSubscribed(symmetry):
        #             # then it's valid
        #             pass
        #         else:
        #             # check with SymmetryOperationFactory.createSymOps
        #             try:
        #                 SymmetryOperationFactory.createSymOps(symmetry)
        #             except RuntimeError as err:
        #                 err_msg = f"Invalid Symmetry Operations value. {err} \n"
        #                 if self.error_callback:
        #                     self.error_callback(err_msg, accumulate=True)
        #                 return False
        #     except RuntimeError as err:
        #         err_msg = f"Invalid Symmetry Operations value. {err} \n"
        #         if self.error_callback:
        #             self.error_callback(err_msg, accumulate=True)
        #         return False
        return True

    def do_make_slice(self):
        """Method to take filename and workspace type and load with correct algorithm"""
        pass

        # alg = AlgorithmManager.create("MakeSlice")
        # alg_obs = MakeSliceObserver(parent=self, ws_name=config.get("OutputWorkspace"))
        # self.algorithms_observers.add(alg_obs)
        # alg_obs.observeFinish(alg)
        # alg_obs.observeError(alg)
        # alg.initialize()
        # alg.setLogging(False)
        # try:
        #     alg.setProperty("InputWorkspace", config.get("InputWorkspace"))
        # except (RuntimeError, ValueError) as err:
        #     if self.error_callback:
        #         self.error_callback(str(err))
