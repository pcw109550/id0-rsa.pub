#!/usr/bin/env python3
from config import ct
from functools import reduce
from string import ascii_uppercase


def getchr(data):
    N = len(data)
    cnt = 0
    while cnt < N:
        # print(data[cnt])
        yield data[cnt]
        cnt += 1


def bxor(b1, b2):
    result = bytearray()
    for b1, b2 in zip(b1, b2):
        result.append(b1 ^ b2)
    return bytes(result)


def decode_vigenere(ct, k):
    N = len(ascii_uppercase)
    dec = ""
    for i in range(len(ct)):
        dec += chr(ord('A') + (ord(ct[i]) - ord(k[i % len(k)])) % N)
    return dec


def decode_rail_fence(data, k):
    dec = ""
    sp = "."
    N = len(data)
    gen = getchr(data)
    cycle = k * 2 - 2
    (width, temp) = (N // cycle, N % cycle)
    app = [0] * k

    for i in range(temp):
        if i < k:
            app[i] += 1
        else:
            app[k - 2 - i % k] += 1

    for i in range(k):
        for j in range(width):
            if i == 0:
                chunk = next(gen) + (sp * (cycle - 1))
            elif i == k - 1:
                chunk = (sp * (cycle // 2)) + next(gen) + (sp * ((cycle // 2) - 1))
            else:
                chunk = (sp * i) + next(gen) + (sp * (cycle - 2 * i - 1))
                chunk += next(gen) + (sp * (i - 1))
            assert(len(chunk) == cycle)
            dec += chunk
        if app[i] == 2:
            dec += (sp * i) + next(gen) + (sp * (cycle - 2 * i - 1))
            dec += next(gen) + (sp * (i - 1))
        elif app[i] == 1:
            if i == 0:
                dec += next(gen) + (sp * (cycle - 1))
            elif i == k - 1:
                dec += (sp * (cycle // 2)) + next(gen) + (sp * ((cycle // 2) - 1))
            else:
                dec += (sp * i) + next(gen) + (sp * (cycle - i - 1))
        else:
            dec += sp * cycle
        dec += "\n"

    dec = dec.split("\n")[:-1]
    dec = [c.encode() for c in dec]
    dec = reduce(lambda x, y: bxor(x, y), dec).decode().strip().rstrip(sp)
    return dec


KEY1 = 21
KEY2 = "TRADER"
ct = decode_rail_fence(ct, KEY1)
pt = decode_vigenere(ct, KEY2)
print(pt)
