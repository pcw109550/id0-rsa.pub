#!/usr/bin/env python3
from config import n, e, d
from math import gcd
import random


def factor(n, e, d):
    k = d * e - 1
    while True:
        g = random.randint(2, n - 1)
        t = k
        while t % 2 == 0:
            t = t // 2
            x = pow(g, t, n)
            y = gcd(x - 1, n)
            if x > 1 and y > 1:
                (p, q) = (y, n // y)
                assert(p * q == n)
                if p < q:
                    (p, q) = (q, p)
                return (p, q)


(p, q) = factor(n, e, d)

print("p = {:d}".format(p))
print("q = {:d}".format(q))
print("q % 100000007 = {:d}".format(q % 100000007))
