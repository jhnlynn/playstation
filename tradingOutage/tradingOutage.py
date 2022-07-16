from typing import List


class TradingOutage:
    def tradingOutage(self, S: List[str]) -> str:
        S.sort()
        n = len(S)

        def get_sec(timestamp):
            return timestamp.split(':')[2].split('.')[0]

        for i in range(1, n):
            f, e = get_sec(S[i-1]), get_sec(S[i])
            if int(e) - int(f) > 1:
                return S[i-1] + '-' + S[i]

        return ''


if __name__ == '__main__':
    to = TradingOutage()
    assert to.tradingOutage(["12:31:04.04",
                             "12:31:05.01",
                             "12:31:06.21",
                             "12:31:14.39",
                             "12:31:15.13",
                             "12:31:16.98",
                             "12:31:17.09"]) == '12:31:06.21-12:31:14.39'
