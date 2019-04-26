#!/usr/bin/env sage
from config import g, p, q, y
from config import m1, r1, s1, m2, r2, s2
from hashlib import sha256

g = Integer(g)
[z1, z2] = [int(sha256(m.encode()).hexdigest(), 16) for m in [m1, m2]]

# same k was used since r1 and r2 are same
assert(r1 == r2)

k = (z1 - z2) * inverse_mod(s1 - s2, q) % q

x = (z1 * s2 - z2 * s1) * inverse_mod(r1 * (s1 - s2), q) % q
assert(inverse_mod(k, q) * (z1 + x * r1) % q == s1)
assert(inverse_mod(k, q) * (z2 + x * r2) % q == s2)

print("{:x}".format(x))
