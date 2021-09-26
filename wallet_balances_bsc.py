from contract import *
import json


#Load ABI from json
with open('ABI.json') as abi_json:
    ABI = json.load(abi_json)
    abi_json.close()

wallet_address = input('wallet=')
wallet_address = Web3.toChecksumAddress(wallet_address)
token_contract_address = input('token=')
token_contract_address = Web3.toChecksumAddress(token_contract_address)

if __name__ == '__main__':
    contract = BSCContract(token_contract_address, ABI)
    contract.get_balance(wallet_address)


