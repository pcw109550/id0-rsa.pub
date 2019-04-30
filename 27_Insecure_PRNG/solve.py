#!/usr/bin/env python3
from config import a, c, m, target
from config import test_vec


class lcg:
    def __init__(self, seed=1):
        if not 0 <= seed < m:
            raise ValueError("0 <= seed < m does not hold")
        self.state = seed

    def random(self):
        self.state = (a * self.state + c) % m
        return (self.state >> 29) & 1


def check():
    prng = lcg(0x123)
    res = 0
    for i in range(256):
        res = (res << 1) + prng.random()
    assert(res == test_vec)


def brute():
    t = "{:b}".format(target).zfill(256)
    for i in range(2 ** 25):
        prng = lcg(i)
        res = 0
        for j in range(32):
            res = (res << 1) + prng.random()
        res = "{:b}".format(res).zfill(32)
        if res in t:
            return i
    return None


def main():
    check()
    # seed = brute()
    seed = 5361603
    prng = lcg(seed)
    res = 0

    for j in range(32):
        res = (res << 1) + prng.random()

    t = "{:b}".format(target).zfill(256)
    temp = "{:b}".format(res).zfill(32)
    ind = t.index(temp)

    for j in range(256 - 32 - ind):
        res = (res << 1) + prng.random()

    assert("{:b}".format(res).zfill(256 - ind) == t[ind:])

    res = 0
    for j in range(256):
        res = (res << 1) + prng.random()

    print("{:x}".format(res))
    # base58 encode
    ans = "5KiHNrKWK78YyQzJmPXyVPyFCmx1up6QF7ocuLErRT3wAXBP9WW"
    print(ans)

if __name__ == "__main__":
    main()

