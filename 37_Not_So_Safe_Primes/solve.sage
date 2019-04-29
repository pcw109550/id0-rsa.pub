#!/usr/bin/env sage
from config import g, p, url
import requests


def getsecret(message):
    message = "{:x}".format(int(message))
    r = requests.get(url + message)
    if r.status_code == 200:
        return int(r.text, 16)
    return None


def pohlig_hellmen(g, y, p):
    R = IntegerModRing(p)

    [g, y] = [R(n) for n in [g, y]]
    N = factor(p - 1)

    c = [[], []]
    for prime_factor in N:
        p_i, e_i = prime_factor[0], prime_factor[1]
        g_i = g ** ((p - 1) / (p_i ** e_i))
        y_i = y ** ((p - 1) / (p_i ** e_i))
        x_i = log(y_i, g_i)
        c[0].append(x_i)
        c[1].append(p_i ** e_i)

    x = crt(c[0], c[1])
    return x


a_priv = 1
a_pub = Integer(g).powermod(a_priv, p)
S = getsecret(a_pub)
x = pohlig_hellmen(a_pub, S, p)

print(str(x)[-50:])
