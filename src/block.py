import hashlib
import datetime as date


class Block:
    def __init__(self, index, previous_hash, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = date.datetime.now()
        self.data = data
        self.hash = hashlib.sha256((str(index) + str(previous_hash) + str(data)).encode('utf-8')).hexdigest()

    def __str__(self):
        return \
            f"Index: {self.index} \n" \
                f"Previous Hash: {self.previous_hash} \n" \
                f"Timestamp: {self.timestamp} \n" \
                f"Data: {self.data} \n" \
                f"Hash: {self.hash}"


class GenesisBlock(Block):
    def __init__(self):
        super().__init__(0, 0, "Genesis Block")
