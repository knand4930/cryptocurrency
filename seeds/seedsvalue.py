import hashlib
import base58


def encode_base58(input_bytes):
    leading_zeros = 0
    for b in input_bytes:
        if b == 0:
            leading_zeros += 1
        else:
            break
    checksum = hashlib.sha256(hashlib.sha256(input_bytes).digest()).digest()[:4]
    return '1' * leading_zeros + base58.b58encode(input_bytes + checksum).decode()

def wif_to_private_key(wif):
    # Base58 decode the WIF private key
    decoded_wif = base58.b58decode(wif)

    # Drop the version byte and the checksum
    private_key = decoded_wif[1:-4]

    # Return the private key as a base58 encoded string
    return base58.b58encode(private_key).decode('utf-8')
