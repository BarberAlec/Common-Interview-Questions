"""Run tests on MinInt functions"""

from unittest import TestCase
from min_int import MinInt


class TestMinInt(TestCase):
    """
    Run all methods prefixed with 'test'
    """
    def setUp(self) -> None:
        """
        This is called _before_ each test
        """
        max_int = 100000
        max_list = list(range(1, max_int + 1))
        self.test_cases = [
            [1, 2, 3],
            [1, 1, 2, 3, 4, 5, 8, 13, 21, 34],
            [-1, -3],
            [1, 2],
            [0],
            [],
            max_list
        ]
        self.answers = [4, 6, 1, 3, 1, 1, max_int + 1]

    def test_xor(self):
        for test_case, answer in zip(self.test_cases, self.answers):
            self.assertEqual(answer, MinInt.using_xor(test_case))

    def test_quick(self):
        for test_case, answer in zip(self.test_cases, self.answers):
            self.assertEqual(answer, MinInt.quick_search(test_case))

