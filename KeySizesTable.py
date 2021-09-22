import matplotlib.pyplot as plt
from platform import python_version as pythonversion

fig = plt.figure()
ax = fig.add_subplot(111)
y = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1]    
col_labels = ['Public Key', 'Private Key', 'Signature']
row_labels = ['ECDSA-SECP256k1', 'ECDSA-NIST521p', 'Falcon512', 'Falcon1024', 'Dilithium2', 'Dilithium3', 'Dilithium5', 'Rainbow-I-Classic', 'Rainbow-III-Classic', 'Rainbow-V-Classic', 'Rainbow-I-Circumstential', 'Rainbow-III-Circumstential', 'Rainbow-V-Circumstential', 'Rainbow-I-Compressed', 'Rainbow-III-Compressed', 'Rainbow-V-Compressed']
table_vals = [[64, 32, 64], [64, 66, 64], [897, 1281, 655], [1793, 2305, 1275], [1184, 2800, 2044], [1472, 3504, 2701], [1760, 3856, 3366], [148992, 92960, 64], [710640, 511448, 156], [1705536, 1227104, 204], [58144, 92960, 64], [206744, 511448, 156], [491936, 1227104, 204], [58144, 64, 64], [206744, 64, 156], [491936, 64, 204]]

# ax.plot([92960, 511448, 1227104], [rainbowIa_classic_sig_time, rarainbowIIIc_classic_sig_time, rarainbowVc_classic_sig_time], label='Rainbow Classic', marker='s')  #
# ax.plot([92960, 511448, 1227104], [rainbowIa_circumstential_sig_time, rainbowIIIc_circumstential_sig_time, rainbowVc_circumstential_sig_time], label='Rainbow Cyclic', marker='s')  
# ax.plot([92960, 511448, 1227104], [rainbowIa_compressed_sig_time, rainbowIIIc_compressed_sig_time, rainbowVc_compressed_sig_time], label='Rainbow Compressed', marker='s')  

# Draw table
the_table = plt.table(cellText=table_vals,
                      colWidths=[0.1] * 3,
                      rowLabels=row_labels,
                      colLabels=col_labels,
                      loc='center')
the_table.auto_set_font_size(False)
the_table.set_fontsize(24)
the_table.scale(4, 4)

# Removing ticks and spines enables you to get the figure only with table
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.tick_params(axis='y', which='both', right=False, left=False, labelleft=False)
for pos in ['right','top','bottom','left']:
    plt.gca().spines[pos].set_visible(False)
plt.savefig('matplotlib-table.png', bbox_inches='tight', pad_inches=0.05)