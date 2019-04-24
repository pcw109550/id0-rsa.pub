#!/usr/bin/env python
from hashlib import sha256
import base64
import os


def hash(salt, password):
    hash_val = sha256(password + salt).digest()
    return '$' + salt + '$' + base64.b64encode(hash_val)


f = open("data", "r")
data = f.read()
f.close()

datas = data.split("\n")[:-1]
data = [d.split("$")[1:3] for d in datas]
salts = [d[0] for d in data]
hashs = [d[1] for d in data]

res = []

for salt in salts:
    cnt = 0
    # http://downloads.skullsecurity.org/passwords/rockyou.txt.bz2
    f = open("rockyou.txt", "r")
    while True:
        cnt += 1
        m = f.readline().strip('\x0a')
        if hash(salt, m) in datas:
            print(salt, m)
            res.append(m)
            break
        if f.tell() == os.fstat(f.fileno()).st_size:
            print(salt, None)
            break
    f.close()

print("".join(sorted(res)))
