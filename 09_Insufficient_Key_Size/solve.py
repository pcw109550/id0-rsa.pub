from Crypto.PublicKey import RSA


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


key = RSA.import_key(open("pub.pem").read())

# factored using sage
(q, p) = (662700133751480051, 878291059745115859)

phin = (p - 1) * (q - 1)
d = modinv(key.e, phin)

print("{:x}".format(d))
