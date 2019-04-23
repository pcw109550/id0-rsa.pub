from config import c1, c2
from itertools import product
from string import ascii_letters
chset = ascii_letters + " "


def observe(chset, m, n):
    for c in product(list(chset), repeat=n):
        cnt = 0
        temp = bxor(m[:n], bytes("".join(c).encode()))
        for p in temp:
            if chr(p) in chset:
                cnt += 1
        if cnt == n:
            print(temp)
        # print(cnt)


def bxor(b1, b2):
    parts = []
    for b1, b2 in zip(b1, b2):
        parts.append(bytes([b1 ^ b2]))
    return b"".join(parts)


[c1, c2] = [bytes.fromhex("{:x}".format(x)) for x in [c1, c2]]

mxor = bxor(c1, c2)
# observe(chset, m, 5)

m1 = b"this is the text"
m2 = bxor(mxor, m1)
m1 = m1.decode()
m2 = m2.decode()

assert(len(m1) == len(c1))
assert(len(m2) == len(c2))

print("m1 = {:s}".format(m1))
print("m2 = {:s}".format(m2))

print("".join(sorted([m1, m2])))


