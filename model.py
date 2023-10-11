"""Model for the Histogram tab"""
import time
import os.path
from typing import Tuple
import numpy as np

# pylint: disable=no-name-in-module
from mantid.api import (
    AlgorithmManager,
    AlgorithmObserver,
    AnalysisDataServiceObserver,
    Progress,
)
from mantid.simpleapi import mtd, DeleteWorkspace, RenameWorkspace, SaveMD, AddSampleLog
from mantid.kernel import Logger
from mantid.geometry import (
    SymmetryOperationFactory,
    SpaceGroupFactory,
    PointGroupFactory,
)


class HistogramModel:
    """Histogram model"""

    def __init__(self):
        pass

    def symmetry_operations(self, symmetry):
        """Validate the symmetry value with mantid"""
        if len(symmetry) != 0:
            try:
                if SpaceGroupFactory.isSubscribedSymbol(symmetry) or PointGroupFactory.isSubscribed(symmetry):
                    # then it's valid
                    pass
                else:
                    # check with SymmetryOperationFactory.createSymOps
                    try:
                        SymmetryOperationFactory.createSymOps(symmetry)
                    except RuntimeError as err:
                        err_msg = f"Invalid Symmetry Operations value. {err} \n"
                        if self.error_callback:
                            self.error_callback(err_msg, accumulate=True)
                        return False
            except RuntimeError as err:
                err_msg = f"Invalid Symmetry Operations value. {err} \n"
                if self.error_callback:
                    self.error_callback(err_msg, accumulate=True)
                return False
        return True

    def do_make_slice(self, config: dict):
        """Method to take filename and workspace type and load with correct algorithm"""

        # remove the OutputWorkspace first if it exists
        if config.get("OutputWorkspace") and mtd.doesExist(config["OutputWorkspace"]):
            self.delete(config["OutputWorkspace"])

        # alg = AlgorithmManager.create("MakeSlice")
        # alg_obs = MakeSliceObserver(parent=self, ws_name=config.get("OutputWorkspace"))
        # self.algorithms_observers.add(alg_obs)
        # alg_obs.observeFinish(alg)
        # alg_obs.observeError(alg)
        # alg.initialize()
        # alg.setLogging(False)
        # try:
        #     alg.setProperty("InputWorkspace", config.get("InputWorkspace"))
        #     alg.setProperty("BackgroundWorkspace", config.get("BackgroundWorkspace", None))
        #     alg.setProperty(
        #         "NormalizationWorkspace",
        #         config.get("NormalizationWorkspace", None),
        #     )
        #     alg.setProperty("QDimension0", config.get("QDimension0"))
        #     alg.setProperty("QDimension1", config.get("QDimension1"))
        #     alg.setProperty("QDimension2", config.get("QDimension2"))
        #     alg.setProperty("Dimension0Name", config.get("Dimension0Name"))
        #     alg.setProperty("Dimension0Binning", config.get("Dimension0Binning", ""))
        #     alg.setProperty("Dimension1Name", config.get("Dimension1Name"))
        #     alg.setProperty("Dimension1Binning", config.get("Dimension1Binning", ""))
        #     alg.setProperty("Dimension2Name", config.get("Dimension2Name"))
        #     alg.setProperty("Dimension2Binning", config.get("Dimension2Binning", ""))
        #     alg.setProperty("Dimension3Name", config.get("Dimension3Name"))
        #     alg.setProperty("Dimension3Binning", config.get("Dimension3Binning", ""))
        #     alg.setProperty("SymmetryOperations", config.get("SymmetryOperations", ""))
        #     alg.setProperty("Smoothing", config.get("Smoothing", ""))
        #     alg.setProperty("OutputWorkspace", config.get("OutputWorkspace"))
        #     alg.executeAsync()
        # except (RuntimeError, ValueError) as err:
        #     if self.error_callback:
        #         self.error_callback(str(err))
