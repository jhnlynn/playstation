import collections
from typing import List
import re


class MultiSplit:
    def multi_split(self, S: str, simple: List[str]) -> List[str]:
        """
        check wordsets overlap (?)

        arr = s.split(s)
        new_arr = []

        :param S:
        :param simple:
        :return:
        """
        wordSet = set(simple)
        n = len(simple)

        def overlap(w1, w2):
            """
            w1: 'th', w2: 'his'
            can be:
            1. [<-][->]
            2. [->][<-]
            """
            """
            th
            |
            his
             |
            """
            i, j = len(w1) - 1, 0

            if w1[i] == w2[j]:
                while i >= 0 and j < len(w2) and w1[i] == w2[j]:
                    i, j = i - 1, j + 1
                wordSet.add(w1[:i+1] + w2)

            # 'his', 'th'
            i, j = 0, len(w2) - 1
            if w1[i] == w2[j]:
                while i < len(w1) and j >= 0 and w1[i] == w2[j]:
                    i, j = i + 1, j - 1
                wordSet.add(w2[:j+1] + w1)

        for i in range(n):
            for j in range(i + 1, n):
                overlap(simple[i], simple[j])

        arr, new = [S], []
        wordList = sorted(list(wordSet), key=len)
        for w in wordList[::-1]:
            if arr:
                for a in arr:
                    if a:
                        new.extend(a.split(w))
                arr.clear()
            if new:
                for n in new:
                    if n:
                        arr.extend(n.split(w))
                new.clear()

        return arr if len(arr) > 0 else new


if __name__ == '__main__':
    ms = MultiSplit()
    # assert ms.multi_split('this is a test, only a test!', ['is', 'a']) == ['th', ' ', ' ', ' test, only ', ' test!']
    print(ms.multi_split('this is a test, this is only a test!', ['his', 'th']))
    print(ms.multi_split('this is a test, this is only a test!', ['is', 'a']))
    # print('this is a test, this is only a test!'.split('his'))
