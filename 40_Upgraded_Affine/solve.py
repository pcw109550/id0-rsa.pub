#!/usr/bin/env python3
import itertools


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


def test():
    pt = "hello, world."
    iv = "e"
    key = (2, 5)
    ct = encrypt(key, iv, pt)
    ct_ = "e,jqbgnzm.iokx"
    assert(ct == ct_)


def encrypt(key, iv, pt):
    (a, b) = key
    c = chset.find(iv)
    ct = iv + ""
    for p in pt:
        x = chset.find(p)
        c = (a * (x + c) + b) % N
        ct += chset[c]
    return ct


def brute(ct):
    for (a, b) in itertools.product(range(N), repeat=2):
        key = (a, b)
        pt = decrypt(key, ct)
        if pt is None:
            continue
        elif " the " in pt:
            print("a = {:d}, b = {:d}".format(a, b))
            return pt
        else:
            continue


def decrypt(key, ct):
    iv, ct = chset.find(ct[0]), ct[1:]
    (a, b) = key
    ainv = modinv(a, N)
    if ainv is None:
        return None
    pt = ""
    c_ = iv
    for c in ct:
        x = chset.find(c)
        p = (ainv * (x - b) - c_) % N
        c_ = x
        pt += chset[p]
    return pt


chset = "abcdefghijklmnopqrstuvwxyz ,."
N = len(chset)

f = open("ct.txt", "r")
ct = f.read().strip()
f.close()

pt = brute(ct)
assert(len(pt) == len(ct) - 1)

print("pt:\n{:s}".format(pt))
ans = "Dan Boneh"
print("answer: {:s}".format(ans))
