from web3 import Web3

# Set up the Infura API endpoint URL
infura_url = "https://mainnet.infura.io/v3/e34d12f06fcf48ae909c7eb2477bc6d5"

# Set up the public address you want to query
address = "1H2MXWiSniAgg7ykdXEzPHL6oTH1ic4kP"

# Create a Web3 instance connected to the Infura API endpoint
web3 = Web3(Web3.HTTPProvider(infura_url))

# Get the balance of the specified address
balance = web3.eth.get_balance(address)

# Print the address balance
print(f"Address balance: {web3.fromWei(balance, 'ether')} ether")
