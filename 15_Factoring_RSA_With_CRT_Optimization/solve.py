from config import *
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


fault = pow(y, e, n)
p = gcd(fault - x, n)
q = n // p
assert(p * q == n)
phin = (p - 1) * (q - 1)

d = modinv(e, phin)

print("{:d}".format(d % 1000000007))
