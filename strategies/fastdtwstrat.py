from typing import List, Union, Any
from numpy.typing import NDArray
from fastdtw import fastdtw
from dtwstrategy import DTWStrategy
from mydecorators import timer
from mydecorators import print2console


class FastDTWStrategy(DTWStrategy):
    @print2console
    @timer
    def do_algorithm(self, function_1: NDArray, function_2: NDArray) -> List[Union[NDArray, Any]]:
        total_cost, _ = fastdtw(function_1, function_2)
        return [None, None, total_cost]
