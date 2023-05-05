import hashlib
import hmac
import os

# BIP39 word list
word_list = open('data.txt').read().splitlines()

# print(word_list)


def validate_seed_phrase(seed_phrase):
    # Check if seed phrase is a string
    if not isinstance(seed_phrase, str):
        return False

    # Split seed phrase into words
    words = seed_phrase.split()
    print(words, "======================================================================")
    # Check if seed phrase contains exactly 12 or 24 words
    if len(words) not in [12, 24]:
        return False

    # Check if all words are part of the BIP39 word list
    if any(word not in word_list for word in words):
        return False

    # Calculate seed phrase checksum
    entropy = b''
    for word in words:
        index = word_list.index(word)
        entropy += os.urandom(2) + index.to_bytes(1, 'big')
    checksum = hashlib.sha256(entropy).digest()[0] >> 3
    print(checksum, "================================================")
    # Calculate expected checksum
    expected_checksum = hmac.digest(
        key=b"mnemonic",
        msg=bytes(seed_phrase, 'utf-8'),
        digest=hashlib.sha256
    )[0] >> 3
    print(expected_checksum, "========================================================================")
    # Compare checksums
    if checksum != expected_checksum:
        return False

    return True
