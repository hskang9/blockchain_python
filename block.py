from time import time
import json
from hashlib import sha256
from pow import *
<<<<<<< HEAD
=======
import pickle

class Block():
    def __init__(self, _timestamp, _data,  _prevblockhash, _bits):
        self.Timestamp = _timestamp
        self.Data = _data
        self.PrevBlockHash = _prevblockhash
        self.Bits = _bits
        
>>>>>>> 5f5a8df1159de558af5cb0842dea9b4c7f9eeff1


class Block():
    def __init__(self, _timestamp, _merkleroot,  _prevhash, _bits):
        self.timestamp = _timestamp
        self.merkleroot = _merkleroot
        self.prevhash = _prevhash
        self.bits = _bits
        self.hash = b''
        self.nonce = 0
        self.nextbits = 0


    def new_block(self, _merkleroot: str, _prevhash: bytearray, _bits: int):
        """
        Create a new Block in the Blockchain
        :param _merkleroot: hash of the merkletree
        :param _prevhash: Hash of previous Block
        :return: New Block
        """
        block = Block(time(), _merkleroot, _prevhash, _bits)
        pow = ProofOfWork(block)
        nonce, hash, nextbits = pow.run()

        # Add new properties for mined block
        block.hash = hash
        block.nonce = nonce
        block.nextbits = nextbits

        return block
