from typing import List


class PortfolioBalances:
    def portfolio_balances(self, n: int, rounds: List[List[int]]) -> int:
        """


        :param n: 3
        :param rounds: [[1, 2, 10], [2, 4, 5], [3, 5, 12]]
        :return:
        """
        invest = [0 for _ in range(n)]
        for round in rounds:
            invest[round[0] - 1] += round[2]
            if round[1] < n:
                invest[round[1]] -= round[2]

        cur = 0
        max_val = 0
        for val in invest:
            cur += val
            max_val = max(max_val, cur)
        return max_val


if __name__ == '__main__':
    pb = PortfolioBalances()
    assert pb.portfolio_balances(5, [[1, 2, 10], [2, 4, 5], [3, 5, 12]]) == 17
