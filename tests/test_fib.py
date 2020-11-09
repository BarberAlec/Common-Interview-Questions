"""Run tests on fibonacci functions"""

from unittest import TestCase
from fib_questions import Fib


class TestFibonacci(TestCase):
    """
    Run all methods prefixed with 'test'
    """
    def setUp(self) -> None:
        """
        This is called _before_ each test
        """
        self.fib_terms = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    def tearDown(self) -> None:
        """
        This is called _after_ each test
        """
        pass

    def test_fib_term(self):
        for i, fib_term in enumerate(self.fib_terms):
            self.assertEqual(fib_term, Fib.fib_term(i))

    def test_fib_inv(self):
        for i, fib_term in enumerate(self.fib_terms):
            if fib_term == 1:
                self.assertAlmostEqual(i, Fib.fib_inv(fib_term), delta=1)
            else:
                self.assertEqual(i, Fib.fib_inv(fib_term))

    def test_fib_num(self):
        for i, fib_term in enumerate(self.fib_terms):
            self.assertEqual(fib_term, Fib.fib_num(i))

    def test_next_fib_num(self):
        self.assertTrue(len(self.fib_terms) > 3, msg="Need > 3 fib terms to test")
        prev_1 = self.fib_terms[0]
        prev_2 = self.fib_terms[1]
        for fib_term in self.fib_terms[2:]:
            self.assertEqual((prev_2, fib_term), Fib.next_fib_num(prev_1, prev_2))
            prev_1 = prev_2
            prev_2 = fib_term

    def test_closest_fib_num(self):
        for i, fib_term in enumerate(self.fib_terms[1:]):
            self.assertAlmostEqual(i, Fib.closest_fib_num(i), delta=fib_term - self.fib_terms[i])

    def test_fib_multi(self):
        for i, fib_term in enumerate(self.fib_terms):
            self.assertEqual(Fib.fib_term(i), Fib.fib_num(Fib.fib_inv(fib_term)))

    def test_fib_sum(self):
        fib_sums = [0, 1, 2, 4, 7, 12, 20]
        for i, fib_term in enumerate(fib_sums):
            self.assertEqual(fib_term, Fib.fib_sum(i))

