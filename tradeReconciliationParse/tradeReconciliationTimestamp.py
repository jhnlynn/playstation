class TradeReconciliationParsing:
    def __init__(self):
        self.record_hist = {}
        self.dic = {}

    def trade_recon(self, line: str) -> str:
        source, *element = line.split(',')
        if source != 'RECONCILIATION':
            product, quantity, timestamp = element
            if source not in self.record_hist:
                self.record_hist[source] = [(product, quantity, timestamp)]
            else:
                self.record_hist[source].append((product, quantity, timestamp))
            return quantity
        else:
            first_source, counterpart = element
            if first_source not in self.record_hist:
                return '0'
            elif counterpart not in self.record_hist:
                return str(len(self.record_hist[first_source]))
            else:
                filtered_trade_list = list(
                    filter(lambda x: x not in self.record_hist[counterpart], self.record_hist[first_source])
                )
                return str(len(filtered_trade_list))

    def trade_recon2(self, line: str) -> str:
        """
        trading:
            source, product, quantity, timestamp
        RECONCILIATION:
            recon, recon_source, counterparty

        :param line:
        :return:
        """
        source, *latter = line.split(',')
        if source == 'RECONCILIATION':
            recon_source, counterparty = latter
            if recon_source not in self.dic:
                return '0'
            elif counterparty not in self.dic:
                return str(len(self.dic[recon_source]))
            else:
                rem = []
                for s in self.dic[recon_source]:
                    if s not in self.dic[counterparty]:
                        rem.append(s)
                return str(len(rem))
        else:
            product, quantity, timestamp = latter
            if source not in self.dic:
                self.dic[source] = [(product, quantity, timestamp)]
            else:
                self.dic[source].append((product, quantity, timestamp))
            return quantity


if __name__ == '__main__':
    tr = TradeReconciliationParsing()
    print(tr.trade_recon2('AKUNA,A,10,12: 01:00'), tr.trade_recon('AKUNA,A,10,12: 01:00'))
    print(tr.trade_recon2('AKUNA,B,-15,12: 05:00'), tr.trade_recon('AKUNA,B,-15,12: 05:00'))
    print(tr.trade_recon2('RECONCILIATION,AKUNA,EXCHANGE1'), tr.trade_recon('RECONCILIATION,AKUNA,EXCHANGE1'))
    print(tr.trade_recon2('RECONCILIATION,EXCHANGE1,AKUNA'), tr.trade_recon('RECONCILIATION,EXCHANGE1,AKUNA'))
    print(tr.trade_recon2('EXCHANGE1,B,-15,12: 05:00'), tr.trade_recon('EXCHANGE1,B,-15,12: 05:00'))
    print(tr.trade_recon2('EXCHANGE1,B,-20,12: 07:00'), tr.trade_recon('EXCHANGE1,B,-20,12: 07:00'))
    print(tr.trade_recon2('RECONCILIATION,AKUNA,EXCHANGE1'), tr.trade_recon('RECONCILIATION,AKUNA,EXCHANGE1'))
    print(tr.trade_recon2('RECONCILIATION,EXCHANGE1,AKUNA'), tr.trade_recon('RECONCILIATION,EXCHANGE1,AKUNA'))
    print(tr.trade_recon2('RECONCILIATION,EXCHANGE2,AKUNA'), tr.trade_recon('RECONCILIATION,EXCHANGE2,AKUNA'))

