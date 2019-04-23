#!/usr/bin/env sage
from config import *

p = 6277101735386680763835789423207666416083908700390324961279
b = 0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1
E = EllipticCurve(Zmod(p), [0, 0, 0, -3, b])

k = (z1 - z2) * inverse_mod(s1 - s2, n) % n

print("{:x}".format(k))
