import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto import Random

'''Main class for encrypting and decrypting data'''
class Crypter:

    def __init__(self):
        '''initial constants'''
        self.MAX_LENGTH = 12
        self.mode = AES.MODE_CBC
        self.BLOCK_SIZE = 16

    def generate_key(self, line):
        '''generates MAX_LENGTH's-long bytes from a custom string line'''
        if len(line) < self.MAX_LENGTH:
            line += "0" * (self.MAX_LENGTH - len(line))
        elif len(line) > self.MAX_LENGTH:
            line = line[:self.MAX_LENGTH]
        return base64.b64encode(line.encode("utf-8"))
    
    def encrypt(self, key: str, data: str):
        '''Encryption method'''
        key = self.generate_key(key)
        iv = base64.b64encode(Random.get_random_bytes(self.MAX_LENGTH)) # Salt for ecnryption
        encrypter = AES.new(key, self.mode, iv=iv)
        encrypted_data = base64.b64encode(encrypter.encrypt(pad(data.encode("utf-8"), self.BLOCK_SIZE)))
        result = f"{iv.decode("utf-8")}:{encrypted_data.decode("utf-8")}" # forms string that contains salt:data in base64
        return result

    def decrypt(self, key: str, encoded_data: str):
        '''Decryption method'''
        key = self.generate_key(key)
        iv, data = encoded_data.split(":") # Gets salt and data from encrypted line
        iv = iv.encode("utf-8")
        data = base64.b64decode(data)
        decrypter = AES.new(key, self.mode, iv) 
        result = unpad(decrypter.decrypt(data), self.BLOCK_SIZE)
        print(result)
        # decrypter = AES.new(key, self.mode, iv=iv.encode("utf-8"))
        # result = base64.b64decode(unpad(decrypter.decrypt(base64.b64decode(data)), self.BLOCK_SIZE)).decode("utf-8")
        # return result
