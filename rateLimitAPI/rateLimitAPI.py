from collections import defaultdict
from heapq import heappop
from typing import List


class RateLimit:
    def rate_limit(self, time_window: float, limit: int, events: List[str]) -> List[int]:
        """
        pq from user2share
        # timestamp, ops, user
        limits[user] = limit
        [(0, 10), (30, 10), ()]
        if use not in user2share:
            user2share[user] = []
            limits[user] = limit
        pq = user2share[user]
        cur_lim = limits[user]
        while pq and time - pq[0][0] > time_window:
            cur_lim += pq[0][1]
            heappop(pq)

        if cur_lim > 0:
            cur_lim = max(0, cur_lim - ops)
            ops = min(cur_lim, ops)
            pq.append((time, ops))
            res.append(ops)
        else:
            res.append(0)
        """
        user2shares = {}
        limits = {}
        res = []
        for event in events:
            e = event.split(' ')
            time, ops, user = int(e[0]), int(e[1]), e[2]
            if user not in user2shares:
                user2shares[user] = []
                limits[user] = limit
            pq, cur_lim = user2shares[user], limits[user]
            while pq and time - pq[0][0] > time_window:
                cur_lim += pq[0][1]
                heappop(pq)
            if cur_lim > 0:
                ops = min(ops, cur_lim)
                cur_lim = max(0, cur_lim - ops)
                pq.append((time, ops))
                res.append(ops)
            else:
                res.append(0)
            limits[user] = cur_lim

        return res


if __name__ == '__main__':
    """
    Input Format:
    time_window: float
    limit: int
    num of events: int
    evt1: Event
    evt2: Event
    ...
    
    INPUT:
    60.0
    30
    5
    155931800 10 Vlad
    155931830 10 Vlad
    155931840 20 Vlad
    155931840 20 Vlad_alchemist
    155931870 20 Vlad
    
    OUTPUT:
    10
    10
    10
    20
    10
    """
    rl = RateLimit()
    print(rl.rate_limit(60.0, 30, ['155931800 10 Vlad',
                                   '155931830 10 Vlad',
                                   '155931840 20 Vlad',
                                   '155931840 20 Vlad_alchemist',
                                   '155931870 20 Vlad']))
