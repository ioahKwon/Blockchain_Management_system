from datetime import datetime
from hashlib import sha256

class Block_comp:
    def __init__(self, transactions, uid_comp, previous_hash, nonce = 0):
        self.timestamp = datetime.now()
        self.transactions = transactions
        self.uid = uid_comp
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.generate_hash()

    def print_block(self):
        # prints block contents
        print("timestamp:", self.timestamp)
        print("transactions:", self.transactions)
        print("material index :", self.uid)
        print("current hash:", self.generate_hash())

    def generate_hash(self):
        # hash the blocks contents
        return sha256(str(self.timestamp).encode() + str(self.transactions).encode() +
                      str(self.previous_hash).encode() + str(self.uid).encode()
                      + str(self.nonce).encode()).hexdigest()
