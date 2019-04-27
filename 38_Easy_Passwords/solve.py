#!/usr/bin/env python
from passlib.hash import md5_crypt
from itertools import product
from string import ascii_lowercase


def hash(salt, msg):
    h = md5_crypt.using(salt=salt, salt_size=8)
    return h.hash(msg)


def step1(salt, res, datas):
    # https://www.scrapmaker.com/data/wordlists/dictionaries/rockyou.txt
    f = open("rockyou.txt", "r")
    while True:
        m = f.readline().strip('\x0a')
        h = hash(salt, m)[12:]
        if h in datas:
            for i in range(len(datas)):
                if datas[i] == h:
                    res[i] = m
            print(m)
            print(res)
    f.close()
    return res


def step2(salt, res, datas):
    for n in range(2, 5):
        for m in product(list(ascii_lowercase), repeat=n):
            m = "".join(m)
            h = hash(salt, m)[12:]
            if h in datas:
                for i in range(len(datas)):
                    if datas[i] == h:
                        res[i] = m
                print(m)
                print(res)
    return res

f = open("data", "r")
data = f.read()
f.close()

datas = data.split("\n")[:-1]

salt = [d.split('$')[2:] for d in datas][0][0]
datas = [d.split('$')[-1] for d in datas]

res = [""] * len(datas)
# res = step1(salt, res, datas)
res = ["the", "second", "letter", "", "each", "word", "", "this", "", "", "order"]
# res = step2(salt, res, datas)
res = ["the", "second", "letter", "of", "each", "word", "in", "this", "list", "in", "order"]

res = "".join([c[1] for c in res])
print(res)

