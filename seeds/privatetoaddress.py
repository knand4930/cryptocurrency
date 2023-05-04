## Part of iq.opengenus.org
import codecs
import ecdsa
import secrets
import binascii
import base58
import bitcoin

# generate bitcoin private key
def generate_private_key():
    bits = secrets.randbits(256)
    bits_hex = hex(bits)
    return bits_hex[2:]

base58_string = "5FYjigSbg5p8a68v1uMG3yUDyMfkayjqYH7YKh6twq9h"
private_key = binascii.hexlify(base58.b58decode(base58_string)).decode('utf-8')

print("Private Hex Key: ", private_key)
print()
 # return 64-byte key, 2 32-byte representing x,y coordinates of elliptic curve
def generate_public_key(private_key):
    priv_key_bytes = codecs.decode(private_key, 'hex') # convert string into byte array
    key = ecdsa.SigningKey.from_string(priv_key_bytes, curve=ecdsa.SECP256k1).verifying_key
    key_bytes = key.to_string()
    public_key = codecs.encode(key_bytes, 'hex')
    return public_key 


public_key = generate_public_key(private_key)
print("Generated Public Key: ", public_key.decode())
print()

def convert_pub_key(public_key):
    bit_public_key = b'0x04' + public_key
    return bit_public_key.decode()[2:]

bit_pub_key = convert_pub_key(public_key)
print("Standard Bitcoin Pub_Key: ", bit_pub_key)
print()

# compress public key
def compress_pub_key(public_key):
    mid = int(len(public_key) / 2)
    x = public_key[:mid]
    if(int(public_key[-1:]) % 2 == 0):
        x = b'0x02' + x
    else:
        x = b'0x03' + x
    return x

compressed_pub_key = compress_pub_key(public_key)

print("Compressed Pub_Key: ", compressed_pub_key.decode()[2:])
public_value = (compressed_pub_key.decode()[2:])
print()
wallet_address = bitcoin.pubkey_to_address(public_value)

print("Wallet Address: ",wallet_address)
