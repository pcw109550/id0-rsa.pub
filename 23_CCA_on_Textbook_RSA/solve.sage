#!/usr/bin/env sage
from Crypto.PublicKey import RSA
from config import c, url
import requests


def decrypt(message):
    message = "{:x}".format(message)
    r = requests.get(url + message)
    if r.status_code == 200:
        return int(r.text, 16)
    return None


key = RSA.importKey(open("pub.pem").read())

m1 = decrypt(2 * c)
m2 = decrypt(2)

m = m1 * inverse_mod(m2, key.n) % key.n

print("{:x}".format(m))
