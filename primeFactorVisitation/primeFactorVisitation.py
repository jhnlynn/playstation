from collections import defaultdict
from math import isqrt
from typing import List


class PrimeFactorVisitation:
    def sieve(self, maxn):
        sf = list(range(maxn + 1))
        for i in range(4, len(sf), 2):
            sf[i] = 2
        for p in range(3, isqrt(maxn) + 1, 2):
            if sf[p] == p:
                for i in range(p * p, len(sf), p + p):
                    if sf[i] == i:
                        sf[i] = p
        return sf

    def prime_factor_visitation(self, states: List[int], numbers: List[int]) -> List[int]:
        def upf(n, sf):
            result = []
            while n > 1:
                p = sf[n]
                result.append(p)
                n //= p
                while n % p == 0:
                    n //= p
            return result

        sf = self.sieve(max(numbers))

        def crunch():
            pcount = defaultdict(int)
            for num in numbers:
                for p in upf(num, sf):
                    pcount[p] += 1

            for p, count in pcount.items():
                if count & 1:
                    for i in range(p - 1, len(states), p):
                        states[i] = 1 - states[i]

        crunch()
        return states


if __name__ == '__main__':
    pfv = PrimeFactorVisitation()
    assert pfv.prime_factor_visitation([1, 1, 0, 0, 1, 1, 0, 1, 1, 1], [3, 4, 15]) == [1, 0, 0, 1, 0, 0, 0, 0, 1, 1]
