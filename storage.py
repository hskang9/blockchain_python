import plyvel
import pickle

chainDB= './chaindata'

class Storage():
    def __init__(self):
        self.db = plyvel.DB(chainDB, create_if_missing=True)
        self.raw_iterator = self.db.raw_iterator()

    def put(self, key, value):
        self.db.put(key.encode(), pickle.dumps(value))

    def get(self, key):
        raw = self.db.get(key.encode())
        result = pickle.loads(raw)
        return result

    def get_block_height(self):
        height = 0
        for key, value in self.db.iterator(prefix=b'bk_'):
            height += 1
        return height

    def get_transactions(self):
        txs = 0
        for key, value in self.db.iterator(prefix=b'tx_'):
            txs += 1
        return txs
