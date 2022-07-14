from typing import List


class ShippingRob:
    def shipping_rob(self, packages: List[int]) -> int:
        """
         0,1,2,3,4,5,6
        [5,3,4,7,1,9,2]
        [0,0,0,2,0,4,0]
        [0,0,0,0,0,2,0]

        (5*7 + 2*4 + 2*2) + sum(packages)
        rolling a snowball
        start = packages[0]
        res = [(5,7),(2,4),(2,2)]
        1. if start < packages[i]:
            res.append((packages[i] - start, n-i+1))
            start = packages[i]

        :param packages:
        :return:
        """
        n, _sum = len(packages), 0
        start = packages[0]
        res = [(start, n)]
        for i, p in enumerate(packages):
            _sum += p
            if start < p:
                res.append((p - start, n - i + 1))
                start = n
        return sum([a * b for a, b in res]) + _sum


if __name__ == '__main__':
    sr = ShippingRob()
    assert sr.shipping_rob([1, 2, 3]) == 12
    assert sr.shipping_rob([7, 4, 7]) == 39
