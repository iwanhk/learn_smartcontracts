from scripts.com_functions import *
from brownie import ContractDataStorage, SvgParser, CyberBrokersMetadata, CyberBrokers

def main():
    active_network= "developmet"
    print("Current Network:"+ active_network)
    admin, creator, consumer, iwan= get_accounts(active_network)
    
    try:
        svg= SvgParser.deploy(addr(admin))
        data_storage= ContractDataStorage.deploy(addr(admin))
        meta_data= CyberBrokersMetadata.deploy(data_storage, svg, addr(admin))
        broker= CyberBrokers.deploy(meta_data, addr(admin))

        flat_contract("CyberBrokers", CyberBrokers.get_verification_info())

    except Exception:
        console.print_exception()
        # Test net contract address

if __name__=="__main__":
    main()