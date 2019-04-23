#!/usr/bin/env python
from hashlib import sha256
import os

# http://downloads.skullsecurity.org/passwords/rockyou.txt.bz2
f = open("rockyou.txt", "r")

largest = b"\x00" * 32
largeval = ""
smallest = b"\xff" * 32
smallval = ""

while True:
    m = f.readline().strip('\x0a')
    h = sha256(m).digest()
    if h > largest:
        (largest, largeval) = (h, m)
    if h < smallest:
        (smallest, smallval) = (h, m)
    if f.tell() == os.fstat(f.fileno()).st_size:
        break

[largeval, smallval] = [x.decode() for x in [largeval, smallval]]

print(largeval + smallval)
