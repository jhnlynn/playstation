from typing import List


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

        pq: [[price, timestamp, number of shares, id]]

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
                2. else, brute force en and poll?
                    1. if even not enough for 1 round:
                        result: [share, len(q) - 1] + remaining in pq
                    2. result: only those in pq
                        [1,2,3] 2
        
        """

