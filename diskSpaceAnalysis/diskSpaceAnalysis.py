from collections import deque
from typing import List


class DiskSpaceAnalysis:
    def disk_space_analysis(self, x: int, space: List[int]) -> List[int]:
        """
        monotonic stack
        sliding window minimum
        [8,2,4,6]

        [8] 2 -> [2] i==1, res: [2]
        [2] 4 -> [2,4] i==2, res: [2,2]
        []

        :param x: 2
        :param space: [8,2,4,6]
        :return: [2,2,4]
        """
        dq, res = deque(), []
        for i, num in enumerate(space):
            while dq and i - x >= dq[0][-1]:
                dq.popleft()
            while dq and num < dq[-1][0]:
                dq.pop()
            dq.append((num, i))

            if i >= x - 1:
                res.append(dq[0][0])
        return res


if __name__ == '__main__':
    dsa = DiskSpaceAnalysis()
    assert dsa.disk_space_analysis(1, [1, 2, 3, 1, 2]) == [1, 2, 3, 1, 2]
    assert dsa.disk_space_analysis(2, [8, 2, 4, 6]) == [2, 2, 4]
