from web3.auto import w3
from eth_account import Account
Account.enable_unaudited_hdwallet_features()

seed_phrase = "try shadow song south pencil margin pool law theory pencil pet burger"

# Create an account object from the seed phrase
account = Account.from_mnemonic(seed_phrase)
print(account.address)
# Check if the account address matches with your MetaMask account address
my_address = w3.eth.accounts[0]

if my_address.lower() == account.address.lower():
    print("Seed phrase is correct!")
else:
    print("Seed phrase is incorrect.")