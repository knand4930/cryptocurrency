import json
from web3 import Web3

# Connect to the Ethereum JSON-RPC API endpoint
web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/e34d12f06fcf48ae909c7eb2477bc6d5'))

print(web3)
# Public address to retrieve private key for
address = 'bc1qazcm763858nkj2dj986etajv6wquslv8uxwczt'
print(address)
# Unlock the account with a password and get the private key
private_key = web3.eth.account.decrypt(json.loads(
    web3.eth.personal.unlockAccount(address, 'Nand#@!123', duration=60)
), 'YOUR_PASSWORD')

print('Private key:', private_key.hex())


