#!/usr/bin/env python
from config import permissions, owner_hash, doc_id
from config import user_hash, padding, key_len
from hashlib import md5
from Crypto.Cipher import ARC4
# https://www.adobe.com/content/dam/acom/en/devnet/pdf/pdf_reference_archive/PDFReference.pdf


def sxor(s1, s2):
    return "".join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))


def _convert(msg):
    return "{:x}".format(msg).decode("hex")


def convert():
    global permissions
    permissions = _convert(permissions)
    global owner_hash
    owner_hash = _convert(owner_hash)
    global doc_id
    doc_id = _convert(doc_id)
    global user_hash
    user_hash = _convert(user_hash)
    global padding
    padding = _convert(padding)


def pad(msg):
    if len(msg) > 32:
        msg = msg[:32]
    else:
        msg += padding[:32 - len(msg)]
    return msg


def gen_key(pw):
    pw = pad(pw)
    pw += owner_hash
    pw += permissions
    pw += doc_id
    assert(len(pw) == 32 + 32 + 4 + 16)

    for i in range(51):
        pw = md5(pw).digest()

    return pw[:key_len // 8]


def gen_user_hash(pw):
    pw = gen_key(pw)

    key = md5(padding + doc_id).digest()
    c = ARC4.new(pw)
    key = c.encrypt(key)

    for i in range(1, 20):
        c = ARC4.new(sxor(pw, chr(i) * 16))
        key = c.encrypt(key)

    return key


def iterate():
    f = open("rockyou.txt", "r")

    while True:
        pw = f.readline().strip('\x0a')
        if gen_user_hash(pw) == user_hash:
            return pw

    return None


def main():
    convert()
    res = iterate()
    print("{:s}".format(res))

if __name__ == "__main__":
        main()
