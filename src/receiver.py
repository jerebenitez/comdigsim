from functools import reduce
from typing import Any, List

from src.channel import Channel
from src.source import Source


class Receiver:
    def __init__(self, source: Source, channel: Channel) -> None:
        self.source = source
        self.channel = channel

    @property
    def output(self) -> List[Any]:
        return self.hypothesis_test(self.channel.output)

    def hypothesis_test(self, inputs: List[Any]) -> List[Any]:
        raise NotImplementedError("No hypothesis testing method was defined.")


class MAPReceiver(Receiver):
    def hypothesis_test(self, inputs: List[Any]) -> List[Any]:
        predicted_symbols = []
        for _input in inputs:
            input_probability = self.channel.get_probability_for(_input)
            predicted_symbols.append(
                reduce(
                    lambda x, y: y[0] if x[1] < y[1] else x[0],
                    [
                        (sym, self.source.get_probability_for(sym) * input_probability)
                        for sym in self.source.alphabet
                    ],
                )
            )

        return predicted_symbols
