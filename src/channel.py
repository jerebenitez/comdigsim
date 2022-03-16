from typing import List, Dict, Callable

from source import Source

class Channel:
    def __init__(self, input: Source=None) -> None:
        self._input = input

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
    def output(self) -> List[float]:
        raise NotImplementedError("An output function needs to be implemented for this channel.")

    def mapper(self) -> Callable:
        raise NotImplementedError("A mapper function needs to be implemented for this channel.")


class PoissonChannel(Channel):
    def __init__(self, dist: Dict[str, float]) -> None:
        self._params = dist
        super().__init__()

    @property
    def params(self) -> Dict[str, float]:
        return self._params

    def mapper(self) -> Callable:
        return np.random.poisson

    @property
    def output(self) -> List[float]:
        return [self.mapper(self._params[x]) for x in self.input]
