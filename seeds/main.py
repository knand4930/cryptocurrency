import mnemonic
from bitcoin import *
import base58
from seedsvalue import encode_base58, wif_to_private_key
from keygenerate import generate_public_key, convert_pub_key ,compress_pub_key
import binascii
import base58
import bitcoin
import requests
import json

# Initial wordlists
fours = []
fives = []
sixes = []
sevens = []

# Fill above lists with corresponding word lengths from wordlist
with open('wordlist.txt') as wordlist:
    for line in wordlist:
        if len(line) == 4:
            fours.append(line.strip())
        elif len(line) == 5:
            fives.append(line.strip())
        elif len(line) == 6:
            sixes.append(line.strip())
        elif len(line) == 7:
            sevens.append(line.strip())

# Create new lists and fill with number of items in fours
fivesLess = []
sixesLess = []
sevensLess = []

fivesCounter = 0
while fivesCounter < len(fours):
    randFive = random.choice(fives)
    if randFive not in fivesLess:
        fivesLess.append(randFive)
        fivesCounter += 1

sixesCounter = 0
while sixesCounter < len(fours):
    randSix = random.choice(sixes)
    if randSix not in sixesLess:
        sixesLess.append(randSix)
        sixesCounter += 1

sevensCounter = 0
while sevensCounter < len(fours):
    randSeven = random.choice(sevens)
    if randSeven not in sevensLess:
        sevensLess.append(randSeven)
        sevensCounter += 1

choices = [fours, fivesLess, sixesLess, sevensLess]

# Generate n number of seeds and print
seedCounter = 0
while seedCounter < 1:
    seed = []
    while len(seed) < 12:
        wordLengthChoice = random.choice(choices)
        wordChoice = random.choice(wordLengthChoice)
        seed.append(wordChoice)
    # seedCounter += 2


    value = ' '.join(seed)
    string = repr(value)

    my_set = string

    with open('data.txt', 'a') as file:
        file.write('\n' + str(my_set))

    # with open('data.txt', 'r') as unique:
    #     lines = unique.readlines()
    #     print("Line Of Code Done: ",lines)
    with open('data.txt') as lines:
        seeds = [line.strip() for line in lines]
    for seed in seeds:
        print("value Printed ",seed)
        # Set the BIP39 seed phrase
        seed_phrase = seed
        
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
        print("Private Key: ", private_key_base58)
        print('\n')

        # generate bitcoin private key
        base58_string = private_key_base58
        private_key = binascii.hexlify(base58.b58decode(base58_string)).decode('utf-8')
        print("private Hex Code: ", private_key)
        print()
        # return 64-byte key, 2 32-byte representing x,y coordinates of elliptic curve
        public_key = generate_public_key(private_key)
        print("Generated Public Key: ", public_key.decode())
        print()
        bit_pub_key = convert_pub_key(public_key)
        print("Standard Bitcoin Pub_Key: ", bit_pub_key)
        print()
        compressed_pub_key = compress_pub_key(public_key)
        print("Compressed Pub_Key: ", compressed_pub_key.decode()[2:])
        public_value = (compressed_pub_key.decode()[2:])
        print()
        wallet_address = bitcoin.privkey_to_address(private_key)
        print("Wallet Address: ",wallet_address)

        url = f"https://blockchain.info/address/{wallet_address}?format=json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print("Show the Total Balance: ", data['final_balance'])
            print("Sent the Total Balance: ", data['total_sent'])
            print("Received the Total Balance: ", data['total_received'])

            if data['final_balance'] != 0:
                values = {
                    "seed": seed_phrase,
                    "private_key": private_key,
                    "private_key_base58": private_key_base58,
                    "Wallet_address": wallet_address,
                    "compressed_pub_key": compressed_pub_key,
                    "pricing": data['final_balance'],
                    "sent_total_balance": data['total_sent'],
                    "received_total_balance": data['total_received'],

                }
                with open('payment.txt', 'a') as file:
                    file.write('\n' + str(values))