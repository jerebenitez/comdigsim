from typing import Any, Callable, List, Union

import numpy as np
from numpy import ndarray
from scipy.stats.distributions import poisson

from source import Source


class Channel:
    def __init__(self, input_source: Source = None) -> None:
        self._input = input_source

    @property
    def input(self) -> List[Any]:
        return self._input.output

    @input.setter
    def input(self, new_input: Source) -> None:
        self.input = new_input

    @input.deleter
    def input(self) -> None:
        self._input = None

    def get_probability_for(self, signal: Any, symbol: Any) -> float:
        raise NotImplementedError(
            "A get_probability_for function needs to be implemented for this channel."
        )

    @property
    def output(self) -> List[Any]:
        raise NotImplementedError(
            "An output function needs to be implemented for this channel."
        )

    def distribution(self, *args, **kwargs) -> Union[ndarray, int, float, complex]:
        raise NotImplementedError(
            "A mapper function needs to be implemented for this channel."
        )


class PoissonChannel(Channel):
    def __init__(self, input_source: Source, lambdas: List[float]) -> None:
        super().__init__(input_source)
        self._lambdas = None
        self.set_lambdas(lambdas)
        self._symbols = {input_source.alphabet[i]: v for i, v in enumerate(lambdas)}

    def set_lambdas(self, lambdas):
        if len(lambdas) != len(self._input.alphabet):
            raise AttributeError("The alphabet list and the lambda list do not match.")

        self._lambdas = lambdas

    @property
    def params(self) -> List[float]:
        return self._lambdas

    @params.setter
    def params(self, lambdas: List[float]) -> None:
        self.set_lambdas(lambdas)

    def distribution(self, *args, **kwargs) -> Union[ndarray, int, float, complex]:
        return np.random.poisson(*args, **kwargs)

    @property
    def output(self) -> list[Any]:
        return [self.distribution(self._symbols[symbol]) for symbol in self.input]

    def get_probability_for(self, signal: Any, symbol: Any) -> float:
        return poisson.pmf(signal, self._symbols[symbol])
