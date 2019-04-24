#!/usr/bin/env sage
from config import ct, pk

n = len(pk)

M = Matrix.identity(n) * 2

last_row = [1 for x in pk]
M_last_row = Matrix(ZZ, 1, len(last_row), last_row)

last_col = pk
last_col.append(ct)
M_last_col = Matrix(ZZ, len(last_col), 1, last_col)

M = M.stack(M_last_row)
M = M.augment(M_last_col)

X = M.LLL()

sol = []
for i in range(n + 1):
    testrow = X.row(i).list()[:-1]
    if set(testrow).issubset([-1, 1]):
        for v in testrow:
            if v == 1:
                sol.append(0)
            elif v == -1:
                sol.append(1)
        break

assert(ct == sum([x * y for (x, y) in zip(sol, pk)]))
print("{:x}".format(int("".join(map(str, sol)), 2)).decode("hex"))
