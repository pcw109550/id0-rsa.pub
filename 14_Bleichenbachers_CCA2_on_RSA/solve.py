#!/usr/bin/env python
from config import n, e, c, url
from urllib2 import urlopen
# import random


def oracle(ctxt):
    # decryption oracle
    response = int(urlopen(url + str(ctxt)).read())
    if response == 1:
        return True
    return False


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("modular inverse does not exist")
    else:
        return x % m


def factordb():
    # unintended solution: use factordb to factorize n
    p = 3282014306048855502762732473947802268449348103132721395461
    q = 3587785326232499230469871163617998437518840696099919395911
    k = (n.bit_length() + (8 - (n.bit_length() % 8)) % 8) * 8
    assert(p * q == n)
    phin = (p - 1) * (q - 1)
    d = modinv(e, phin)
    temp = "{:x}".format(pow(c, d, n)).zfill(k / 32)
    print([temp[i:i + 2] for i in range(0, len(temp), 2)])
    m = temp[-40:].decode("hex")
    print(m)

factordb()



"""
k = n.bit_length() // 8
B = pow(2, 8 * (k - 2))

s0 = 1
i = 0
c0 = 0
M0 = [0, 0]
while True:
    s0 = random.randint(2, n - 1)
    print(s0)
    c0 = c * pow(s0, e, n) % n
    if oracle(c0):
        i = 1
        M0 = [2 * B, 3 * B - 1]
        break

s1 = n / (3 * B)

while True:
    s1 += 1
    temp = c0 * pow(s1, e, n) % n
    if oracle(temp):
        break
"""


