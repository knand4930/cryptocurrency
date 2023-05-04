import requests

# Set the Bitcoin address you want to query
address = "1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2"

# Make a GET request to the Blockchain.info API
response = requests.get(f"https://blockchain.info/rawaddr/{address}")

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the response content as JSON data
    data = response.json()
    
    # Get the public key from the first transaction input
    pubkey_hash = data['txs'][0]['inputs'][0]['prev_out']['script'][-42:-2]

    
    # Print the public key
    print(f"Public key: {pubkey_hash}")
else:
    print(f"Error: {response.status_code} - {response.reason}")
