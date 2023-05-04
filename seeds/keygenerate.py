import codecs
import ecdsa
import secrets


def generate_private_key():
    bits = secrets.randbits(256)
    bits_hex = hex(bits)
    return bits_hex[2:]

def generate_public_key(private_key):
    priv_key_bytes = codecs.decode(private_key, 'hex') # convert string into byte array
    key = ecdsa.SigningKey.from_string(priv_key_bytes, curve=ecdsa.SECP256k1).verifying_key
    key_bytes = key.to_string()
    public_key = codecs.encode(key_bytes, 'hex')
    return public_key 

def convert_pub_key(public_key):
    bit_public_key = b'0x04' + public_key
    return bit_public_key.decode()[2:]