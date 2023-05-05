## Part of iq.opengenus.org
from keygenerate import generate_public_key, convert_pub_key ,compress_pub_key
import binascii
import base58
import bitcoin
import hashlib
import hmac
from Crypto.Hash import RIPEMD
# generate bitcoin private key

base58_string = "BTuGbDK2zUMNeAbrZTib3xSFuG6uM8JxtVyvDuoPGNHY"
private_key = binascii.hexlify(base58.b58decode(base58_string)).decode('utf-8')
print("Private Key Base58: ", base58_string)
print()
print("Private Hex Key: ", private_key)
print()
 # return 64-byte key, 2 32-byte representing x,y coordinates of elliptic curve

public_key = generate_public_key(private_key)
print("Generated Public Key: ", public_key.decode())
print()

bit_pub_key = convert_pub_key(public_key)
print("Standard Bitcoin Pub_Key: ", bit_pub_key)
print()

compressed_pub_key = compress_pub_key(public_key)
# compressed_pub_key=compress_pub_key(public_key.to_string('compressed'))

print("Compressed Pub_Key: ", compressed_pub_key.decode()[2:])
public_value = (compressed_pub_key.decode()[2:])
print()

def bin_hash160(public_key):
    hash160 = RIPEMD.new()
    sha256 = hashlib.new('sha256')
    sha256.update(public_key)
    hash160.update(sha256.digest())
    return hash160.digest()

hash160 = bin_hash160(compressed_pub_key)
address = base58.b58encode_check(b'\x00' + hash160).decode('utf-8')
print("address: ", address)
wallet_address = bitcoin.privkey_to_address(private_key)

print("Wallet Address: ",wallet_address)
