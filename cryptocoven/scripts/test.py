from brownie import accounts, network, config
from scripts.tools import *
import time

D18= 10**18
ZERO= '0x0000000000000000000000000000000000000000'
active_network= network.show_active()

class deployer:
    _instance = None
    cns=None
    asc=None
    iio_token0=None
    iio_token1=None
    token1= None
    token0=None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)

            # Now deploy
            console.print("_______________________部署合约_________________________", style="bold white on blue", justify="center")

            admin=accounts[0]
            creator=accounts[1]
            consumer=accounts[2]

        return class_._instance

    def __init__(self):
        pass

    def getTokens(self):
        return self.asc, self.cns, self.token0, self.token1, self.iio_token0, self.iio_token1


def main():
    active_network= network.show_active()
    print("Current Network:"+ active_network)

    try:
        if active_network == 'development' :
            admin=accounts[0]
            creator=accounts[1]
            consumer=accounts[2]

        if active_network== 'mainnet-fork':
            admin=accounts[0]
            creator=accounts[1]
            consumer=accounts[2]

            balance_alert(admin, "admin")
            balance_alert(creator, "creator")
            balance_alert(consumer, "consumer")



        if active_network== 'bsc-test' or active_network== 'rinkeby' :
            accounts.add(config['wallets']['admin'])
            accounts.add(config['wallets']['creator'])
            accounts.add(config['wallets']['consumer'])

            admin= accounts[0]
            creator= accounts[1]
            consumer= accounts[2]

            balance_alert(admin, "admin")
            balance_alert(creator, "creator")
            balance_alert(consumer, "consumer")


        if active_network == 'bsc-main':
            accounts.add(config['wallets']['admin'])
            accounts.add(config['wallets']['creator'])
            accounts.add(config['wallets']['consumer'])

            admin= accounts[0]
            creator= accounts[1]
            consumer= accounts[2]

    except Exception:
        console.print_exception()
        # Test net contract address