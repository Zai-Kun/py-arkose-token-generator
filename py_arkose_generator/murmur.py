import struct

import mmh3


def x64hash128(data, seed=0):
    """
    The x64hash128 function takes a string and returns the MurmurHash3 128-bit hash as a hexadecimal string.

    Args:
        data: Pass in the data that you want to hash
        seed: Change the output of the hash function

    Returns:
        A string of 32 hexadecimal characters
    """

    hash_bytes = mmh3.hash_bytes(data, seed=seed, x64arch=True)
    hash_hex = struct.unpack("<QQ", hash_bytes)
    hash_hex_str = "{:016x}{:016x}".format(*hash_hex)

    return hash_hex_str
