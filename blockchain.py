# from __future__ import absolute_import
# # from blockchain.blockexplorer import get_address
# from chinilla.blockchain.key import Key

# address = '1H2MXWiSniAgg7ykdXEzPHL6oTH1ic4kP'
# txs = key.to_hex(address)
# print(txs)

import blockcypher

address = "12SgauqhWDnjVVMnpZwmoAhRBTGnbJcoVy"
details = blockcypher.get_address_details(address)
with open('blockcypher.json', 'a') as file:
    file.write('\n' + str(details))
# print(details)
value = blockcypher.get_address_full(address, api_key='0f8feaca0fe74922b11aa8ce42054f31')
print("Total Amount: ", value['final_balance'])
print("Total Received: ", value['total_received'])
print("Total Send: ", value['total_sent'])
print('\n')
print(value)
print('\n')

for tx in value['txs']:
    print("Hash Values: ", tx['hash'])
    print('\n')

    print("Address: ", tx['addresses'])
    print('\n')

for txt in value['txs']:
    for i in tx['inputs']:
        print("Private Key Hex: ", i['prev_hash'])
        print('\n')

