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

    def hypothesis_test(self, symbols: List[Any]) -> List[Any]:
        raise NotImplementedError("No hypothesis testing method was defined.")


class MAPReceiver(Receiver):
    def hypothesis_test(self, symbol) -> List[str]:
        pass
