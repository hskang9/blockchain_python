
class Txin():
    def __init__(self):
        self.id = b''
        self.scriptsig = ''


class Txout():
    def __init__(self):
        self.amount = 0
        self.scriptpubkey = ''




class Transaction():
    def __init__(self):
        self.id = b''
        self.input = list()
        self.output = list()
