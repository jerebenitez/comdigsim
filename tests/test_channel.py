import unittest as ut

import numpy as np

from src.channel import Channel, PoissonChannel
from src.source import UniformSource


class TestChannel(ut.TestCase):
    def setUp(self) -> None:
        self.source = UniformSource(["0", "1"])

    def test_no_distribution_set(self) -> None:
        c = Channel(input_source=self.source)
        with self.assertRaises(NotImplementedError):
            c.distribution()

    def test_no_output_function_set(self) -> None:
        c = Channel(input_source=self.source)
        with self.assertRaises(NotImplementedError):
            _ = c.output


class TestPoissonChannel(ut.TestCase):
    def setUp(self) -> None:
        self.source = UniformSource(["0", "1"])
        self.lambdas = [1.5, 15]

    def test_no_output_without_messages_from_source(self) -> None:
        c = PoissonChannel(input_source=self.source, lambdas=self.lambdas)
        self.assertEqual(c.output, [])

    def test_all_messages_are_transmitted(self) -> None:
        c = PoissonChannel(input_source=self.source, lambdas=self.lambdas)
        self.source.generate_messages(10)
        self.assertEqual(len(c.output), 10)

    def test_fail_on_incorrect_lambdas(self) -> None:
        with self.assertRaises(AttributeError):
            _ = PoissonChannel(input_source=self.source, lambdas=[])

    def test_channel_accepts_integer_sources(self) -> None:
        s = UniformSource([1, 2])
        c = PoissonChannel(input_source=s, lambdas=self.lambdas)
        s.generate_messages(10)
        # np.int64 is used because, internally, the source calls numpy to select its output
        self.assertEqual(all(isinstance(x, np.int64) for x in c.input), True)
