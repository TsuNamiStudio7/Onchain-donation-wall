from config import CONTRACT

donors = CONTRACT.functions.getDonors().call()
sorted_donors = sorted(donors, key=lambda d: d[1], reverse=True)

print("🏆 Top Donors:")
for i, donor in enumerate(sorted_donors):
    eth = int(donor[1]) / 10**18
    print(f"{i+1}. {donor[0]} - {eth:.4f} ETH")
