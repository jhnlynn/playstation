from typing import List


class TaskQueue:
    def task_queue(self, n: int, batchSize: List[int], processingTime: List[int], numTasks: List[int]) -> int:
        """
        timeCost[i] = (numTasks[i] // batchSize[i] + 1) * processingTime[i]
        max(timeCost)

        :param n: [1, 10^5]
        :param batchSize:
        :param processingTime:
        :param numTasks:
        :return:
        """


if __name__ == '__main__':
    tq = TaskQueue()
    assert tq.task_queue(2, [4, 3], [6, 5], [8, 8]) == 15
