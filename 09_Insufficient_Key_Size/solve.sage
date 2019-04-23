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


key = RSA.importKey(open("pub.pem").read())

res = str(factor(key.n)).split()
q = int(res[0])
p = int(res[2])

phin = (p - 1) * (q - 1)
d = modinv(key.e, phin)

print("{:x}".format(d))
