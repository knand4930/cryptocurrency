import requests

def get_public_key(address):
    url = f"https://blockchain.info/address/{address}?format=json"
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        data = response.json()

        with open('apidata.txt', 'a') as file:
            file.write('\n' + str(data))
        # print(data)
        # return data["pubkey"]

        return data
    else:
        raise Exception("Unable to get public key from API")

# Example usage
address = "1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2"
public_key = get_public_key(address)
# print(public_key)
print(public_key['final_balance'])
print(public_key['total_sent'])
print(public_key['total_received'])