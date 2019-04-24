#!/usr/bin/env python3
from hashlib import md5
from Crypto.Cipher import AES
from config import c
from string import printable
import datetime


def genkey(t):
    return md5(str(t).encode()).digest()

s1 = "24/01/2016"
s2 = "31/01/2016"
[t1, t2] = [int(datetime.datetime.strptime(s, "%d/%m/%Y").timestamp()) for s in [s1, s2]]

c = c.to_bytes(16, byteorder="big")

for t in range(t1, t2):
    key = genkey(t)
    cipher = AES.new(key, AES.MODE_ECB)
    m = cipher.decrypt(c)
    if all(chr(k) in printable for k in m):
        print(m.decode("utf-8"))
        break
