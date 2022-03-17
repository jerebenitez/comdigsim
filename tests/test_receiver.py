import unittest as ut

from src.channel import PoissonChannel
from src.receiver import Receiver
from src.source import UniformSource


class TestReceiver(ut.TestCase):
    def setUp(self) -> None:
        self.source = UniformSource(["0", "1"])
        self.channel = PoissonChannel(input_source=self.source, lambdas=[1.5, 15])
        self.no_of_messages = 10

    def test_undefined_hypothesis_test(self):
        r = Receiver(source=self.source, channel=self.channel)
        with self.assertRaises(NotImplementedError):
            _ = r.output
