import unittest as ut

from src.channel import PoissonChannel
from src.receiver import MAPReceiver, Receiver
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


class TestMAPReceiver(ut.TestCase):
    def setUp(self) -> None:
        self.no_of_messages = 10
        self.source = UniformSource(["0", "1"])
        self.source.generate_messages(self.no_of_messages)
        self.channel = PoissonChannel(input_source=self.source, lambdas=[1.5, 15])

    def test_should_make_a_prediction_for_all_messages(self) -> None:
        r = MAPReceiver(source=self.source, channel=self.channel)
        self.assertEqual(len(r.output), self.no_of_messages)

    def test_all_predictions_should_belong_to_source_alphabet(self) -> None:
        r = MAPReceiver(source=self.source, channel=self.channel)
        self.assertEqual(
            all(isinstance(x, type(self.source.alphabet[0])) for x in r.output), True
        )
