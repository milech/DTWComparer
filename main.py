# -----------------------------------------------------------
# Comparer of various implementations of Dynamic Time Warping (DTW) algorithm
# - entry point
#
# (C) 2022 Michal Lech, Gdynia, Poland
# Released under GNU General Public License v3.0 (GPL-3.0)
# email: mlech.ksm@gmail.com
# -----------------------------------------------------------

from typing import List
import numpy as np
from numpy.typing import NDArray
from dtwcontext import DTWContext
from strategies.origdtw import DTWOrigStrategy
from strategies.dtwpython import DTWPythonStrategy
from mydecorators import timer


@timer
def run_strategies(dtw_strategies: List, function_1: NDArray, function_2: NDArray) -> None:
    for dtw_strategy in dtw_strategies:     # TODO: implement as multi processes
        dtw_context = DTWContext(dtw_strategy)
        dtw_context.do_algorithm(function_1, function_2)


def main() -> None:
    sample_size = 200
    # use sin and its deviation to test DTW
    l_space = np.linspace(-np.pi, np.pi, sample_size)
    function_1 = np.sin(l_space)
    function_2 = np.random.rand() * np.sin(l_space + np.random.rand(1)*np.pi)

    dtw_strategies = [DTWOrigStrategy(), DTWPythonStrategy()]
    run_strategies(dtw_strategies, function_1, function_2)


main()
