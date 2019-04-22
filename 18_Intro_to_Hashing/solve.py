#!/usr/bin/env python3
import hashlib

pt = "id0-rsa.pub".encode()

res = hashlib.sha256(pt).hexdigest().encode()
res = hashlib.md5(res).hexdigest()

print(res)
