image.gif
# import needed libraries
import pqcrypto.sign.falcon_512 as falcon512
import pqcrypto.sign.falcon_1024 as falcon1024

import pqcrypto.sign.dilithium2 as dilithium2
import pqcrypto.sign.dilithium3 as dilithium3
import pqcrypto.sign.dilithium4 as dilithium5

import pqcrypto.sign.rainbowIa_classic as rainbowIa_classic
import pqcrypto.sign.rainbowIIIc_classic as rainbowIIIc_classic
import pqcrypto.sign.rainbowVc_classic as rainbowVc_classic

import pqcrypto.sign.rainbowIa_cyclic as rainbowIa_cyclic
import pqcrypto.sign.rainbowIIIc_cyclic as rainbowIIIc_cyclic
import pqcrypto.sign.rainbowVc_cyclic as rainbowVc_cyclic

import pqcrypto.sign.rainbowIa_cyclic_compressed as rainbowIa_cyclic_compressed
import pqcrypto.sign.rainbowIIIc_cyclic_compressed as rainbowIIIc_cyclic_compressed
import pqcrypto.sign.rainbowVc_cyclic_compressed as rainbowVc_cyclic_compressed

import ecdsa as ecdsa
import datetime
import hashlib


class Transaction:

    def __init__(self, senderAddress, receiverAddress, transactionAmount):
        self.senderAddress = senderAddress
        self.receiverAddress = receiverAddress
        self.transactionAmount = transactionAmount
        self.timestamp = datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")

    def hash_calculation(self):
        hash_string = (str(self.senderAddress) + str(self.receiverAddress) +
                       str(self.transactionAmount) + self.timestamp).encode('utf-8')
        hash = hashlib.sha3_512(hash_string).digest()
        return hash.hex()

    def sign_transaction(self, pk, sk):
        if pk != self.senderAddress:
            raise Exception('Transactions cannot be signed for other wallets.')

        tsx_hash = bytes.fromhex(self.hash_calculation())
        self.signature = falcon512.sign(sk, tsx_hash)
        #print('sig', self.signature)

    def is_valid(self):
        if self.senderAddress == None:
            return True

        if not self.signature or len(str(self.signature)) == 0:
            raise Exception(
                'No signature found withing this transaction object.')

        pk = self.senderAddress
        print('Is Valid?', pk.verify(bytes.fromhex(
            self.hash_calculation()), self.signature))
        return falcon512.verify(self.signature, bytes.fromhex(self.hash_calculation()))


class Block:

    def __init__(self, timestamp, transactions, previousHash=''):
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.transactions = transactions
        self.nonce = 0
        self.hash = self.hash_calculation()

    def hash_calculation(self):
        str_transactions = ''.join([str(tx) for tx in self.transactions])
        hash_string = str(self.previousHash) + self.timestamp + \
            str_transactions + str(self.nonce)
        hash_string = hash_string.encode('utf-8')
        hash = hashlib.sha3_512(hash_string).digest()
        #print('Digest Size:', hash.digest_size)
        return hash.hex()

    def mine_block(self, difficultyOfMining):
        diffArr = "".join(["0"*difficultyOfMining])
        dotInd = 0
        while self.hash[0: difficultyOfMining] != diffArr:
            self.nonce += 1
            self.hash = self.hash_calculation()
            #print('Mining' + '.'*dotInd)
            print('Mining, current hash:', self.hash)
            dotInd += 1

        print('Block mined with hash:', self.hash)

    def contains_valid_transactions(self):
        for transaction in self.transactions:
            if not transaction.is_valid():
                return False
        return True


class Blockchain:

    def __init__(self):
        self.chainArr = [self.create_initial_block()]
        self.difficultyOfMining = 1
        self.pendingTransactions = []
        self.miningRewardAmount = 100

    def create_initial_block(self):
        return Block(datetime.datetime.strptime('01-01-2021, 00:00:00', '%d-%m-%Y, %H:%M:%S').strftime('%d-%m-%Y, %H:%M:%S'), [], '0')

    def get_last_block_in_chain(self):
        return self.chainArr[len(self.chainArr) - 1]

    def mine_pending_transactions(self, miningRewardAddress, mine=False):
        if mine:
            rewardTransaction = Transaction(
                None, miningRewardAddress, self.miningRewardAmount)
            self.pendingTransactions.append(rewardTransaction)

        newBlock = Block(datetime.datetime.now().strftime(
            "%d-%m-%Y, %H:%M:%S"), self.pendingTransactions, self.get_last_block_in_chain().hash)
        newBlock.mine_block(self.difficultyOfMining)

        self.chainArr.append(newBlock)
        self.pendingTransactions = []

    def append_transaction(self, transaction):

        if not transaction.senderAddress or not transaction.receiverAddress:
            raise Exception(
                'Transaction doesn\'t contain sender and receiver addresses.')

        if not transaction.is_valid():
            raise Exception('Transaction is not valid.')

        if transaction.transactionAmount <= 0:
            raise Exception(
                'Transaction amount cannot be negative or zero, it must be greater than 0.')

        if self.get_balance(transaction.senderAddress) < transaction.transactionAmount:
            raise Exception('Not enough balance in sender address.')

        self.pendingTransactions.append(transaction)
        print('Transaction is added:', transaction)

    def get_balance(self, address):
        balance = 0

        for block in self.chainArr:
            for transaction in block.transactions:
                if transaction.senderAddress == address:
                    #print('h', balance)
                    balance -= transaction.transactionAmount
                    #print('he', balance)

                if transaction.receiverAddress == address:
                    #print('e', balance)
                    balance += transaction.transactionAmount
                    #print('ef', balance)

        print('Balance of address is: {} units.'.format(balance))
        return balance

    def get_transactions_of_wallet(self, address):
        transactions = []

        for block in self.chainArr:
            for transaction in block.transactions:
                if transaction.senderAddress == address or transaction.receiverAddress == address:
                    transactions.append(transaction)

        print('There is {} transactions for the given address'.format(
            len(transactions)))
        return transactions

    def is_chain_valid(self):
        actualInitialBlock = (self.create_initial_block())

        if actualInitialBlock.hash != self.chainArr[0].hash:
            return False

        for i in range(1, len(self.chainArr)):
            currBlock = self.chainArr[i]
            prevBlock = self.chainArr[i - 1]

            if prevBlock.hash != currBlock.previousHash:
                return False

            if not currBlock.contains_valid_transactions():
                return False

            if currBlock.hash != currBlock.hash_calculation():
                return False

        return True

pk, sk = falcon512.generate_keypair()

walletAddress = pk

bchain = Blockchain()

bchain.mine_pending_transactions(walletAddress, True)

tx1 = Transaction(walletAddress, 'addr2', 50)
tx1.sign_transaction(walletAddress, sk)
bchain.append_transaction(tx1)

bchain.mine_pending_transactions(walletAddress)

tx2 = Transaction(walletAddress, 'addr2', 20)
tx2.sign_transaction(walletAddress, sk)
bchain.append_transaction(tx2)

bchain.mine_pending_transactions(walletAddress)
print('balance', bchain.get_balance(walletAddress))
print('balance of sec', bchain.get_balance('addr2'))

print('Is the blockchain Valid?', bchain.is_chain_valid())