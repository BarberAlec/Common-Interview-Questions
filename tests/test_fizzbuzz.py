"""Run tests on FizzBuzz functions"""

from unittest import TestCase
from fizz_buzz import FizzBuzz
from random import seed
from random import randint


class TestMinInt(TestCase):
    """
    Run all methods prefixed with 'test'
    """
    def setUp(self) -> None:
        """
        This is called _before_ each test
        """
        seed(42)
        self.test_cases = {
            1: 1,
            2: 2,
            3: "Fizz",
            4: 4,
            5: "Buzz",
            0: 0,
            -1: -1,
            6: "Fizz",
            7: 7,
            8: 8,
            9: "Fizz",
            10: "Buzz",
            11: 11,
            12: "Fizz",
            13: 13,
            14: 14,
            15: "FizzBuzz",
            16: 16,
            3 * randint(1, 3): "Fizz",
            5 * randint(4, 5): "Buzz",
            15 * randint(1, 100): "FizzBuzz"
        }

    def test_fizzbuzz_build(self):
        for test_case, answer in self.test_cases.items():
            self.assertEqual(answer, FizzBuzz.fizzbuzz_build(test_case))

    def test_fizzbuzz_simple(self):
        for test_case, answer in self.test_cases.items():
            self.assertEqual(answer, FizzBuzz.fizzbuzz_simple(test_case))

    def test_fizzbuzz_complete(self):
        for test_case, answer in self.test_cases.items():
            self.assertEqual(answer, FizzBuzz.fizzbuzz_complete(test_case))

