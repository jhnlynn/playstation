import math
from typing import List


class AutoscalePolicy:
    def auto_scale_policy(self, inst: int, arr: List[int]) -> int:
        """
        < 25: if instances > 1: inst = ceil(inst/2)
        [25, 60]: nothing
        > 60: if inst <= 1*10**8: inst *= 2

        once take action, skip 10 seconds

        :param inst: 2
        :param arr: [25,23,1,2,3,4,5,6,7,8,9,10,76,80]
        :return: 2
        """
        i = 0
        while i < len(arr):
            if arr[i] < 25:
                inst = math.ceil(inst/2)
                i += 10
            elif arr[i] > 60 and inst <= 10**8:
                inst *= 2
                i += 10
            i += 1
        return inst


if __name__ == '__main__':
    ap = AutoscalePolicy()
    assert ap.auto_scale_policy(2, [25, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 76, 80]) == 2
    assert ap.auto_scale_policy(5, [30, 5, 4, 8, 19, 89]) == 3
