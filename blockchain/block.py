import hashlib
import base64

class Block:
    def __init__(self, previous, transaction):
        self.transactions = transaction
        self.previous = previous
        string_to_hash = "".join(transaction) + previous
        self.block_hash = base64.bs64encode(string_to_hash.encrypt()).hexdigest()

