from functools import cache
from typing import List


class LongestStringChain:
    def longest_string_chain(self, words: List[str]) -> int:
        word_set = set(words)
        max_len = 0

        @cache
        def dfs(word):
            if not word:
                return 0
            res = 1
            for i in range(len(word)):
                new_word = word[:i] + word[i + 1:]
                if new_word in word_set:
                    res = max(res, dfs(new_word) + 1)
            return res

        for word in sorted(words, key=len):
            max_len = max(max_len, dfs(word))

        return max_len


if __name__ == '__main__':
    lsc = LongestStringChain()
    assert lsc.longest_string_chain(["a", "b", "ba", "bca", "bda", "bdca"]) == 4
    assert lsc.longest_string_chain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]) == 5
    assert lsc.longest_string_chain(["abcd", "dbqca"]) == 1
