from math import gcd
from sympy.ntheory.modular import crt
from sympy import integer_nthroot
from Crypto.Util.number import long_to_bytes

ct = []

mods = []
cts = []
with open("./src/public_keys.txt", "r") as f :
    lines = f.readlines()
    for l in lines :
        s = l.split(',')
        mods.append(int(s[0]))

with open("./src/ciphertexts.bin", "rb") as f :
    data = f.read()
    for i in range(0, len(data), len(data) // 10):
        cts.append(int.from_bytes(data[i: i + len(data) // 10]))

x, _ = crt(mods, cts)
m = integer_nthroot(x, 3)
print(long_to_bytes(m[0]))