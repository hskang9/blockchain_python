from block import Block
import merkletools
from storage import Storage
import transactions as tx




class Blockchain(Block):

<<<<<<< HEAD
    def __init__(self):
        self.pool = merkletools.MerkleTools(hash_type="sha256")
        self.storage = Storage()
        self.new_blockchain()


    # Blockchain methods
=======

    def __init__(self, _db_file: str):
        self.db = plyvel.DB(_db_file, create_if_missing=True)
        self.iterator = self.db.raw_iterator()


    def add_block(self, _data: str):
        self.iterator.seek_to_last()
        last_block = get_last_block()
        last_hash = last_block.Hash
        last_bit = last_block.NextRequiredBits
        new_block = self.new_block(_data, last_hash, last_bit)
        self.db.put(f'bk_{last_bit}'.encode(), new_block.serialize())
        self.db.close()

        return self


    def new_genesis_block(self):
        return self.new_block( "Genesis block", b'Genesis', 18)


    def get_last_block(self):
        self.iterator.seek_to_last()
        return self.deserialize(self.iterator.value())

    

>>>>>>> 5f5a8df1159de558af5cb0842dea9b4c7f9eeff1
    def new_blockchain(self):
        # Null check for DB's content
        self.storage.raw_iterator.seek_to_first()
        if self.storage.raw_iterator.valid():
            self.storage.raw_iterator.seek_to_first()
            print("The chain is already stored")
            return self
        else:
            print("No existing blockchain found. Create Genesis first.")
            genesis = self.new_genesis_block()
<<<<<<< HEAD
            self.storage.put('bk' + genesis.hash, genesis)
            self.storage.put('l', genesis)
=======
            self.db.put(f'bk_0'.encode() + genesis.Hash.encode(), genesis.serialize())
>>>>>>> 5f5a8df1159de558af5cb0842dea9b4c7f9eeff1
            return self

    # Block methods
    def new_genesis_block(self):
        return self.new_block("Genesis block", b'Genesis', 18)

    def add_block(self, _merkleroot: str):
        # Get last block
        last_block = self.get_last_block()

        # Generate Merkle root hash
        self.pool.make_tree()
        merkleroot = self.pool.get_merkle_root()

        new_block = self.new_block(_merkleroot, last_block.hash, last_block.nextbits)
        self.storage.put('bk' + new_block.hash, new_block)
        self.storage.put('l', new_block)

        return self

    def get_last_block(self):
        value = self.storage.get('l')
        return value

    # Transaction methods
    def new_transaction(self, t):
        tx.verify(t)
        self.storage.put(t.id, t)
        self.pool.add_leaf(t.id)

        return self

    # Wallet methods
