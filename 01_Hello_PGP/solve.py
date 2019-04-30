#!/usr/bin/env python3
from subprocess import run


def check(password, filedata):
    cmd = "echo '{:s}' | ".format(filedata)
    cmd += "gpg -d --passphrase '{:s}' ".format(password)
    cmd += "--no-use-agent 2> /dev/null"
    if run(cmd, shell=True).returncode == 0:
        return True
    return False


filename = "enc.pgp"
f = open(filename, "r")
filedata = f.read()
f.close()
for word in open("/usr/share/dict/words", "r"):
    if "'" in word:
        continue
    word = word.strip()
    if check(word, filedata):
        print("\npassphrase: {:s}".format(word))
        break
