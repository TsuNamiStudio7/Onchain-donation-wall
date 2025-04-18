from web3 import Web3
from eth_account import Account
import json

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))  # lub Infura
PRIVATE_KEY = "your-private-key"
ACCOUNT = Account.from_key(PRIVATE_KEY)

with open("Donation_abi.json") as f:
    ABI = json.load(f)

CONTRACT_ADDRESS = "0xYourDeployedContractAddress"
CONTRACT = w3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)
