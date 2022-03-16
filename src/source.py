from typing import Any, List

import numpy as np

from src.utils import alphabet_is_valid


class Source:
    def __init__(self, symbols: List[str], probabilities: List[float]) -> None:
        if not alphabet_is_valid(symbols):
            raise AttributeError(
                "The alphabet list should not contain repeated symbols."
            )
        self.alphabet = symbols

        if len(probabilities) != len(symbols):
            raise AttributeError(
                "The alphabet list and the probabilities list do not match."
            )
        self.probabilities = probabilities
        self._symbols = {
            self.alphabet[i]: self.probabilities[i]
            for i in range(len(self.probabilities))
        }

        self._rng = np.random.default_rng()
        self._output = None

    def get_probability_for(self, symbol: Any) -> float:
        return self._symbols[symbol]

    @property
    def output(self) -> List[str]:
        return self._output if self._output is not None else []

    def generate_messages(self, n: int = None) -> None:
        if n is None:
            raise AttributeError("No amount of messages to generate provided")

        self._output = self._rng.choice(self.alphabet, n, p=self.probabilities)


class UniformSource(Source):
    def __init__(self, symbols: List[str]) -> None:
        super().__init__(
            symbols=symbols,
            probabilities=[1 / len(symbols) for _ in symbols],
        )
