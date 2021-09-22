from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np
import time
import timeit
import psutil
import hashlib
#from pqcrypto.sign.rainbowIIIc_classic import generate_keypair, sign, verify
iters = 1000000000
sec_to_ms = 1000
dot_index = 0

#SHA2_256 
setup_code_SHA2_256 = """
import hashlib
hashString = bytes.fromhex("3e580a819609b7d0ec628d6be3e0ea9928f3c952777118a46ce81271ef556fa64625df47e1d9b6d048562108b55b7c04d3138753a3878078de5e5d45bf0429d5")
"""

statement_SHA2_256 = """
h = hashlib.sha256(hashString)
"""
SHA2_256_hash_time = timeit.timeit(setup = setup_code_SHA2_256, stmt = statement_SHA2_256, number = iters)/iters * sec_to_ms

print('First Done')

#SHA3-512
setup_code_SHA3_512 = """
import hashlib
hashString = bytes.fromhex("3e580a819609b7d0ec628d6be3e0ea9928f3c952777118a46ce81271ef556fa64625df47e1d9b6d048562108b55b7c04d3138753a3878078de5e5d45bf0429d5")
"""

statement_SHA3_512 = """
h = hashlib.sha3_512(hashString)
"""
SHA3_512_hash_time = timeit.timeit(setup = setup_code_SHA3_512, stmt = statement_SHA3_512, number = iters)/iters * sec_to_ms

print('Second Done')

fig, ax = plt.subplots() 
x = ['SHA2-256', 'SHA3-512']
energy = [SHA2_256_hash_time, SHA3_512_hash_time]

x_pos = [i for i, _ in enumerate(x)]
print(SHA2_256_hash_time, SHA3_512_hash_time)
plt.bar(x_pos, energy)
plt.xlabel("Algorithm Types")
plt.ylabel("CPU Time (ms)")
plt.title("Cryptographic Hashing Algortihms - Hashing Time (Over The Average of {} Iterations)".format(iters))

plt.xticks(x_pos, x)

plt.show()
