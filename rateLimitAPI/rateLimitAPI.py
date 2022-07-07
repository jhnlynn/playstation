from collections import defaultdict


class Event:
    def __init__(self, Timestamp: str, NumberOfOperations: int, Consumer: int):
        self.__Timestamp = Timestamp
        self.NumberOfOperations = NumberOfOperations
        self.Consumer = Consumer


class RateLimit:
    def __init__(self, time_window, limit):
        self.__time_window = time_window
        self.__limit = limit
        self.__num_event = 0
        self.__max_each_event = self.__limit
        self.__consumer_map = defaultdict(int)

    def num_event(self, num_event):
        self.__num_event = num_event
        self.__max_each_event = max(self.__max_each_event, self.__time_window / self.__limit)

    def rate_limit(self, event: Event) -> int:
        """
        called on the receipt of an event

        :param event:
        :return: denotes the # of operations that will be processed
        """
        # allow at most `limit` number of operations,
        # for any particular `time_window` PER user
        """
        5 events, 60 time_window, 30 as processing limit 
        if one consumer has too many events in the past, 
                we should assign the other with the current tasks
        """


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
    rl = RateLimit(60.0, 30)
    rl.rate_limit(Event('1559318000', 10, 'Vlad'))
