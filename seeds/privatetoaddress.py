## Part of iq.opengenus.org
from keygenerate import generate_private_key, generate_public_key, convert_pub_key
import binascii
import base58
import bitcoin

# generate bitcoin private key

base58_string = "GgyopU7SoRK5whsas9nj6XhDXafKrdMayohg9esg4w5C"
private_key = binascii.hexlify(base58.b58decode(base58_string)).decode('utf-8')

print("Private Hex Key: ", private_key)
print()
 # return 64-byte key, 2 32-byte representing x,y coordinates of elliptic curve


public_key = generate_public_key(private_key)
print("Generated Public Key: ", public_key.decode())
print()



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
