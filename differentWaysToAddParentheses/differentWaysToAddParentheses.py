from collections import defaultdict
from typing import List


class DifferentWays:
    def __init__(self):
        self.memo = defaultdict(list)
        self.op = {'+', '-', '*'}

    def perform(self, left, right, exp):
        if exp == '+':
            return left + right
        elif exp == '-':
            return left - right
        else:
            return left * right

    def diffWaysToCompute(self, expression: str) -> List[int]:
        """

        """
        if expression in self.memo:
            return self.memo[expression]

        if ('+' not in expression) and ('-' not in expression) and ('*' not in expression):
            return [int(expression)]

        res = []

        for i, e in enumerate(expression):
            if not e.isdigit():
                left, right = self.diffWaysToCompute(expression[:i]), \
                              self.diffWaysToCompute(expression[i + 1:])
                for l in left:
                    for r in right:
                        res.append(self.perform(int(l), int(r), e))

        self.memo[expression] = res
        return res


if __name__ == '__main__':
    dw = DifferentWays()
    assert dw.diffWaysToCompute("2-1-1") == [0, 2] or dw.diffWaysToCompute("2-1-1") == [2, 0]
