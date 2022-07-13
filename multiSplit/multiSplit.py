import collections
from typing import List
import re


class MultiSplit:
    def multi_split(self, paragraph: str, banned: List[str]) -> List[str]:
        """
        check if some words in simple can be connected to a longer word (?)

        arr = s.split(s)
        new_arr = []

        :param S:
        :param simple:
        :return:
        """
        counters = collections.defaultdict(int)
        bannedSet = set(banned)

        for word in re.split("[!?',;. ]", paragraph):
            if word == '':
                continue

            lowWord = word.lower()
            if lowWord not in bannedSet:
                counters[lowWord] += 1

        return max(counters, key=counters.get)  # return the key by the largest value


if __name__ == '__main__':
    ms = MultiSplit()
    # assert ms.multi_split('this is a test, only a test!', ['is', 'a']) == ['th', ' ', ' ', ' test, only ', ' test!']
    print(ms.multi_split('this is a test, this is only a test!', ['his', 'th', 'on', 'tone']))
    print('this is a test, this is only a test!'.split('his'))
