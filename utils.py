from solcx import compile_standard, install_solc
import json
from web3 import Web3
from config import w3, ACCOUNT

install_solc("0.8.0")

def compile_and_deploy(sol_file, contract_name):
    with open(sol_file, "r") as f:
        source_code = f.read()

    compiled = compile_standard({
        "language": "Solidity",
        "sources": {sol_file: {"content": source_code}},
        "settings": {"outputSelection": {"*": {"*": ["abi", "evm.bytecode"]}}},
    }, solc_version="0.8.0")

    abi = compiled["contracts"][sol_file][contract_name]["abi"]
    bytecode = compiled["contracts"][sol_file][contract_name]["evm"]["bytecode"]["object"]

    contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    tx = contract.constructor().buildTransaction({
        "from": ACCOUNT.address,
        "nonce": w3.eth.getTransactionCount(ACCOUNT.address),
        "gas": 3000000
    })
    signed = ACCOUNT.sign_transaction(tx)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    print("✅ Contract deployed to:", tx_receipt.contractAddress)

    with open("Donation_abi.json", "w") as f:
        json.dump(abi, f, indent=2)

def send_transaction(tx):
    signed_tx = ACCOUNT.sign_transaction(tx)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    w3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_hash
