from config import w3, ACCOUNT, CONTRACT
from utils import send_transaction

tx = CONTRACT.functions.donate().buildTransaction({
    "from": ACCOUNT.address,
    "value": w3.toWei(0.01, "ether"),
    "nonce": w3.eth.getTransactionCount(ACCOUNT.address),
    "gas": 100000
})
tx_hash = send_transaction(tx)
print("✅ Donated:", w3.toHex(tx_hash))
