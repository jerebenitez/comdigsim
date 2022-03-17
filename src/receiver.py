from typing import Any, Dict, List

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
        predicted_probability = 0
        predicted_symbol = None
        predicted_symbols = []
        for _input in inputs:
            input_probability = self.channel.get_probability_for(_input)
            for symbol in self.source.alphabet:
                probability = (
                    self.source.get_probability_for(symbol) * input_probability
                )
                if probability > predicted_probability:
                    predicted_probability = probability
                    predicted_symbol = symbol
            predicted_symbols.append(predicted_symbol)
            predicted_probability = 0
            predicted_symbol = None

        return predicted_symbols
