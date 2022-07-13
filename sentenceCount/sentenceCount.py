from collections import defaultdict
from typing import List


class SentenceCount:
    def sentence_count(self, wordSet: List[str], sentences: List[str]) -> List[int]:
        """
        iterate all words in wordSet, sort the word seen, and count
        {'listen': 2, 'it': 1, 'is': 1}

        :param sentences:
        :param wordSet:
        :return:
        """
        cnt = defaultdict(int)
        res = []
        for word in wordSet:
            cnt[''.join(sorted(word))] += 1
        for sentence in sentences:
            cur = 0
            for s in sentence.split():
                rs = ''.join(sorted(s))
                if rs in cnt:
                    cur = cur + cnt[rs] if cur == 0 else cur * cnt[rs]
            res.append(cur)
        return res


if __name__ == '__main__':
    sc = SentenceCount()
    assert sc.sentence_count(['listen', 'silent', 'it', 'is'], ['listen is silent']) == [4]
    assert sc.sentence_count(['the', 'bats', 'tabs', 'in', 'cat', 'act'],
                             ['cat the bats', 'in the act', 'act tabs in']) == [4, 2, 4]
