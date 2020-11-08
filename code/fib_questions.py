"""Finds the closest fib number to a given input"""
import numpy as np


class Fib:

    def __init__(self):
        ...

    @staticmethod
    def fib_term(fib_index: int) -> int:
        """returns fib number at index n"""
        golden_ratio = (1 + np.sqrt(5)) / 2
        result = int(round((golden_ratio**fib_index - (1-golden_ratio)**fib_index) / np.sqrt(5)))
        return result

    @staticmethod
    def fib_inv(f):
        """returns index of fib number f, if f is not a fib number,
        then return closet fib number index, Binet's formula"""
        if f < 2:
            return f

        golden_ratio = (1 + np.sqrt(5)) / 2
        return int(round(np.log(f * np.sqrt(5)) / np.log(golden_ratio)))

    @staticmethod
    def fib_num(fib_index: int) -> int:
        if fib_index in [0, 1]:
            return fib_index

        first_n = 0
        second_n = 1

        for _ in range(1, fib_index):
            temp = first_n + second_n
            first_n = second_n
            second_n = temp

        return second_n

    @staticmethod
    def fib_sum(fib_term: int) -> int:
        """
        Return the sum of n elements of the Fibonacci sequence
        """
        total = 0
        for fib_index in range(fib_term + 1):
            total += Fib.fib_num(fib_index)
        return total

    @staticmethod
    def next_fib_num(prev: int, curr: int) -> tuple:
        return curr, prev + curr

    @staticmethod
    def closest_fib_num(num: int) -> int:
        curr = 1
        prev = 0

        while curr < num:
            prev, curr = Fib.next_fib_num(prev, curr)

        if abs(curr - num) < abs(prev-num):
            return curr
        else:
            return prev
