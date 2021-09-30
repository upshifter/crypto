# class AbstractContract is a template for any 
# EVM based contract and initializing with contract address and ABI.
# Address and ABI can be found on blockchain explorer sush as https://etherscan.io
#

from abc import ABC
from web3 import Web3


# Binance Smart Chain http node provider
BSC = 'https://bsc-dataseed1.binance.org:443'


class AbstractContract(ABC):
    
    provider = None
    
    def __init__(self, address: str, ABI: str):
        
        if self.provider is not None:
            w3 = Web3(Web3.HTTPProvider(self.provider))
        else:
            raise ProviderInitException
        
        try:
            self.contract = w3.eth.contract(address, abi=ABI)
        except Exception as e:
            print(f'{e} in contract {address}')
    
    @property
    def address(self):
        return self.contract.address
    
    @property
    def abi(self):
        return self.contract.abi

    def get_functions_list(self) -> list:
        return self.contract.all_functions()



class BSCContract(AbstractContract):
    provider = BSC

class BEP20Token(object):

    def __init__(self, object):
        self.functions = object.contract.functions
        

    def get_balance(self, wallet_address):
        raw_balance = self.functions.balanceOf(wallet_address).call()
        DECIMALS = 10 ** self.functions.decimals().call()
        balance = raw_balance // DECIMALS
        print('The balance of token {} on wallet {} equal to:'.format(self.functions.symbol().call(), wallet_address),
              Web3.fromWei(balance, 'ether'))

