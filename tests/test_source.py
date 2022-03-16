import unittest

from src.source import Source, UniformSource


class TestSource(unittest.TestCase):
    def setUp(self) -> None:
        self.alphabet = ["0", "1"]

    def test_creation_of_valid_source(self) -> None:
        s = Source(self.alphabet, [0.5, 0.5])
        self.assertEqual(s.alphabet, self.alphabet)

    def test_normalization_in_probabilities(self) -> None:
        with self.assertRaises(AttributeError):
            Source(self.alphabet, [1, 1])

    def test_different_sizes_of_lists_should_fail(self) -> None:
        with self.assertRaises(AttributeError):
            Source(self.alphabet, [])

    def test_repeated_symbols_should_not_be_allowed(self) -> None:
        with self.assertRaises(AttributeError):
            Source(["0", "0", "1", "2"], [0.25, 0.25, 0.25, 0.25])

    def test_probabilities_should_remain_the_same(self) -> None:
        s = Source(self.alphabet, [0.3, 0.7])
        self.assertEqual(s.get_probability_for("0"), 0.3)
        self.assertEqual(s.get_probability_for("1"), 0.7)

    def test_output_should_be_empty_if_not_generated(self) -> None:
        s = Source(self.alphabet, [0.3, 0.7])
        self.assertEqual(s.output, [])

    def test_messages_should_be_generated_correctly(self) -> None:
        messages = 10
        s = Source(self.alphabet, [0.5, 0.5])
        s.generate_messages(messages)
        self.assertEqual(len(s.output), messages)


class TestUniformSource(unittest.TestCase):
    def test_probabilities_are_assigned_correctly(self) -> None:
        s = UniformSource(["0", "1", "2"])
        self.assertEqual(s.get_probability_for("0"), 1 / 3)
