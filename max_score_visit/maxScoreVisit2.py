from collections import defaultdict
from typing import List
from heapq import heappush, heappop


class MaxScoreVisit2:
    def __init__(self):
        self.res = 0

    def find(self, siteScores: List[int], trainRoutes: List[List[int]]) -> int:
        """
        0.	Build Graph
        1.	Then iterate through siteScores, using backtracking to find the maximum:
        	if len(ls) == 4:
        res = max(res, sum(ls))
        return
        ...


        :param siteScores: [90, 95, 80, 85, 70]
        :param trainRoutes: [[0, 4], [1, 2], [2, 3], [1, 0], [0, 2], [4, 3]]
        :return:
        """
        graph = defaultdict(list)
        idx2site = {}
        head2score = defaultdict(dict)  # {0: [1: 2: 3: 4:], 1: []}
        # build graph
        for s, e in trainRoutes:
            graph[s].append(e)
        for i, site in enumerate(siteScores):
            idx2site[i] = site
        #  {0: [4,2], 1: [2,0], 2: [3], 4: [3]}
        """
        ls: 3
        need: 1

        0 - 4 - 3 : 
        0 - 2 - 3 : 

        """

        def backtrack(node, ls, total, visited, origin):
            if ls > 4: return
            if ls == 4:
                self.res = max(self.res, total)
                return
            if 4 - ls in head2score[node]:
                self.res = max(total + head2score[node][4-ls], self.res)
                return
            visited.add(node)  # v: {0,4}

            if ls not in head2score[origin]:
                head2score[origin] = total
            else:
                head2score[origin][ls] = max(head2score[origin][ls], total)

            for nei in graph[node]:
                if nei in visited: continue
                visited.add(nei)
                backtrack(nei, ls + 1, total + idx2site[nei], visited, origin)
                visited.remove(nei)

        for i in range(len(siteScores)):
            head2score[i][1] = idx2site[i]
            backtrack(i, 1, idx2site[i], set(), i)
        print(head2score)
        return self.res


if __name__ == '__main__':
    m = MaxScoreVisit2()
    print(m.find([90, 95, 80, 85, 70], [[0, 4], [1, 2], [2, 3], [1, 0], [0, 2], [4, 3]]))
