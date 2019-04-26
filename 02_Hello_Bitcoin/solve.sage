#!/usr/bin/env sage
from config import x, p, a, b, Gx, Gy
import hashlib

E = EllipticCurve(GF(p), [a, b])
G = E(Gx, Gy)

Q = x * G
(Qx, Qy) = (int(Q[0]), int(Q[1]))

print("x: {:x}".format(x))
[Qx, Qy] = ["{:x}".format(int(Qp)) for Qp in [Q[0], Q[1]]]

pub = "04" + Qx + Qy
print("1 = pubkey: {:s}".format(pub))

t = hashlib.sha256(pub.decode("hex")).hexdigest()
print("2 = sha256(1): {:s}".format(t))
h = hashlib.new("ripemd160")
h.update(t.decode("hex"))

header = "00"
t = header + h.hexdigest()
print("3 = network byte + ripemd160(2): {:s}".format(t))

t = hashlib.sha256(t.decode("hex")).hexdigest()
print("4 = sha256(3): {:s}".format(t))

t = hashlib.sha256(t.decode()).hexdigest()
print("5 = sha256(4): {:s}".format(t))

cksum = t.decode()[:4].encode("hex")
print("ckecksum: {:s}".format(cksum))
t = header + h.hexdigest() + cksum
print("6 = checksum + 5: {:s}".format(t))

# TODO: Implement base58
res = "18GZRs5nx8sVhF1xVAaEjKrYJga4hMbYc2"
print("7 = base58(6): {:s}".format(res))
