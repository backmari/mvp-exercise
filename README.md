# Model-View-Presenter exercise

This is an exercise to get you thinking about code organization according to the Model-View-Presenter architectural pattern.

The directory `./exercise/` contains the source code for a small Qt-based app for calculating statistics for a Fibonacci sequence. The goal of the exercise is to refactor the code in `./exercise/spaghetti.py` to separate it into the three classes `FiboStatsModel`, `FiboStatsView` and `FiboStatsPresenter`.

## Get dependencies

### Option 1: Create new conda environment

    conda env create -f environment.yml

### Option 2: Get dependencies using pip

Assuming python3 and pip in the environment:

    pip install numpy py-fibonacci qtpy pyqt5

## Run

    python exercise/main_all.py
