from Crypto.PublicKey import RSA

c = 0x6794893f3c47247262e95fbed846e1a623fc67b1dd96e13c7f9fc3b880642e42

key = RSA.import_key(open('privkey.der').read())
d = key.d
n = key.n

m = pow(c, d, n)

print("{:x}".format(m))
