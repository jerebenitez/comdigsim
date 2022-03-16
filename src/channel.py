from typing import Any, Callable, Dict, List, Union

import numpy as np
from numpy import ndarray

from source import Source


class Channel:
    def __init__(self, input_source: Source = None) -> None:
        self._input = input_source

    @property
    def input(self) -> List[str]:
        return self._input.output

    @input.setter
    def input(self, new_input: Source) -> None:
        self.input = new_input

    @input.deleter
    def input(self) -> None:
        self._input = None

    @property
    def output(self) -> List[Any]:
        raise NotImplementedError(
            "An output function needs to be implemented for this channel."
        )

    def mapper(self) -> Callable:
        raise NotImplementedError(
            "A mapper function needs to be implemented for this channel."
        )


class PoissonChannel(Channel):
    def __init__(self, input_source: Source, lambdas: List[float]) -> None:
        if len(lambdas) != len(input_source.alphabet):
            raise AttributeError("The alphabet list and the lambda list do not match.")

        self._lambdas = lambdas
        self._symbols = {
            input_source.alphabet[i]: lambdas[i] for i in range(len(lambdas))
        }
        super().__init__(input_source)

    @property
    def params(self) -> List[float]:
        return self._lambdas

    def mapper(self, *args, **kwargs) -> Union[ndarray, int, float, complex]:
        return np.random.poisson(*args, **kwargs)

    @property
    def output(self) -> list[Any]:
        return [self.mapper(self._symbols[symbol]) for symbol in self.input]
