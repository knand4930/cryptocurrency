import mnemonic
from bitcoin import *
import base58
from seedsvalue import encode_base58, wif_to_private_key


# Set the BIP39 seed phrase
seed_phrase = 'sniff you best genius figure oblige cook boat faint crouch race lady'

# Generate the BIP39 seed from the seed phrase
seed = mnemonic.Mnemonic.to_seed(seed_phrase)

# Derive the master private key from the seed using BIP32
master_key = bip32_master_key(seed)

# Derive the private key for a specific account using BIP32
account_key = bip32_ckd(master_key, 0) # Replace 0 with the account index

# Convert the private key to WIF format
private_key_wif = encode_privkey(bip32_extract_key(account_key), 'wif')

# Convert the private key to Base58Check format
private_key_base58 = encode_privkey(bip32_extract_key(account_key), 'hex')
private_key_base58 = encode_base58(bytes.fromhex("80" + private_key_base58))
wif_private_key = private_key_base58
private_key_base58 = wif_to_private_key(wif_private_key)
# print(private_key_base58)

# Print the private key in Base58Check format
print(private_key_base58)