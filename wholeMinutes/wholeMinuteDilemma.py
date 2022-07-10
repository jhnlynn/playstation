from collections import Counter
from typing import List


class WholeMinuteDilemma:
    def wholeMinuteDilemma(self, n: int, songs: List[int]) -> int:
        """
        [40,20,60]

        :param n: 3
        :param songs: [40,20,60]
        :return:
        """
        wholeMinutes = [60 * i for i in range(1, 2000 // 60 + 1)]
        counter = Counter(songs)  # {40: 1, 20: 1, 60: 1}
        res = 0
        song_set = set([k for k in counter])
        for song in song_set:

            for duration in wholeMinutes:
                diff = duration - song
                # if diff < 0, will not go into `if` statement
                if diff in counter:
                    if diff * 2 == duration:
                        # print('same! ', diff, counter[diff], ', addition: ', counter[diff] * (counter[diff] - 1) // 2)
                        res += counter[diff] * (counter[diff] - 1) // 2
                    else:
                        # print('diff: ', diff, ', song: ', song, ', addition: ', counter[diff] * counter[song])
                        res += counter[diff] * counter[song]
            del counter[song]

        return res

    def wholeMinuteDilemma2(self, n: int, songs: List[int]) -> int:
        bucket = [0 for _ in range(60)]
        res = 0
        for song in songs:
            song = song % 60
            res += (bucket[0] if song == 0 else bucket[60 - song])
            bucket[song] += 1

        return res


if __name__ == '__main__':
    wmd = WholeMinuteDilemma()
    assert wmd.wholeMinuteDilemma(5, [300, 60, 120, 180, 60]) == 10
    assert wmd.wholeMinuteDilemma(3, [40, 20, 60]) == 1
    assert wmd.wholeMinuteDilemma2(5, [300, 60, 120, 180, 60]) == 10
