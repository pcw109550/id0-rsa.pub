#!/usr/bin/env python3
from config import *

# Goal: m = "Deposit amount: One million dollars"
[c1, c2, c3] = [bytes.fromhex("{:x}".format(x)) for x in [c1, c2, c3]]

m = m1[:N] + m2[:N] + m3[N:N * 2]
print("m = {:s}".format(m))

c = c1[:N] + c2[:N] + c3[N:N * 2]
c = c.hex()
print(c)
