from config import CONTRACT

donors = CONTRACT.functions.getDonors().call()
print("📜 Donors:")
for i, donor in enumerate(donors):
    print(f"{i+1}. {donor[0]} - {int(donor[1]) / 10**18:.5f} ETH")
