#!/usr/bin/env sage
from config import *

e = 3

M = N1 * N2 * N3
[m1, m2, m3] = [M // x for x in [N1, N2, N3]]

t1 = C1 * m1 * inverse_mod(m1, N1)
t2 = C2 * m2 * inverse_mod(m2, N2)
t3 = C3 * m3 * inverse_mod(m3, N3)

x = (t1 + t2 + t3) % M

m = x.nth_root(e)

assert(pow(m, e, N1) == C1)
assert(pow(m, e, N2) == C2)
assert(pow(m, e, N3) == C3)

print("{:x}".format(m).decode("hex"))
