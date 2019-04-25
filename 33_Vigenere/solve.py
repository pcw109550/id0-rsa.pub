#!/usr/bin/env python3
from config import ct
from string import ascii_uppercase

N = len(ascii_uppercase)
k = "BARLEY"

dec = ""
for i in range(len(ct)):
    dec += chr(ord('A') + (ord(ct[i]) - ord(k[i % len(k)])) % N)

assert("VIGENERE" in dec)
print(k)
