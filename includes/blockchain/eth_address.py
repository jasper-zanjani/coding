import random
import hashlib

def eth_address():
    # Random 20-byte address
    address = random.random(2 ** (20 * 8))
    address_hex = 
    address_hash = hashlib.sha3_256(address.to_bytes(20, 'big')).hex()

