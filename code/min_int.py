"""Find the smallest positive integer not in the array"""


class MinInt:

    @staticmethod
    def using_xor(a: list) -> int:
        min_int = 1
        a_pos_sorted = sorted(list(set(filter(lambda x: x > 0, a))))
        if a_pos_sorted:
            max_int = len(a_pos_sorted) + 1
            nums = list(range(1, max_int))
            x_nums = sorted(set(a_pos_sorted) ^ set(nums))
            if x_nums:
                min_int = x_nums[0]
            else:
                min_int = max_int

        return min_int

    @staticmethod
    def quick_search(a: list) -> int:
        min_int = 1
        a_pos_sorted = sorted(set(filter(lambda x: x > 0, a)))

        for i in a_pos_sorted:
            if i == min_int:
                min_int += 1
            elif i > min_int:
                break

        return min_int
