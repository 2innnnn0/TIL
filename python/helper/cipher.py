#!/usr/bin/python
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import binascii

BS = 32
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS).encode()
unpad = lambda s: s[:-ord(s[len(s)-1:])]

class AESCipher(object):
    """
    https://github.com/dlitz/pycrypto
    """

    def __init__(self, key, iv):
        self.key = key[:32]
        self.iv = binascii.unhexlify(iv)
        #self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, message):
        """
        It is assumed that you use Python 3.0+
        , so plaintext's type must be str type(== unicode).
        """
        message = message.encode()
        raw = pad(message)
        
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        enc = cipher.encrypt(raw)
        return base64.b64encode(enc).decode('utf-8')

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        
        dec = cipher.decrypt(enc)
        
        return unpad(dec).decode('utf-8')