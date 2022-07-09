from collections import defaultdict, Counter
from typing import List


class TripletsThreshold:
    def triplets(self, d: List[int], t: int) -> int:
        """

        :param d: [1,2,2,2,3,4,5], numbers can be dups
        :param t: 8
        :return: number of triplets

         0,1,2,3,4,5,6
        [1,2,2,2,3,4,5]
         | |         |

        3sum, but each number is different

        [1,2,3,4,5]
           |     |
        """
        counter = Counter(d)
        tmp = []
        res = 0
        for cnt in counter:
            tmp.append(cnt)
        tmp.sort()
        # [1,2,3,4,5], 8
        for i, num in enumerate(tmp):
            target, cnt = t - num, counter[num]
            l, r = i + 1, len(tmp) - 1
            while l < r:
                cur = tmp[l] + tmp[r]
                if cur > target:
                    r -= 1
                else:
                    res += cnt * counter[tmp[l]] * sum([counter[tmp[t]] for t in range(l + 1, r + 1)])
                    l += 1

        return res


if __name__ == '__main__':
    ttd = TripletsThreshold()
    print(ttd.triplets([1, 2, 2, 2, 3, 3, 4, 5, 5], 8))
    print(ttd.triplets([1, 2, 3, 4, 5], 8))
