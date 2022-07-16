from datetime import datetime, timedelta
from typing import List


class TradeReconciliationTimestamp:
    def __init__(self):
        self.record_hist = {}

    def trade_recon(self, trades: List[str]) -> bool:
        for t in trades:
            source, product, quantity, timestamp = t.split(',')
            self.record_hist[source] = self.record_hist.setdefault(source, [])
            self.record_hist[source].append((product, quantity, timestamp))

        if len(self.record_hist['AKUNA']) != len(self.record_hist['EXCHANGE']):
            return False
        v = set()
        for product, quantity, timestamp in self.record_hist['AKUNA']:
            recon = False
            for p, q, t in self.record_hist['EXCHANGE']:
                from_time = datetime.strptime(timestamp, '%H:%M:%S')
                to_time = datetime.strptime(t, '%H:%M:%S')
                if (p, q, t) not in v:
                    if product == p and quantity == q and abs(from_time - to_time) <= timedelta(minutes=5):
                        recon = True
                        v.add((p, q, t))
                        break
            if not recon:
                return False
        return True


if __name__ == '__main__':
    tr = TradeReconciliationTimestamp()
    assert tr.trade_recon(['AKUNA,A,10,11:59:00',
                           'AKUNA,B,-15,12:05:00',
                           'EXCHANGE,A,10,12:01:00',
                           'EXCHANGE,B,-15,12:09:00'])
    assert tr.trade_recon(['AKUNA,A,10,11:01:00',
                           'AKUNA,A,10,11:02:00',
                           'AKUNA,A,10,11:03:00',
                           'EXCHANGE,A,10,11:04:00',
                           'EXCHANGE,A,10,11:02:00',
                           'EXCHANGE,A,10,11:03:00'])
    assert not tr.trade_recon(['EXCHANGE,A,10,11:59:00',
                               'AKUNA,A,10,11:59:00',
                               'EXCHANGE,A,10,12:00:00',
                               'EXCHANGE,B,12,15:01:03',
                               'EXCHANGE,H,-50,16:14:02',
                               'AKUNA,A,10,11:53:00',
                               'AKUNA,A,10,12:00:00',
                               'EXCHANGE,A,10,12:01:00',
                               'AKUNA,B,12,15:01:02',
                               'AKUNA,H,-50,16:19:02'])

"""
'AKUNA,A,10,11:59:00',
'AKUNA,B,-15,12:05:00',
'EXCHANGE,A,10,12:01:00',
'EXCHANGE,B,-15,12:09:00'

'AKUNA,A,10,11:01:00'
'AKUNA,A,10,11:02:00'
'AKUNA,A,10,11:03:00'
'EXCHANGE,A,10,11:04:00'
'EXCHANGE,A,10,11:02:00'
'EXCHANGE,A,10,11:03:00'

'EXCHANGE,A,10,11:59:00'
'AKUNA,A,10,11:59:00'
'EXCHANGE,A,10,12:00:00'
'EXCHANGE,B,12,15:01:03'
'EXCHANGE,H,-50,16:14:02'
'AKUNA,A,10,11:53:00'
'AKUNA,A,10,12:00:00'
'EXCHANGE,A,10,12:01:00'
'AKUNA,B,12,15:01:02'
'AKUNA,H,-50,16:19:02'
"""
