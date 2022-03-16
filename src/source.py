from typing import Dict, List
import numpy as np


class Source:
  def __init__(self, symbols: Dict[str, float]) -> None:
    self._rng = np.random.default_rng()
    self.alphabet = symbols

  def generate_messages(self, n: int = None) -> str:
    if n is None:
        raise AttributeError("No amount of messages to generate provided")

    return self._rng.choice(list(self.alphabet.keys()), n, p=list(self.alphabet.values()))


class UniformSource(Source):
    def __init__(self, symbols: List[str]) -> None:
        super().__init__({symbol:1 / len(symbols) for symbol in symbols})

