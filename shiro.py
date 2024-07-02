import sys

import uuid

import base64

import subprocess

from Crypto.Cipher import AES

def get_file(name):

    with open(name,'rb') as f:

        data = f.read()

    return data

def en_aes(data):

    BS = AES.block_size

    pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()

    key = base64.b64decode("kPH+bIxk5D2deZiIxcaaaA==")

    iv = uuid.uuid4().bytes

    encryptor = AES.new(key, AES.MODE_CBC, iv)

    base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(pad(data)))

    return base64_ciphertext

if __name__ == '__main__':

    data = get_file("ser.bin")

    print(en_aes(data))
