from functools import cache
from typing import List


class Inversions:
    def inversions(self, n: int, arr: List[int]) -> int:
        """
        merge sort ///


        :param n: 5
        :param arr: [5,3,4,2,1]
        :return:
        """

        @cache
        def dp(idx, k, max_val):
            if idx == len(arr):
                if k == 0:
                    return 1
                else:
                    return 0
            with_first = dp(idx + 1, k - 1, arr[idx]) if arr[idx] < max_val else 0
            without_first = dp(idx + 1, k, max_val)
            return with_first + without_first

        return dp(0, 3, float('inf'))


if __name__ == '__main__':
    i = Inversions()
    assert i.inversions(5, [5, 3, 4, 2, 1]) == 7
