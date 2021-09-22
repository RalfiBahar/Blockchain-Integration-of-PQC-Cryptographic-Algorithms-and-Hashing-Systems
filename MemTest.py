import time
import numpy as np
from concurrent.futures import ProcessPoolExecutor

import pqcrypto.sign.falcon_512 as falcon512
import pqcrypto.sign.falcon_1024 as falcon1024

import pqcrypto.sign.dilithium2 as dilithium2
import pqcrypto.sign.dilithium3 as dilithium3
import pqcrypto.sign.dilithium4 as dilithium5

import pqcrypto.sign.rainbowIa_classic as rainbowIa_classic
import pqcrypto.sign.rainbowIIIc_classic as rainbowIIIc_classic
import pqcrypto.sign.rainbowVc_classic as rainbowVc_classic

import pqcrypto.sign.rainbowIa_cyclic as rainbowIa_cyclic
import pqcrypto.sign.rainbowIIIc_cyclic as rainbowIIIc_cyclic
import pqcrypto.sign.rainbowVc_cyclic as rainbowVc_cyclic

import pqcrypto.sign.rainbowIa_cyclic_compressed as rainbowIa_cyclic_compressed
import pqcrypto.sign.rainbowIIIc_cyclic_compressed as rainbowIIIc_cyclic_compressed
import pqcrypto.sign.rainbowVc_cyclic_compressed as rainbowVc_cyclic_compressed

import ecdsa as ecdsa

######ECDSA
def ecdsa_256():
    sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1) # uses NIST192p
    pk = sk.verifying_key
    return pk, sk

def ecdsa_521():
    sk = ecdsa.SigningKey.generate(curve=ecdsa.NIST521p) # uses NIST192p
    pk = sk.verifying_key
    return pk, sk
######ECDSA

######Falcon
def falcon_512():
    pk, sk = falcon512.generate_keypair()
    return pk, sk

def falcon_1024():
    pk, sk = falcon1024.generate_keypair()
    return pk, sk
######Falcon

######Dilithium
def dilithium_2():
    pk, sk = dilithium2.generate_keypair()
    return pk, sk

def dilithium_3():
    pk, sk = dilithium3.generate_keypair()
    return pk, sk

def dilithium_5():
    pk, sk = dilithium5.generate_keypair()
    return pk, sk
######Dilithium

######Rainbow Classic
def rbow_classic_I():
    pk, sk = rainbowIa_classic.generate_keypair()
    return pk, sk

def rbow_classic_III():
    pk, sk = rainbowIIIc_classic.generate_keypair()
    return pk, sk

def rbow_classic_V():
    pk, sk = rainbowVc_classic.generate_keypair()
    return pk, sk

######Rainbow Cyclic
def rbow_cyclic_I():
    pk, sk = rainbowIa_cyclic.generate_keypair()
    return pk, sk

def rbow_cyclic_III():
    pk, sk = rainbowIIIc_cyclic.generate_keypair()
    return pk, sk

def rbow_cyclic_V():
    pk, sk = rainbowVc_cyclic.generate_keypair()
    return pk, sk

######Rainbow compressed
def rbow_compressed_I():
    pk, sk = rainbowIa_cyclic_compressed.generate_keypair()
    return pk, sk

def rbow_compressed_III():
    pk, sk = rainbowIIIc_cyclic_compressed.generate_keypair()
    return pk, sk

def rbow_compressed_V():
    pk, sk = rainbowVc_cyclic_compressed.generate_keypair()
    return pk, sk

def main_func():
    ppe = ProcessPoolExecutor(max_workers=9)
    futures = []


    futures.append(ppe.submit(rbow_classic_I))
    futures.append(ppe.submit(rbow_classic_III))
    futures.append(ppe.submit(rbow_classic_V))

    futures.append(ppe.submit(rbow_cyclic_I))
    futures.append(ppe.submit(rbow_cyclic_III))
    futures.append(ppe.submit(rbow_cyclic_V))

    futures.append(ppe.submit(rbow_compressed_I))
    futures.append(ppe.submit(rbow_compressed_III))
    futures.append(ppe.submit(rbow_compressed_V))

    #print([future.result() for future in futures])

if __name__ == '__main__':
    main_func()


"""
    futures.append(ppe.submit(ecdsa_256))
    futures.append(ppe.submit(ecdsa_521))

    futures.append(ppe.submit(falcon_512))
    futures.append(ppe.submit(falcon_1024))

    futures.append(ppe.submit(dilithium_2))
    futures.append(ppe.submit(dilithium_3))
    futures.append(ppe.submit(dilithium_5))
"""