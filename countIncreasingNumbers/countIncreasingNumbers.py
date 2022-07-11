from functools import cache
from typing import List


class CountIncreasingNumbers:
    """
    Inversion's reversed version
    """

    def count_increasing_numbers(self, arr: List[int], x: int) -> int:
        """

        :param arr:
        :return:
        """

        @cache
        def dp(idx, k, min_val):
            if idx == len(arr):
                if k == 0:
                    return 1
                else:
                    return 0
            with_first = dp(idx + 1, k - 1, arr[idx]) if arr[idx] > min_val else 0
            without_first = dp(idx + 1, k, min_val)
            return with_first + without_first

        return dp(0, x, -float('inf'))


if __name__ == '__main__':
    cin = CountIncreasingNumbers()
    assert cin.count_increasing_numbers([1, 2, 3, 4, 5], 4) == 5
    assert cin.count_increasing_numbers([1, 3, 3, 4, 5], 4) == 2
    assert cin.count_increasing_numbers([1, 4, 1, 4, 5], 3) == 3
