import os
from dotenv import load_dotenv
from web3 import Web3

def printContractDetails(transaction):
    print("Blockhash:", (transaction.blockHash).hex())
    print("Block Number:", transaction.blockNumber)
    # print("From:", transaction.from)
    print("Gas Used:", transaction.gas)
    print("Effective Gas Price:", transaction.gasPrice)
    print("Transaction Hash:", (transaction.hash).hex())
    # print("Input:", transaction.input)
    print("Max Fee Per Gas:", transaction.maxFeePerGas)
    print("Max Priority Fee Per Gas:", transaction.maxPriorityFeePerGas)
    print("Nonce:", transaction.nonce)
    print("To:", transaction.to)
    print("Transaction Index:", transaction.transactionIndex)
    print("Type:", transaction.type)


def main():
    load_dotenv()

    API_URL = os.getenv('API_URL')
    WALLET = os.getenv('WALLET')
    contract_tranaction = '0xbe5e162ba3af81913f52711724e283f98f40fc7a04ecfbb20bf4d246fb847e22'
    # contract_address = "0x01Bd73c77ca59512aEfF682cfd81c827Fab549bB"

    web3 = Web3(Web3.HTTPProvider(API_URL))
    transaction = web3.eth.get_transaction(contract_tranaction)
    
    # contract = web3.eth.contract(contract_address)
    printContractDetails(transaction)
 
    exit(0)

if __name__ == "__main__":
    main()