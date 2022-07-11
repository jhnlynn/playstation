from heapq import heappop, heapify


def some_interesting():
    pq, q = [-5, -1, -3, -5, -8], []
    heapify(pq)
    totalShares = 18
    while pq and totalShares > 0:
        top = heappop(pq)
        if pq and top == pq[0]:
            q.append(top)
            while pq and pq[0] == top:
                q.append(heappop(pq))
        else:
            totalShares -= -top
        if q:
            totalShares -= -sum(q)
        print('top: ', top)
        print('q: ', q)
        print('totalShares: ', totalShares)


if __name__ == '__main__':
    some_interesting()
