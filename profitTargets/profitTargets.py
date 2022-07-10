class ProfitTargets:
    def profit_targets(self, stocksProfit, target) -> int:
        """
        distinct pairs
        :param stocksProfit: [5,7,9,13,11,6,6,3,3]
        :param target: 12
        :return: number of distinct pairs

        * sort,
        * two pointers
        * if found a pair, skip all dups from left and right respectively
        [3,3,5,6,6,7,9,11,13]
               | |

        OR
        do as `two sum`, and store the pairs
        pass, this cannot be a valid solution. i.e., 6 + 6 = 12
        b/c needs the numbers to be distinct
        """
        stocksProfit.sort()
        res = 0
        l, r = 0, len(stocksProfit) - 1
        while l < r:
            cur = stocksProfit[l] + stocksProfit[r]
            if cur > target:
                r -= 1
            elif cur < target:
                l += 1
            else:
                # skip all the dups
                res += 1
                while l < r and stocksProfit[l] == stocksProfit[l + 1]:
                    l += 1
                while l < r and stocksProfit[r] == stocksProfit[r - 1]:
                    r -= 1
                l, r = l + 1, r - 1

        return res

    def profit_targets2(self, profits, target) -> int:
        res, comp = set(), set()
        for i, p in enumerate(profits):
            cur = target - p
            if cur in comp:
                ans = (p, cur) if p > cur else (cur, p)
                if ans not in res:
                    res.add(ans)
            comp.add(p)
        return len(res)


if __name__ == '__main__':
    pt = ProfitTargets()
    assert pt.profit_targets2([3, 3, 5, 6, 6, 7, 9, 11, 13], 12) == 3
    assert pt.profit_targets2([1, 3, 46, 1, 3, 9], 47) == 1
    assert pt.profit_targets2([6, 6, 3, 9, 3, 5, 1], 12) == 2
