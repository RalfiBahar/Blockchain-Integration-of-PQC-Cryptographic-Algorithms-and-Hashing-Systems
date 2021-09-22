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

import ecdsa  as ecdsa256

import matplotlib.pyplot as plt
import numpy as np
import sys

def utf8len(s):
    return len(s)

hash = bytes.fromhex("3e580a819609b7d0ec628d6be3e0ea9928f3c952777118a46ce81271ef556fa64625df47e1d9b6d048562108b55b7c04d3138753a3878078de5e5d45bf0429d5")

ecdsa256_sk = ecdsa256.SigningKey.generate(curve=ecdsa256.SECP256k1)
ecdsa256_pk = ecdsa256_sk.verifying_key
ecdsa256_sig = ecdsa256_sk.sign(hash)
print(len(ecdsa256_sk.to_string()), len(ecdsa256_pk.to_string()), utf8len(ecdsa256_sig))

ecdsa512_sk = ecdsa256.SigningKey.generate(curve=ecdsa256.NIST521p)
ecdsa512_pk = ecdsa256_sk.verifying_key
ecdsa512_sig = ecdsa256_sk.sign(hash)
print(len(ecdsa512_sk.to_string()), len(ecdsa512_pk.to_string()), utf8len(ecdsa512_sig))


falcon512_pk, falcon512_sk = falcon512.generate_keypair()
falcon512_signature = falcon512.sign(falcon512_sk, hash)

falcon1024_pk, falcon1024_sk = falcon1024.generate_keypair()
falcon1024_signature = falcon1024.sign(falcon1024_sk, hash)

#######
dilithium2_pk, dilithium2_sk = dilithium2.generate_keypair()
dilithium2_signature = dilithium2.sign(dilithium2_sk, hash)

dilithium3_pk, dilithium3_sk = dilithium3.generate_keypair()
dilithium3_signature = dilithium3.sign(dilithium3_sk, hash)

dilithium5_pk, dilithium5_sk = dilithium5.generate_keypair()
dilithium5_signature = dilithium5.sign(dilithium5_sk, hash)
#######

#######
rainbowIa_classic_pk, rainbowIa_classic_sk = rainbowIa_classic.generate_keypair()
rainbowIa_classic_signature = rainbowIa_classic.sign(rainbowIa_classic_sk, hash)

rainbowIIIc_classic_pk, rainbowIIIc_classic_sk = rainbowIIIc_classic.generate_keypair()
rainbowIIIc_classic_signature = rainbowIIIc_classic.sign(rainbowIIIc_classic_sk, hash)

rainbowVc_classic_pk, rainbowVc_classic_sk = rainbowVc_classic.generate_keypair()
rainbowVc_classic_signature = rainbowVc_classic.sign(rainbowVc_classic_sk, hash)
#######

#######
rainbowIa_circum_pk, rainbowIa_circum_sk = rainbowIa_cyclic.generate_keypair()
rainbowIa_circum_signature = rainbowIa_cyclic.sign(rainbowIa_circum_sk, hash)

rainbowIIIc_circum_pk, rainbowIIIc_circum_sk = rainbowIIIc_cyclic.generate_keypair()
rainbowIIIc_circum_signature = rainbowIIIc_cyclic.sign(rainbowIIIc_circum_sk, hash)

rainbowVc_circum_pk, rainbowVc_circum_sk = rainbowVc_cyclic.generate_keypair()
rainbowVc_circum_signature = rainbowVc_cyclic.sign(rainbowVc_circum_sk, hash)
#######

#######
rainbowIa_compressed_pk, rainbowIa_compressed_sk = rainbowIa_cyclic_compressed.generate_keypair()
rainbowIa_compressed_signature = rainbowIa_cyclic_compressed.sign(rainbowIa_compressed_sk, hash)

rainbowIIIc_compressed_pk, rainbowIIIc_compressed_sk = rainbowIIIc_cyclic_compressed.generate_keypair()
rainbowIIIc_compressed_signature = rainbowIIIc_cyclic_compressed.sign(rainbowIIIc_compressed_sk, hash)

rainbowVc_compressed_pk, rainbowVc_compressed_sk = rainbowVc_cyclic_compressed.generate_keypair()
rainbowVc_compressed_signature = rainbowVc_cyclic_compressed.sign(rainbowVc_compressed_sk, hash)
#######

print('Public Keys', [utf8len(falcon512_pk), utf8len(falcon1024_pk), utf8len(dilithium2_pk), utf8len(dilithium3_pk), utf8len(dilithium5_pk), utf8len(rainbowIa_classic_pk), utf8len(rainbowIIIc_classic_pk), utf8len(rainbowVc_classic_pk), utf8len(rainbowIa_circum_pk), utf8len(rainbowIIIc_circum_pk), utf8len(rainbowVc_circum_pk), utf8len(rainbowIa_compressed_pk), utf8len(rainbowIIIc_compressed_pk), utf8len(rainbowVc_compressed_pk)])
print('Private Keys', [utf8len(falcon512_sk), utf8len(falcon1024_sk), utf8len(dilithium2_sk), utf8len(dilithium3_sk), utf8len(dilithium5_sk), utf8len(rainbowIa_classic_sk), utf8len(rainbowIIIc_classic_sk), utf8len(rainbowVc_classic_sk), utf8len(rainbowIa_circum_sk), utf8len(rainbowIIIc_circum_sk), utf8len(rainbowVc_circum_sk), utf8len(rainbowIa_compressed_sk), utf8len(rainbowIIIc_compressed_sk), utf8len(rainbowVc_compressed_sk)])
print('Signatures', [utf8len(falcon512_signature), utf8len(falcon1024_signature), utf8len(dilithium2_signature), utf8len(dilithium3_signature), utf8len(dilithium5_signature), utf8len(rainbowIa_classic_signature), utf8len(rainbowIIIc_classic_signature), utf8len(rainbowVc_classic_signature), utf8len(rainbowIa_circum_signature), utf8len(rainbowIIIc_circum_signature), utf8len(rainbowVc_circum_signature), utf8len(rainbowIa_compressed_signature), utf8len(rainbowIIIc_compressed_signature), utf8len(rainbowVc_compressed_signature)])

"""
labels = ['Falcon512', 'Falcon 1024', 'Dilithium 3', 'Dilithium 5', 'Rainbow Ia Classic', 'Rainbow IIIc Classic']
left_means = [utf8len(falcon512_pk), utf8len(falcon1024_pk), utf8len(dilithium3_pk), utf8len(dilithium5_pk), utf8len(rainbowIa_classic_pk), utf8len(rainbowIIIc_classic_pk)]
right_means = [utf8len(falcon512_signatrue), utf8len(falcon1024_signature), utf8len(dilithium3_signature), utf8len(dilithium5_signature), utf8len(rainbowIa_classic_signature), utf8len(rainbowIIIc_classic_signature)]

x = np.arange(len(labels))  # the label locations
width = 0.35  # 0.35 the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, left_means, width, label='Public Key Size')
rects2 = ax.bar(x + width/2, right_means, width, label='Signature Size')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Size (bytes)')
ax.set_title('Public Key and Signature Sizes of NIST Post-Quantum Cryptography Finalists')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()

print('ECDSA256 Public', ecdsa256_pk)
print('ECDSA256 Private', ecdsa256_sk)
print('ECDSA256 Sig', utf8len(ecdsa256_sig))

"""