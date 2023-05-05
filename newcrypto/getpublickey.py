# import bitcoin
# import hashlib
#
# # Define the Bitcoin address
# address = '1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2'
#
# # Convert the address to a public key
# public_key = bitcoin.add_privkeys(address, 'p2')
#
# # Convert the public key to an address
# hash160 = hashlib.new('ripemd160', hashlib.sha256(public_key).digest()).digest()
# address = bitcoin.bin_to_b58check(hash160, magicbyte=0)
# print(address)


# import bitcoin
# import hashlib
#
# # Define the Bitcoin address and network (mainnet or testnet)
# address = '34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo'
# network = 'mainnet' # or 'testnet'
#
# # Get the private key from the address
# pubkey = bitcoin.pubkey_to_address(address, magicbyte={'mainnet': 0x00, 'testnet': 0x6f}[network])
# privkey = bitcoin.encode_privkey(bitcoin.get_privkey_format(pubkey), 'wif', magicbyte={'mainnet': 0x80, 'testnet': 0xef}[network])
#
# # Print the private key
# print(privkey)
#

import bitcoin
import hashlib

# Define the public key
public_key_hex = '12SgauqhWDnjVVMnpZwmoAhRBTGnbJcoVy'

# Convert the public key to a Bitcoin address
hash160 = hashlib.new('ripemd160', hashlib.sha256(bytes.fromhex(public_key_hex)).digest()).digest()
address = bitcoin.bin_to_b58check(hash160, magicbyte=0)
print(address)
