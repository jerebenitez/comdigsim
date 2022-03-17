from typing import Dict
import numpy as np


class PoissonDetector:
    def __init__(self, symbols: Dict[str, float]) -> None:
        self._rng = np.random.default_rng()
        self.symbols = symbols

    def sample(self, symbol: str, samples: int):
        return self._rng.poisson(self.symbols.get(symbol), samples)

