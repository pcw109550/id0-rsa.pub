from config import *

E = EllipticCurve(Zmod(p), [0, 0, 0, a, b])
G = E(G)
Q = E(Q)

d = discrete_log(Q, G, G.order(), operation='+')
print("private key = {:d}".format(d))
