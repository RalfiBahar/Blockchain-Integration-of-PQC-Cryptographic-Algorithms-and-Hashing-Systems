from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np
import time
import timeit
import psutil
import hashlib
#from pqcrypto.sign.rainbowIIIc_classic import generate_keypair, sign, verify
iters = 10
sec_to_ms = 1000
dot_index = 0

print('Running' + '.' *dot_index)
dot_index += 1

 #ECDSA
setup_code_ecdsa = """
from ecdsa import SigningKey, SECP256k1
sk = SigningKey.generate(curve=SECP256k1) 
vk = sk.verifying_key
by = 't\xddrRx\xef\x13\xb1\x8b\xc0\xc3\xad\x84s\xc8Q\xa97\x1e\xe5\xbf\xb0\xdf\x9a'
print('ECDSA:', len(by))
hash = bytes.fromhex("3e580a819609b7d0ec628d6be3e0ea9928f3c952777118a46ce81271ef556fa64625df47e1d9b6d048562108b55b7c04d3138753a3878078de5e5d45bf0429d5")
signature = sk.sign(hash)
"""

statement_ecdsa = """
verif = vk.verify(signature, hash)
"""
ecdsa_keygen_time = timeit.timeit(setup = setup_code_ecdsa, stmt = statement_ecdsa, number = iters)/iters * sec_to_ms

setup_code_ecdsa521 = """
from ecdsa import SigningKey, NIST521p
sk = SigningKey.generate(curve=NIST521p)
vk = sk.verifying_key
by = 't\xddrRx\xef\x13\xb1\x8b\xc0\xc3\xad\x84s\xc8Q\xa97\x1e\xe5\xbf\xb0\xdf\x9a'
print('ECDSA:', len(by))
hash = bytes.fromhex("3e580a819609b7d0ec628d6be3e0ea9928f3c952777118a46ce81271ef556fa64625df47e1d9b6d048562108b55b7c04d3138753a3878078de5e5d45bf0429d5")
signature = sk.sign(hash)
"""

statement_ecdsa521 = """
verif = vk.verify(signature, hash)
"""
ecdsa_keygen_time521 = timeit.timeit(setup = setup_code_ecdsa521, stmt = statement_ecdsa521, number = iters)/iters * sec_to_ms

print('256', ecdsa_keygen_time)
print('521', ecdsa_keygen_time521)

# #################
# #Falcons
# #################

# #Falcon 512
# setup_code_falcon512 = """
# from pqcrypto.sign.falcon_512 import generate_keypair, sign, verify
# public_key, secret_key = generate_keypair()
# print('Falcon512 Public Key:', len(public_key))
# hash = bytes.fromhex("3e580a819609b7d0ec628d6be3e0ea9928f3c952777118a46ce81271ef556fa64625df47e1d9b6d048562108b55b7c04d3138753a3878078de5e5d45bf0429d5")
# signature = sign(secret_key, hash)
# """

# statement_falcon512  = """
# public_key, secret_key = generate_keypair()
# """
# falcon512_keygen_time = timeit.timeit(setup = setup_code_falcon512, stmt = statement_falcon512, number = iters)/iters * sec_to_ms

# print('Running' + '.' *dot_index)
# dot_index += 1

# #Falcon 1024
# setup_code_falcon1024 = """
# from pqcrypto.sign.falcon_1024 import generate_keypair, sign, verify

# """

# statement_falcon1024  = """
# public_key, secret_key = generate_keypair()
# """
# falcon1024_keygen_time = timeit.timeit(setup = setup_code_falcon1024, stmt = statement_falcon1024, number = iters)/iters * sec_to_ms

# print('Running' + '.' *dot_index)
# dot_index += 1

# #################
# #Dilithium
# #################

# #Dilithium3
# setup_code_dilithium2 = """
# from pqcrypto.sign.dilithium2 import generate_keypair, sign, verify
# """

# statement_dilithium2  = """
# public_key, secret_key = generate_keypair()
# """
# dilithium2_keygen_time = timeit.timeit(setup = setup_code_dilithium2, stmt = statement_dilithium2, number = iters)/iters * sec_to_ms

# print('Running' + '.' *dot_index)
# dot_index += 1

# #Dilithium3
# setup_code_dilithium3 = """
# from pqcrypto.sign.dilithium3 import generate_keypair, sign, verify
# """

# statement_dilithium3  = """
# public_key, secret_key = generate_keypair()
# """

# dilithium3_keygen_time = timeit.timeit(setup = setup_code_dilithium3, stmt = statement_dilithium3, number = iters)/iters * sec_to_ms

# print('Running' + '.' *dot_index)
# dot_index += 1

# #Dilithium4
# setup_code_dilithium4 = """
# from pqcrypto.sign.dilithium4 import generate_keypair, sign, verify
# """

# statement_dilithium4  = """
# public_key, secret_key = generate_keypair()
# """
# dilithium4_keygen_time = timeit.timeit(setup = setup_code_dilithium4, stmt = statement_dilithium4, number = iters)/iters * sec_to_ms

# print('Running' + '.' *dot_index)
# dot_index += 1


# print('Running' + '.' *dot_index)
# dot_index += 1
# print(ecdsa_keygen_time)

################
# #################
# #Rainbow
# #################

#Rainbow IA Classic
setup_code_rainbowIa_classic = """
from pqcrypto.sign.rainbowIa_classic import generate_keypair, sign, verify
"""

statement_rainbowIa_classic  = """
public_key, secret_key = generate_keypair()
"""

rainbowIa_classic_keygen_time = timeit.timeit(setup = setup_code_rainbowIa_classic, stmt = statement_rainbowIa_classic, number = iters)/iters * sec_to_ms

print('Running' + '.' *dot_index)
dot_index += 1

#Rainbow IIIc Classic
setup_code_rainbowIIIc_classic = """
from pqcrypto.sign.rainbowIIIc_classic import generate_keypair, sign, verify
"""

statement_rainbowIIIc_classic  = """
public_key, secret_key = generate_keypair()
"""

rarainbowIIIc_classic_keygen_time = timeit.timeit(setup = setup_code_rainbowIIIc_classic, stmt = statement_rainbowIIIc_classic, number = iters)/iters * sec_to_ms

###
#Rainbow Vc Classic
setup_code_rainbowVc_classic = """
from pqcrypto.sign.rainbowVc_classic import generate_keypair, sign, verify
"""

statement_rainbowVc_classic  = """
public_key, secret_key = generate_keypair()
"""

rarainbowVc_classic_keygen_time = timeit.timeit(setup = setup_code_rainbowVc_classic, stmt = statement_rainbowVc_classic, number = iters)/iters * sec_to_ms

### Rainbow Circumstentials

#Rainbow Ic Circumstential
setup_code_rainbowIa_circumstential = """
from pqcrypto.sign.rainbowIa_cyclic import generate_keypair, sign, verify
"""

statement_rainbowIa_circumstential  = """
public_key, secret_key = generate_keypair()
"""

rainbowIa_circumstential_keygen_time = timeit.timeit(setup = setup_code_rainbowIa_circumstential, stmt = statement_rainbowIa_circumstential, number = iters)/iters * sec_to_ms

#Rainbow IIIc Circumstential
setup_code_rainbowIIIc_circumstential = """
from pqcrypto.sign.rainbowIIIc_cyclic import generate_keypair, sign, verify
"""

statement_rainbowIIIc_circumstential  = """
public_key, secret_key = generate_keypair()
"""

rainbowIIIc_circumstential_keygen_time = timeit.timeit(setup = setup_code_rainbowIIIc_circumstential, stmt = statement_rainbowIIIc_circumstential, number = iters)/iters * sec_to_ms


#Rainbow Vc Circumstential
setup_code_rainbowVc_circumstential = """
from pqcrypto.sign.rainbowVc_cyclic import generate_keypair, sign, verify
"""

statement_rainbowVc_circumstential  = """
public_key, secret_key = generate_keypair()
"""

rainbowVc_circumstential_keygen_time = timeit.timeit(setup = setup_code_rainbowVc_circumstential, stmt = statement_rainbowVc_circumstential, number = iters)/iters * sec_to_ms


#Rainbow Ia Compressed
setup_code_rainbowIa_compressed = """
from pqcrypto.sign.rainbowIa_cyclic_compressed import generate_keypair, sign, verify
"""

statement_rainbowIa_compressed  = """
public_key, secret_key = generate_keypair()
"""

rainbowIa_compressed_keygen_time = timeit.timeit(setup = setup_code_rainbowIa_compressed, stmt = statement_rainbowIa_compressed, number = iters)/iters * sec_to_ms

#Rainbow IIIc Compressed
setup_code_rainbowIIIc_compressed = """
from pqcrypto.sign.rainbowIIIc_cyclic_compressed import generate_keypair, sign, verify
"""

statement_rainbowIIIc_compressed  = """
public_key, secret_key = generate_keypair()
"""

rainbowIIIc_compressed_keygen_time = timeit.timeit(setup = setup_code_rainbowIIIc_compressed, stmt = statement_rainbowIIIc_compressed, number = iters)/iters * sec_to_ms

#Rainbow Vc Compressed
setup_code_rainbowVc_compressed = """
from pqcrypto.sign.rainbowVc_cyclic_compressed import generate_keypair, sign, verify
"""

statement_rainbowVc_compressed  = """
public_key, secret_key = generate_keypair()
"""

rainbowVc_compressed_keygen_time = timeit.timeit(setup = setup_code_rainbowVc_compressed, stmt = statement_rainbowVc_compressed, number = iters)/iters * sec_to_ms


fig, ax = plt.subplots() 
# ax.plot([897, 1793], [falcon512_keygen_time, falcon1024_keygen_time], label='Flacon', marker='s') 
# ax.plot([1184, 1472, 1760], [dilithium2_keygen_time, dilithium3_keygen_time, dilithium4_keygen_time], label='Dilithium', marker='s')  #
# ax.plot([32, 130], [ecdsa_keygen_time, ecdsa_keygen_time521], label='ECDSA', marker='s')  #


# ax.plot([148992, 710640, 1705536], [rainbowIa_classic_keygen_time, rarainbowIIIc_classic_keygen_time, rarainbowVc_classic_keygen_time], label='Rainbow Classic', marker='s')  #
# ax.plot([58144, 206744, 491936], [rainbowIa_circumstential_keygen_time, rainbowIIIc_circumstential_keygen_time, rainbowVc_circumstential_keygen_time], label='Rainbow Cyclic', marker='s')  
# ax.plot([58144, 206744, 491936], [rainbowIa_compressed_keygen_time, rainbowIIIc_compressed_keygen_time, rainbowVc_compressed_keygen_time], label='Rainbow Compressed', marker='s')  

print('Classic Times', [rainbowIa_classic_keygen_time, rarainbowIIIc_classic_keygen_time, rarainbowVc_classic_keygen_time])
print('Cyclic Times', [rainbowIa_circumstential_keygen_time, rainbowIIIc_circumstential_keygen_time, rainbowVc_circumstential_keygen_time])
print('Compressed Times', [rainbowIa_compressed_keygen_time, rainbowIIIc_compressed_keygen_time, rainbowVc_compressed_keygen_time])

# print('Falcon Times', [falcon512_keygen_time, falcon1024_keygen_time])
# print('Dilithium Times', [dilithium2_keygen_time, dilithium3_keygen_time, dilithium4_keygen_time])
# print('ECDSA Times', [ecdsa_keygen_time, ecdsa_keygen_time521])

x = ['Rainbow-Classic-I', 'Rainbow-Classic-III', 'Rainbow-Classic-V', 'Rainbow-Cyclic-I', 'Rainbow-Cyclic-III', 'Rainbow-Cyclic-V', 'Rainbow-Compressed-I', 'Rainbow-Compressed-III', 'Rainbow-Compressed-V']
energy = [rainbowIa_classic_keygen_time, rarainbowIIIc_classic_keygen_time, rarainbowVc_classic_keygen_time, rainbowIa_circumstential_keygen_time, rainbowIIIc_circumstential_keygen_time, rainbowVc_circumstential_keygen_time, rainbowIa_compressed_keygen_time, rainbowIIIc_compressed_keygen_time, rainbowVc_compressed_keygen_time]

x_pos = [i for i, _ in enumerate(x)]

plt.barh(x, energy, color='blue')
plt.xlabel("Algorithm Types")
plt.ylabel("CPU Time (ms)")
plt.title("Digital Signature Algorithm - Rainbow - Key Generation Time (Over The Average of 100 Iterations)".format(iters))

#plt.xticks(x_pos, x)

# ax.set_xlabel('Public Key Size (bytes)')  
# ax.set_ylabel('CPU Time (ms)')  
# ax.set_title("Digital Signature Schemes - Verification Performance by Key Size (Over The Average of 100 Iterations)")  
# ax.legend()  
plt.show()
"""
print(f"Execution time is falcon: {w}")
print('sdsd')
# Alice generates a (public, secret) key pair
start_time = time.process_time() 
public_key, secret_key = generate_keypair()
end_time = time.process_time() 
print('Between', end_time - start_time)

start_time = time.time() 
public_key, secret_key = generate_keypair()
end_time = time.time() 
print('Between', end_time - start_time)
#print('PK:', public_key.hex())
# Alice signs her message using her secret key
signature = sign(secret_key, b"Hello world")
print(psutil.virtual_memory())
# Bob uses Alice's public key to validate her signature
print(verify(public_key, b"Hello world", signature))
"""

"""
# from pqcrypto.sign.rainbowIa_classic import generate_keypair, sign, verify
# from pqcrypto.sign.rainbowIa_cyclic import generate_keypair, sign, verify
# from pqcrypto.sign.rainbowIa_cyclic_compressed import generate_keypair, sign, verify
# from pqcrypto.sign.rainbowIIIc_classic import generate_keypair, sign, verify
# from pqcrypto.sign.rainbowIIIc_cyclic import generate_keypair, sign, verify
# from pqcrypto.sign.rainbowIIIc_cyclic_compressed import generate_keypair, sign, verify
# from pqcrypto.sign.rainbowVc_classic import generate_keypair, sign, verify
# from pqcrypto.sign.rainbowVc_cyclic import generate_keypair, sign, verify
# from pqcrypto.sign.rainbowVc_cyclic_compressed import generate_keypair, sign, verify
"""


