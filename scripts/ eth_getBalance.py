import os
from dotenv import load_dotenv
from web3 import Web3

def main():
    load_dotenv()

    API_URL = os.getenv('API_URL')
    WALLET = os.getenv('WALLET')

    w3 = Web3(Web3.HTTPProvider(API_URL))
    balance = w3.eth.get_balance(WALLET)

    # w3 = Web3(HTTPProvider(url))
    # print(w3.__dict__)
    print(balance)

    exit(0)

if __name__ == "__main__":
    main()