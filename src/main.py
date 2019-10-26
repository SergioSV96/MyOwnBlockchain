from src.blockchain import Blockchain

blockchain = Blockchain()
blockchain.add_block("Second!")
blockchain.add_block("Third!")

print(blockchain)
