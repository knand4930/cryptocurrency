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
import blockcypher

api= {
    "api":"112d0c9bf2d64350aabca3a553e20333",
    "api1": "f294dc9d7ef24c169b3dd40ae56ef06d",
}

fours = []
fives = []
sixes = []
sevens = []

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

seedCounter = 0
while seedCounter < 1:
    seed = []
    while len(seed) < 12:
        wordLengthChoice = random.choice(choices)
        wordChoice = random.choice(wordLengthChoice)
        seed.append(wordChoice)


    value = ' '.join(seed)
    string = repr(value)

    my_set = string

    print("My Seeds Printed ",my_set)
    seed_phrase = my_set
    
    seed = mnemonic.Mnemonic.to_seed(seed_phrase)

    master_key = bip32_master_key(seed)

    account_key = bip32_ckd(master_key, 0) 

    private_key_wif = encode_privkey(bip32_extract_key(account_key), 'wif')

    private_key_base58 = encode_privkey(bip32_extract_key(account_key), 'hex')
    private_key_base58 = encode_base58(bytes.fromhex("80" + private_key_base58))
    wif_private_key = private_key_base58


    private_key_base58 = wif_to_private_key(wif_private_key)

    print("Private Key: ", private_key_base58)
    print('\n')

    # generate bitcoin private key
    base58_string = private_key_base58
    private_key = binascii.hexlify(base58.b58decode(base58_string)).decode('utf-8')
    print("private Hex Code: ", private_key)
    print()

    # return 64-byte key, 2 32-byte representing x,y coordinates of elliptic curve
    public_key = generate_public_key(private_key)
    # print("Generated Public Key: ", public_key.decode())
    print()

    bit_pub_key = convert_pub_key(public_key)
    # print("Standard Bitcoin Pub_Key: ", bit_pub_key)
    print()

    compressed_pub_key = compress_pub_key(public_key)
    # print("Compressed Pub_Key: ", compressed_pub_key.decode()[2:])
    public_value = (compressed_pub_key.decode()[2:])
    print()

    wallet_address = bitcoin.privkey_to_address(private_key)
    print("Wallet Address: ",wallet_address)

    print()
    url = f"https://blockchain.info/address/{wallet_address}?format=json"
    
    print(url)
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
    # value = blockcypher.get_address_full(wallet_address, api_key='0f8feaca0fe74922b11aa8ce42054f31')

    # elif value:
    #     print("Total Amount: ", value['final_balance'])
    #     print("Total Received: ", value['total_received'])
    #     print("Total Send: ", value['total_sent'])

    #     if value['final_balance'] != 0:
    #         values = {
    #             "seed": seed_phrase,
    #             "private_key": private_key,
    #             "private_key_base58": private_key_base58,
    #             "Wallet_address": wallet_address,
    #             "compressed_pub_key": compressed_pub_key,
    #             "pricing": value['final_balance'],
    #             "sent_total_balance": value['total_sent'],
    #             "received_total_balance": value['total_received'],

    #         }

    #         with open('payment.txt', 'a') as file:
    #             file.write('\n' + str(values))