from config import a, b, p
from config import d, out, P, Q
# http://dualec.org/DualECTLS.pdf

E = EllipticCurve(Zmod(p), [0, 0, 0, a, b])
[P, Q] = [E(P), E(Q)]
assert(P in E and Q in E)
assert(P == d * Q)
R = IntegerModRing(p)

out_ = out >> (2 * 8)
check = out & ((2 ** 16) - 1)

for i in range(2 ** 16):
    guess = out_ + (i << (30 * 8))
    x = R(guess)
    if E.is_x_coord(x):
        sQ = E.lift_x(x)
        # A = d * s * Q = s * P
        A = d * sQ
        s = Integer(A[0])
        B = s * Q
        r = Integer(B[0]) & ((2 ** (8 * 30)) - 1)
        r = r >> (8 * 28)
        if r == check:
            sol = Integer(B[0]) & ((2 ** (8 * 28)) - 1)
            print("{:x}".format(sol))
            break
