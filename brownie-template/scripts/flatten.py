from scripts.com_functions import *
from brownie import SUPERCOOLPEEPS

def main():
    active_network= "developmet"
    print("Current Network:"+ active_network)
    admin, creator, consumer, iwan= get_accounts(active_network)
    
    try:
        supercool= SUPERCOOLPEEPS.deploy(addr(admin))

        flat_contract('supercool', SUPERCOOLPEEPS.get_verification_info())

    except Exception:
        console.print_exception()
        # Test net contract address

if __name__=="__main__":
    main()