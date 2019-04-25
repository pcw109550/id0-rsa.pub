#!/usr/bin/env python3
from config import ct
from hashlib import md5

chest = ""
key = "FWIUNYXZSVRGTODMQJLECKAPHB"

dec = ""
for c in ct:
    dec += chr(ord("A") + key.index(c))

print(md5(dec.encode()).hexdigest())
