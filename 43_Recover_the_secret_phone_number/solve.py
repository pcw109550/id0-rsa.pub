#!/usr/bin/env python
from Crypto.PublicKey import RSA
from config import c
import base64
import os


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


f = open("raw", "r")
priv = f.read()
f.close()

filename = "decoded.gz"
f = open(filename, "w")
f.write(base64.b64decode(priv))
f.close()

os.system("gzip -d " + filename)
f = open(filename.rstrip(".gz"))
data = f.read()
f.close()

data = base64.b64decode(data)
data = "\n".join(data.split("\n")[-6:])
f = open("pub.pem", "w")
f.write(data.strip() + "\n")
f.close()

key = RSA.importKey(open("pub.pem").read())
# use factor.db to factorize n
p = 36746043666799590428244633799627952632279158164343087642676032283815739666511279233373417143396810270092798736308917
q = 33478071698956898786044169848212690817704794983713768568912431388982883793878002287614711652531743087737814467999489
assert(p * q == key.n)

phin = (p - 1) * (q - 1)
d = modinv(key.e, phin)
m = str(pow(c, d, key.n))

ph = m[:3] + "-" + m[3:6] + "-" + m[6:]
print(ph)
