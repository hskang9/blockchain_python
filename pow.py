from hashlib import sha256
import sys
from tqdm import trange
from time import time
from bitstring import BitArray



class ProofOfWork():

  def __init__(self, _block):
      self.block = _block
      # target value
      self.target = 1 << (256 - _block.bits)
      # Time interval for each block generation in second
      self.interval = 3

  def adjust_difficulty(self, _interval: int):
      if _interval < self.interval:
          print("Increase difficulty")
          return self.block.bits + 1

      elif _interval > self.interval:
          print("Decrease difficulty")
          return self.block.bits - 1


  def prepare_data(self, _nonce: int):
      data = ''.join([str(self.block.prevhash) + self.block.merkleroot + hex(int(self.block.timestamp))[2:] + hex(self.block.bits)[2:] + hex(_nonce)[2:]])

      return data


  def run(self):
      nonce = 0
      for i in trange(sys.maxsize, desc="Mining...."):
          # Get flattened data for generating block hash
          data = self.prepare_data(nonce)
          hash = sha256(data.encode()).hexdigest()
          hash_int = int(hash, 16)
          if(hash_int < self.target):
              break
          nonce += 1

      # Set target_bits based on elapsed time for mining
      elapsed = time()

      mine_interval = int(elapsed - self.block.timestamp)


      nextbits = self.adjust_difficulty(mine_interval)



      return nonce, hash, nextbits

  def validate(self, _block):
      pow = ProofOfWork(_block)
      data = pow.prepare_data(_block.nonce)
      hash = sha256(data.encode("utf-8")).hexdigest()
      return int(hash, 16) < 1 << (256 - _block.bits)
