from functools import reduce
from typing import Any, List

from channel import Channel
from source import Source


class Receiver:
    def __init__(self, source: Source, channel: Channel) -> None:
        self.source = source
        self.channel = channel

    @property
    def output(self) -> List[Any]:
        return self.hypothesis_test(self.channel.output)

    def hypothesis_test(self, inputs: List[Any]) -> List[Any]:
        raise NotImplementedError("No hypothesis testing method was defined.")

    def real_error(self, source_output: List[Any]) -> float:
        difference = sum(1 if x != y else 0 for x, y in zip(self.output, source_output))
        return difference / len(source_output)


class MAPReceiver(Receiver):
    def hypothesis_test(self, inputs: List[Any]) -> List[Any]:
        predicted_symbols = []
        for _input in inputs:
            predicted_symbols.append(
                reduce(
                    lambda x, y: y[0] if x[1] < y[1] else x[0],
                    [
                        (
                            sym,
                            self.source.get_probability_for(sym)
                            * self.channel.get_probability_for(_input, sym),
                        )
                        for sym in self.source.alphabet
                    ],
                )
            )

        return predicted_symbols
