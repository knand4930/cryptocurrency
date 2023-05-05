import blockcypher

# The private key for the address
private_key = '78d358fa5ed57bbccf2701fe08f4e37210cfc2b7c8baaff4112f4cc563762eaf'

# The address you want to send funds from
address = '1H2MXWiSniAgg7ykdXEzPHL6oTH1ic4kP'

# The destination address and amount
dest_address = '3DtKExDtwnD3d5f6vq7ERSzqt1idx54b4V'
amount = 10  # 0.01 BTC in Satoshis

# Construct the transaction
inputs = [{'address': address}]
outputs = [{'address': dest_address, 'value': amount}]
unsigned_tx = blockcypher.create_unsigned_tx(inputs=inputs, outputs=outputs, coin_symbol='btc-testnet')

# Sign the transaction
signed_tx = blockcypher.make_tx_signer('btc-testnet')(unsigned_tx, private_key=private_key)

# Broadcast the transaction
result = blockcypher.broadcast_signed_transaction(signed_tx, coin_symbol='btc-testnet')
print(f'Transaction signed and broadcasted with ID {result["tx"]["hash"]}')
