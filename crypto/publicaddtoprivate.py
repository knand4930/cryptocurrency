from pycoin.ecdsa.secp256k1 import secp256k1_generator
from pycoin.encoding.b58 import a2b_hashed_base58
from pycoin.encoding.hexbytes import b2h, h2b, b2h_rev
from pycoin.networks.registry import network_for_netcode
network = network_for_netcode("BTC")
import hashlib
import base58
import requests

# Bitcoin address and public key
address = '12SgauqhWDnjVVMnpZwmoAhRBTGnbJcoVy'
# public_key = '04' + '03dffcff271db5b6ba518444d9443e7f2ecf6e3cbe4a8d00783d26556f1b77b736'

url = f"https://blockchain.info/address/{address}?format=json"
response = requests.get(url)
print('\n')
print(response)
print('\n')
# Decode the address to its raw form
address_raw = a2b_hashed_base58(address)
if response.status_code == 200:
    data = response.json()
    print('\n')
    print(data)
    print('\n')
    print("Current Balance: ", data['final_balance'])
    print("Total Sent: ", data['total_sent'])
    print("Total Received: ", data['total_received'])
    pubkey_hash = data['txs'][0]['inputs'][0]['prev_out']['script'][-42:-2]
public_key = pubkey_hash
print("Public Key: ", public_key)    
# Derive the public key hash from the address
public_key_hash = address_raw[1:21]

# Decode the public key to its raw form
public_key_raw = bytes.fromhex(public_key)

# Construct the uncompressed public key by adding the prefix byte '04'
public_key_uncompressed = b'\x04' + public_key_raw

# Calculate the x and y coordinates of the public key
x, y = secp256k1_generator * int.from_bytes(public_key_raw, 'big')

# Combine the x coordinate and a prefix byte to get the compressed public key
if y % 2 == 0:
    prefix = b'\x02'
else:
    prefix = b'\x03'
public_key_compressed = prefix + x.to_bytes(32, 'big')

# Print the uncompressed, compressed, and public key hash
print('Uncompressed Public Key:', b2h(public_key_uncompressed))
print('Compressed Public Key:', b2h(public_key_compressed))
print('Public Key Hash:', b2h(public_key_hash))

# Use pycoin to derive the private key from the public key hash
private_key_int = int.from_bytes(bytes.fromhex(b2h_rev(public_key_hash)), byteorder='big')
print("Private Key Int Value: ",private_key_int)

private_key_bytes = private_key_int.to_bytes((private_key_int.bit_length() + 7) // 8, byteorder='big')
prefix_byte = bytes.fromhex('80')
private_key_bytes = prefix_byte + private_key_bytes

first_hash = hashlib.sha256(private_key_bytes).digest()
second_hash = hashlib.sha256(first_hash).digest()

wif_bytes = private_key_bytes + second_hash[:4]

wif_string = base58.b58encode_check(wif_bytes).decode()
print("Private Key Base58: ", wif_string)
wif_prefix = '5'
wif_string = wif_prefix + wif_string

print("private key WIF: ", wif_string)
















# from pycoin.ecdsa import generator_secp256k1
# from pycoin.serialize import b2h, b2h_rev
# from pycoin.key import Key
# from pycoin.key import BIP32Node
# from binascii import unhexlify
# from pycoin.symbols.btc import create_bitcoinish_network, network
# key = Key.from_wallet_key('mainnet:' + b2h_rev(public_key_hash), network=network)
# key = Key(secret_exponent=int.from_bytes(public_key_hash, byteorder='big'), netcode=network.symbol)
# key = Key.from_bytes_32('mainnet:' + b2h_rev(public_key_hash), network=network.symbol)
# key = network.keys.private('mainnet:' + b2h_rev(public_key_hash))
# key = Key.from_bytes_32(b2h_rev(public_key_hash), netcode=network.symbol)
# key = Key.from_bytes_32('mainnet:'+b2h_rev(public_key_hash), network.symbol)
# key = Key.from_bytes_32(b2h_rev(public_key_hash), netcode=network.symbol)
# key = Key.from_bytes_32(b2h_rev(public_key_hash))
# private_key_int = int.from_bytes(bytes.fromhex(b2h_rev(public_key_hash)), byteorder='big')
# key = Key(secret_exponent=private_key_int)
# key = Key.from_secret_exponent(private_key_int)
# key = Key.from_secret_exponent(int.from_bytes(private_key_int, byteorder='big'), network=network)
# key = Key(secret_exponent=private_key_int)
# key = Key.from_bytes_32(bytes.fromhex(b2h_rev(public_key_hash))), network.symbol
# print(Key.Key.secret_exponent)
# key = Key.Key(secret_exponent=private_key_int, netcode=network)
# key._network = network
# key = Key(netcode=network.symbol, secret_exponent=key.secret_exponent())
# Print the private key in WIF format
# print('Private Key:', key.wif())