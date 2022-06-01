# -----------------------------------------------------------
# Comparer of various implementations of Dynamic Time Warping (DTW) algorithm
# - entry point
#
# (C) 2022 Michal Lech, Gdynia, Poland
# Released under GNU General Public License v3.0 (GPL-3.0)
# email: mlech.ksm@gmail.com
# -----------------------------------------------------------

from typing import List, Union
from multiprocessing import Process
import numpy as np
from numpy.typing import NDArray
from dtwcontext import DTWContext
from dtwstrategy import DTWStrategy
from strategies.origdtw import DTWOrigStrategy
from strategies.dtwpython import DTWPythonStrategy
from mydecorators import timer4main


def run_strategy(*args: Union[DTWStrategy, NDArray, NDArray]):
    dtw_strategy, function_1, function_2 = args[0], args[1], args[2]
    dtw_context = DTWContext(dtw_strategy)
    dtw_context.do_algorithm(function_1, function_2)


def run_strategies(dtw_strategies: List, function_1: NDArray, function_2: NDArray) -> None:
    if __name__ == '__main__':
        processes = []
        for dtw_strategy in dtw_strategies:
            p = Process(target=run_strategy, args=(dtw_strategy, function_1, function_2))
            processes.append(p)

        for p in processes:
            p.start()

        for p in processes:
            p.join()


@timer4main
def main():
    sample_size = 1000
    # use sin and its deviation to test DTW
    l_space = np.linspace(-np.pi, np.pi, sample_size)
    function_1 = np.sin(l_space)
    function_2 = (np.random.uniform(0.1, 4)) * np.sin(l_space + np.random.rand(1) * np.pi)

    dtw_strategies = [DTWOrigStrategy(), DTWPythonStrategy()]
    run_strategies(dtw_strategies, function_1, function_2)


main()
