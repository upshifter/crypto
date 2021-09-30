from contract import *
import json


#Load ABI from json
with open('ABI.json') as abi_json:
    ABI = json.load(abi_json)
    abi_json.close()

# wallet_address = input('wallet=')
wallet_address = '0xc36E54d8313d76168c823BF44cB72e46020DbF73'
wallet_address = Web3.toChecksumAddress(wallet_address)
# token_contract_address = input('token=')
token_contract_address = '0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d'
token_contract_address = Web3.toChecksumAddress(token_contract_address)

if __name__ == '__main__':
    contract = BSCContract(token_contract_address, ABI)
    token = BEP20Token(contract)
    token.get_balance(wallet_address)

    