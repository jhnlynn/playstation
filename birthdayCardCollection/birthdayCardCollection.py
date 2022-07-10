from typing import List


class BirthdayCardCollection:
    def birthday_card_collection(self, collections: List[int], budget: int) -> List[int]:
        """
        [1,2,3,4,5,6,7,8,9]
        [1,3]
        b: 5

        :param collections: [2,4,5]
        :param budget: 7
        :return:
        """
        collections.sort()
        to_buy = list(range(1, budget + 1))
        idx = 0
        res = []
        for t in to_buy:
            if budget < t: break
            if t == collections[idx]:
                idx += 1
                continue
            res.append(t)
            budget -= t
        return res


if __name__ == '__main__':
    bcc = BirthdayCardCollection()
    print(bcc.birthday_card_collection([2, 4, 5, 7, 9], 20))
    assert bcc.birthday_card_collection([2, 4, 5, 7, 9], 9) == [1, 3]
