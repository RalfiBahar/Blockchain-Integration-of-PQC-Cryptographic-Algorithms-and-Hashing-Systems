from memory_profiler import profile
from math import factorial
import pqcrypto.sign.falcon_512 as falcon512
import pqcrypto.sign.falcon_1024 as falcon1024
import pqcrypto.sign.dilithium3 as dilithium3
import pqcrypto.sign.dilithium4 as dilithium4
import pqcrypto.sign.rainbowIa_classic as rainbowIa_classic
import pqcrypto.sign.rainbowIIIc_classic as rainbowIIIc_classic
import time

@profile
def falcon_512():
    falcon512.generate_keypair()

@profile
def falcon_1024():
    pk, sk = falcon1024.generate_keypair()

@profile
def dilithium_3():
    pk, sk = dilithium3.generate_keypair()

@profile
def dilithium_4():
    pk, sk = dilithium4.generate_keypair()

@profile
def rainbow_Ia_classic():
    pk, sk = rainbowIa_classic.generate_keypair()

@profile
def rainbow_IIIc_classic():
    pk, sk = rainbowIIIc_classic.generate_keypair()

if __name__ == "__main__":
    falcon_512() #done
    # falcon_1024() #done
    # dilithium_3() #done
    # dilithium_4() #done
    # rainbow_Ia_classic() #done
    #rainbow_IIIc_classic() #done