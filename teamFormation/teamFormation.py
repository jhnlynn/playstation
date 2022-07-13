from typing import List


class TeamFormation:
    def team_formation(self, skill: List[int], miniPlayers: int, miniLevel: int, maxLevel: int) -> int:
        """
        1. # of valid rosters
        2. factorial: DP

        :param skill:
        :param miniPlayers:
        :param miniLevel:
        :param maxLevel:
        :return:
        """
        res, valid = 0, 0
        for t in skill:
            if miniLevel <= t <= maxLevel:
                valid += 1
        if valid < miniPlayers: return 0
        if valid == miniPlayers: return 1
        facts = {1: 1}

        def combinations(miniPlayer, num) -> int:
            ret = 0
            for i in range(miniPlayer, num):
                ret += fact(num) / (fact(i) * fact(num - i))
            return ret + 1

        def fact(num):
            if num in facts:
                return facts[num]
            if num == 1:
                return 1
            facts[num] = num * fact(num - 1)
            return num * fact(num - 1)

        return combinations(miniPlayers, valid)


if __name__ == '__main__':
    tf = TeamFormation()
    assert tf.team_formation([12, 4, 6, 13, 5, 10], 3, 4, 10) == 5
