from scripts.com_functions import *
from brownie import SUPERCOOLPEEPS

def main():
    active_network= network.show_active()
    print("Current Network:"+ active_network)

    admin, creator, consumer, iwan= get_accounts(active_network)

    try:
        if active_network in TEST_NETWORKS:
            SUPERCOOLPEEPS.deploy(addr(admin))

    except Exception:
        console.print_exception()
        # Test net contract address

if __name__=="__main__":
    main()