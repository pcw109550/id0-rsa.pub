#!/usr/bin/env sage
from config import g, p, q
from config import m1, r1, s1, m2, r2, s2
from config import a, c, m
from hashlib import sha1
from itertools import product
# https://cseweb.ucsd.edu/~mihir/papers/dss-lcg.pdf


def Babai_closest_vector(M, G, target):
    # http://mslc.ctf.su/wp/plaidctf-2016-sexec-crypto-300/
    small = target
    for _ in xrange(1):
        for i in reversed(range(M.nrows())):
            c = ((small * G[i]) / (G[i] * G[i])).round()
            small -= M[i] * c
    return target - small

z1 = int(sha1(m1).hexdigest(), 16)
z2 = int(sha1(m2).hexdigest(), 16)

B = Matrix([
    [-r1, -r2,   0, 2 / q,     0,     0],
    [ s1,   0,  -a,     0, 2 / m,     0],
    [  0,  s2,   1,     0,     0, 2 / m],
    [  q,   0,   0,     0,     0,     0],
    [  0,   q,   0,     0,     0,     0],
    [  0,   0,   m,     0,     0,     0]
])

Y = vector([z1, z2, c, 1, 1, 1])

M = B.LLL()
G = M.gram_schmidt()[0]
W = Babai_closest_vector(M, G, Y)

x = None
if W[0] == Y[0] and W[1] == Y[1] and W[2] == Y[2]:
    x = W[3] * q / 2
    k1 = W[4] * m / 2
    k2 = W[5] * m / 2

if x is not None:
    print("{:x}".format(int(x)))
