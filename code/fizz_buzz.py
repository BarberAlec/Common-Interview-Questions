"""Print Fizz if %3, Buzz if %5, FizzBuzz if %3 and %5, else number"""


class FizzBuzz:

    @staticmethod
    def fizzbuzz_build(i: int) -> str:
        s = ""
        if i > 0:
            if i % 3 == 0:
                s += "Fizz"
            if i % 5 == 0:
                s += "Buzz"
        if not s:
            s = i
        return s

    @staticmethod
    def fizzbuzz_simple(i: int) -> str:
        s = i
        if i > 0:
            if i % 15 == 0:
                s = "FizzBuzz"
            elif i % 3 == 0:
                s = "Fizz"
            elif i % 5 == 0:
                s = "Buzz"
        return s

    @staticmethod
    def fizzbuzz_complete(i: int) -> str:
        s = i
        if i > 0:
            if (i % 3 == 0) and (i % 5 == 0):
                s = "FizzBuzz"
            elif i % 3 == 0:
                s = "Fizz"
            elif i % 5 == 0:
                s = "Buzz"
        return s
