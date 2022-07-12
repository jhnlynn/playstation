from functools import cache, cached_property, lru_cache
from typing import List


class GlobalMax:
    def __init__(self):
        self.maxv = 0

    def global_max(self, arr: List[int], m: int) -> int:
        """
        0. sort the arr
        1. pick or not, if m == len(picked), calculate, terminate;
            if run out of, terminate
        2. check for the minimum difference b/t random 2 numbers:
            just keep sml, and a minimum flag
            if num - sml < _min:
                _min = num-sml
            sml = num

        dp(m, sml, _min)


        :param arr: [2,3,5,9]
        :param m: 3
        :return: 3
        """
        arr.sort()

        @lru_cache(maxsize=None)
        def dp(sml, _min, total, idx):  # sml: initial: -1
            if total == m:
                self.maxv = max(self.maxv, _min)
                return
            if idx == len(arr):
                return

            # pick or not
            x = arr[idx]
            dp(sml, _min, total, idx + 1)
            if sml != -1:
                _min = min(_min, x - sml)
            sml = x
            dp(sml, _min, total + 1, idx + 1)

        dp(-1, 10 ** 9, 0, 0)
        dp.cache_clear()
        return self.maxv

    def global_max2(self, arr: List[int], m: int) -> int:
        def can_do(diff) -> bool:
            cnt, prev = 1, arr[0]
            for i in range(1, len(arr)):
                if arr[i] - prev >= diff:
                    cnt += 1
                    if cnt == m:
                        return True
                    prev = arr[i]
            return False

        arr.sort()
        s, e = arr[0], arr[-1]
        res = 0
        while s <= e:
            mid = (s + e) // 2
            if can_do(mid):
                res = mid
                s = mid + 1
            else:
                e = mid - 1

        return res


if __name__ == '__main__':
    assert GlobalMax().global_max2([2, 3, 5, 9], 3) == 3
    assert GlobalMax().global_max2([1, 2, 3, 4], 3) == 1
