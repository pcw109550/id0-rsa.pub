#!/usr/bin/env python3
import string

chset = string.ascii_uppercase
N = len(chset)

f = open("ct", "r")
ct = f.read().strip()
f.close()

for i in range(N):
    pt = ""
    for c in ct:
        x = chset.find(c)
        pt += chset[(x + i) % N]
    if "CAESAR" in pt:
        print("KEY: {:s}".format(chset[i]))
        break

assert(len(ct) == len(pt))

print("PT: {:s}".format(pt))
sol = "VAJDUXFCPV"

