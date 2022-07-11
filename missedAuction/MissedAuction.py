from collections import deque
from typing import List
from heapq import heappop, heappush, heapify


class MissedAuction:
    """
    I. bidder with highest price gets the # of shares

    II. if multiple bidders have bid at the same price,
        1. each bidder gets 1 share consecutively (timestamp based),
        2. once the bidder gets == share, remove
        3. shares exhausted, or bidders are all removed


    List the userId's of all users who did not any share after shares exhausted,
    sorted ascending
    """

    def __init__(self):
        pass

    """
    bids: 
    [[u: id, sc: shares, bp: price, ts: timestamp]]
    totalShares: 
    """

    def getUnallottedUsers(self, bids: List[List[int]], totalShares: int) -> List[int]:
        """
        1. price
        2. timestamp (if prices are the same)

        pq: [[id, shares, bidding price, timestamp]]

        :param bids:
        :param totalShares:
        :return:
        """
        """
        1. build pq
        2. heappop and deal w/ same prices:
            1. 
                ```
                pq, q
                while pq and share > 0 and cur == pq[0]:
                    heappop(pq)
                    enqueue
                    share -= 1
                ```
            2. check if remaining shares enough
                1. if so, shares -= all needed
                2. else, brute force en and poll? Nah
                    1. if even not enough for 1 round:
                        stops in the above `while` loop
                        result: [share, len(q) - 1] + remaining in pq
                    2. result: only those in pq
                        [1,2,3] 2
        
        """
        # [[id, shares, bidding price, timestamp]]
        # price > timestamp
        pq, q = [], []  # [[id, shares, bidding price, timestamp]]
        for b in bids:
            x = (-b[2], b[3], b[1], b[0])  # [-price, timestamp, shares, id]
            heappush(pq, x)
        while pq and totalShares > 0:
            top = heappop(pq)
            if pq and top[0] == pq[0][0]:
                q.append(top)
                while pq and pq[0][0] == top[0]:
                    q.append(heappop(pq))
            else:
                if totalShares <= -top[0]:
                    return sorted([i[3] for i in pq])
                totalShares -= -top[0]
            if q:
                q.sort(key=lambda a: a[1])  # sort by timestamp
                total = sum(q[i][2] for i in range(len(q)))
                if totalShares <= total:
                    if totalShares < len(q):
                        return sorted([i[3] for i in q[totalShares:]] + [i[3] for i in pq])
                    else:
                        return sorted([i[3] for i in pq])
                else:
                    totalShares -= total
                q.clear()

        return []


if __name__ == '__main__':
    ma = MissedAuction()
    assert ma.getUnallottedUsers([[1, 5, 5, 0], [2, 7, 8, 1], [3, 7, 5, 1], [4, 10, 3, 3]], 18) == [4]
    print(ma.getUnallottedUsers([[1, 5, 5, 0], [2, 7, 8, 1], [3, 7, 5, 1], [4, 10, 3, 3]], 10))
