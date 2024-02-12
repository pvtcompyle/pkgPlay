import logging
# logging.basicConfig(level=logging.DEBUG)

def list_noncontiguous(network:str="192.168.2.1/0.1.0.5"):
    from ipaddress import ip_network

    logging.info(f'list_nonccontiguous(): Figuring out: {network}')