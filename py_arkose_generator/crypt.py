import base64
import hashlib
import json
import random

from Crypto.Cipher import AES


def pad(data):
    """
    The pad function takes a string and returns the same string with padding bytes appended to it.
    The number of padding bytes is determined by the length of the input string, which must be a multiple
    of 16 in order for AES encryption to work properly. The value of each byte is equal to its position in
    the padded output (e.g., if there are two padding bytes, they will have values 0x02 and 0x02). This
    padding scheme is known as PKCS#7.

    Args:
        data: Pass the data to be encrypted

    Returns:
        A bytes object
    """

    # Convert the string to bytes and calculate the number of bytes to pad
    data_bytes = data.encode()
    padding = 16 - (len(data_bytes) % 16)
    # Append the padding bytes with their value
    return data_bytes + bytes([padding] * padding)


def encrypt(data, key):
    """
    The encrypt function takes a string of data and a key, and returns an encrypted version of the data.
    The encryption is AES-256 in CBC mode with PKCS#7 padding. The IV is randomly generated for each encryption,
    and prepended to the ciphertext before it's base64 encoded.

    Args:
        data: Pass the data to be encrypted
        key: Generate the key for encryption

    Returns:
        A json object with the encrypted data, iv and salt
    """

    salt = ""
    salted = ""
    dx = bytes()

    # Generate salt, as 8 random lowercase letters
    salt = "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(8))

    # Our final key and IV come from the key and salt being repeatedly hashed
    for x in range(3):
        dx = hashlib.md5(dx + key.encode() + salt.encode()).digest()
        salted += dx.hex()

    # Pad the data before encryption
    data = pad(data)

    aes = AES.new(
        bytes.fromhex(salted[:64]), AES.MODE_CBC, bytes.fromhex(salted[64:96])
    )

    return json.dumps(
        {
            "ct": base64.b64encode(aes.encrypt(data)).decode(),
            "iv": salted[64:96],
            "s": salt.encode().hex(),
        }
    )
