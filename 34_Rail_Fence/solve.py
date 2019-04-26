#!/usr/bin/env python3
from functools import reduce

def getchr(data):
    N = len(data)
    cnt = 0
    while cnt < N:
        # print(data[cnt])
        yield data[cnt]
        cnt += 1


def bxor(b1, b2):
    result = bytearray()
    for b1, b2 in zip(b1, b2):
        result.append(b1 ^ b2)
    return bytes(result)


def getdata():
    f = open("data", "r")
    data = f.read().strip()
    f.close
    data = data.replace(" ", "")
    return data


def main():
    data = getdata()
    k = 17
    print("KEY: {:d}".format(k))
    res = decode(data, k)
    print("PT: {:s}".format(res))
    sol = res[125:133]
    print(sol)


def decode(data, k):
    dec = ""
    sp = "."
    N = len(data)
    gen = getchr(data)
    cycle = k * 2 - 2
    (width, temp) = (N // cycle, N % cycle)
    app = [0] * k

    for i in range(temp):
        if i < k:
            app[i] += 1
        else:
            app[k - 2 - i % k] += 1

    for i in range(k):
        for j in range(width):
            if i == 0:
                chunk = next(gen) + (sp * (cycle - 1))
            elif i == k - 1:
                chunk = (sp * (cycle // 2)) + next(gen) + (sp * ((cycle // 2) - 1))
            else:
                chunk = (sp * i) + next(gen) + (sp * (cycle - 2 * i - 1))
                chunk += next(gen) + (sp * (i - 1))
            assert(len(chunk) == cycle)
            dec += chunk
        if app[i] == 2:
            dec += (sp * i) + next(gen) + (sp * (cycle - 2 * i - 1))
            dec += next(gen) + (sp * (i - 1))
        elif app[i] == 1:
            if i == 0:
                dec += next(gen) + (sp * (cycle - 1))
            elif i == k - 1:
                dec += (sp * (cycle // 2)) + next(gen) + (sp * ((cycle // 2) - 1))
            else:
                dec += (sp * i) + next(gen) + (sp * (cycle - i - 1))
        else:
            dec += sp * cycle
        dec += "\n"

    dec = dec.split("\n")[:-1]
    dec = [c.encode() for c in dec]
    dec = reduce(lambda x, y: bxor(x, y), dec).decode().strip().rstrip(sp)
    return dec

if __name__ == "__main__":
    main()
