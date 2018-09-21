# -*- coding: utf-8 -*-

"""blockchain.py

Usage:
  cli.py addblock -data <data>
  cli.py printchain

Options:
  -h --help     Show this screen.
  --version     Show version.
  -data         data to put in block


"""

import regex


from pprint import pprint

from docopt import docopt
from pow import *



def add_block(data):
    bc.add_block(data)
    return "Success!"


def printchain():

<<<<<<< HEAD
=======
    bci = bc.iterator
    bci.seek_to_first()
>>>>>>> 5f5a8df1159de558af5cb0842dea9b4c7f9eeff1
    print("------------ Chain Start ------------")
    for k, v in bc.storage.db.iterator(prefix=b'bk_'):
        if k is not None:
            block = bc.storage.get(k.decode())
            print(block)
            print("Prev. hash: %s\n" % (block.prevhash))
            print("Merkle Root: %s\n" % (block.merkleroot))
            print("Hash: %s\n" % (block.hash))
            pow = ProofOfWork(block)
            print("TargetBits: %s\n"%(block.bits))
            print("PoW: %s\n" % (pow.validate(block)))
<<<<<<< HEAD
            print("-------------------------------------")
=======
            bci.next()
>>>>>>> 5f5a8df1159de558af5cb0842dea9b4c7f9eeff1

    return "------------- Chain End --------------"


def Run(_blockchain):
    global bc
    bc = _blockchain
    arguments = docopt(__doc__, version='blockchain 1.0.0')
    if arguments['<data>']:
        print(add_block(arguments['<data>']))
    else:
        print(printchain())
