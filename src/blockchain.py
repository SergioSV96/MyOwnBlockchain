from src.block import Block, GenesisBlock
from typing import List


class Blockchain:
    def __init__(self):
        self.blockchain: List[Block] = []
        self.blockchain.append(GenesisBlock())

    def add_block(self, data):
        self.blockchain.append(Block(len(self.blockchain), self.blockchain[-1].hash, data))

    def __str__(self):
        text = ""
        for block in self.blockchain:
            text += str(block)
            text += "\n---------------------------\n"
        return text


    """
    def is_verified_block(self, block: Block):
        if self.blockchain[block.index - 1].hash != block.previous_hash:
            return False
        elif block.hash != hashlib.sha256(
                (str(block.index) + str(self.blockchain[block.index - 1].hash) + str(block.data))
                .encode('utf-8')).hexdigest():
            return False
        else:
            return True
    """
