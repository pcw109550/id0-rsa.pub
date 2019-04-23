#!/usr/bin/env python3
import itertools
import hashlib


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None
    else:
        return x % m


chset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ,."
N = len(chset)
print("length of chset: {:d}".format(N))

f = open("ct.txt", "r")
ct = f.read().strip()
f.close()

for (a, b) in itertools.product(range(N), repeat=2):
    pt = ""
    ainv = modinv(a, N)
    if ainv is None:
        continue
    for c in ct:
        x = chset.find(c)
        pt += chset[(ainv * (x - b)) % N]
    if "COMMERCE" in pt:
        print("a = {:d}, b = {:d}".format(a, b))
        break

assert(len(pt) == len(ct))

print("pt:\n{:s}".format(pt))
print(hashlib.md5(pt.encode()).hexdigest())
