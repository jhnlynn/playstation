from collections import defaultdict


class Solution:
    def minWindow(self, S: str, T: str) -> str:
        """
        ADOBECODEBANC t = 'ABCC'
        |           |

        a: 0, b: 0, c: 0
        seen = 2
        desire = 3

        ADOBECODEBANC, t = "ABC"
             |    |

        seen = 3
        desire = 3
        a: -1, b: -1, c: 0
        exceed:
        a: 1, b: 1, c: 0

        permutation in string-ii?? lol
                   1234567
        adobecodebancbbcaa "abc"
                    |

        seen = 0
        desire = 3
        a: 0, b: -1, c: -1
        exceed:
        a: 0, b: 1, c: 1
        """
        hm, exceed = defaultdict(int), defaultdict(int)
        for t in T:
            hm[t] += 1
        seen, desire, i, res = 0, len(hm), 0, len(S) + 1
        ret = ''
        for j, s in enumerate(S):
            if s in hm:
                hm[s] -= 1
                if hm[s] == 0: seen += 1
                if hm[s] < 0:
                    exceed[s] = 0 - hm[s]
            while i < len(S) and seen == desire and ((S[i] in hm and exceed[S[i]] > 0) or (S[i] not in hm)):
                if S[i] in hm and exceed[S[i]] > 0:
                    exceed[S[i]] -= 1
                    hm[S[i]] += 1
                    if hm[s] == 1: print(i, j)
                i += 1
            if seen == desire:
                if res > j - i + 1:
                    ret = S[i:j + 1]
                    res = j - i + 1
        return ret


if __name__ == '__main__':
    sol = Solution()
    print(sol.minWindow('adobecodebancbbcaa', 'abc'))
