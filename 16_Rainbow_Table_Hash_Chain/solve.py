#!/usr/bin/env python
from hashlib import sha256
from config import c, pw_start

c = "{:x}".format(c)
num_lines = sum(1 for line in open("rockyou.txt"))


def password_hash(pw):
    val = ""
    for i in range(50000):
        val = sha256(val + pw).digest()
    return val.encode("hex")


def reverse(password_hash, column_number):
    num_val = int(password_hash, 16)
    line_number = (num_val + column_number) % num_lines
    with open("rockyou.txt", "r") as f:
        for _ in range(line_number + 1):
            password = f.readline()
    return password


def iterate():
    pw = pw_start
    for i in range(200):
        pw_hash = password_hash(pw)
        print(i, pw, pw_hash)
        if pw_hash == c:
            break
        pw = reverse(pw_hash, i).strip()
    assert(pw_hash == c)
    return pw


def main():
    pw = iterate()
    print("pw: {:s}".format(pw))

if __name__ == "__main__":
    main()


