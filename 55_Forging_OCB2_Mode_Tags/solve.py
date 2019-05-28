from config import ct, pt, ct_
# https://eprint.iacr.org/2018/1040.pdf


def sxor(s1, s2):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(s1, s2)])


n = len(ct) / 2
assert sxor(pt[:n], ct) == ct_

T_ = sxor(pt[n:], ct[n:])

print(T_.encode("hex"))
