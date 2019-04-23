from Crypto.PublicKey import RSA
from config import c
from math import gcd


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


key1 = RSA.import_key(open("pub1.pem").read())
key2 = RSA.import_key(open("pub2.pem").read())

p = gcd(key1.n, key2.n)
q = key1.n // p
assert(p * q == key1.n)

phin = (p - 1) * (q - 1)
d = modinv(key1.e, phin)

m = pow(c, d, key1.n)

print("{:x}".format(m))
