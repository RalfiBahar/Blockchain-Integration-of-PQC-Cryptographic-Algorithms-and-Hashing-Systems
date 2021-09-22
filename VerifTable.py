import matplotlib.pyplot as plt
from platform import python_version as pythonversion

fig = plt.figure()
ax = fig.add_subplot(111)
y = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1]    
col_labels = ['Key Verification Time (ms)']
row_labels = ['ECDSA-SECP256k1', 'ECDSA-NIST521p', 'Falcon512', 'Falcon1024', 'Dilithium2', 'Dilithium3', 'Dilithium5', 'Rainbow-I-Classic', 'Rainbow-III-Classic', 'Rainbow-V-Classic', 'Rainbow-I-Circumstential', 'Rainbow-III-Circumstential', 'Rainbow-V-Circumstential', 'Rainbow-I-Compressed', 'Rainbow-III-Compressed', 'Rainbow-V-Compressed']
table_vals = [[5.056494259999997], [22.143031200000003], [0.06393447999999857], [0.16066029000000093], [0.15849470000000032], [0.20037821999999927], [0.1754375400000064], [3.019397999999951], [46.9690319999998], [49.84640099999993], [11.755331999999896], [54.8433060000022], [117.60175299999887], [8.898195000000442], [59.49718900000178], [107.95891200000085]]

the_table = plt.table(cellText=table_vals,
                      colWidths=[0.1] * 3,
                      rowLabels=row_labels,
                      colLabels=col_labels,
                      loc='center')
the_table.auto_set_font_size(False)
the_table.set_fontsize(24)
the_table.scale(10, 4)

plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.tick_params(axis='y', which='both', right=False, left=False, labelleft=False)
for pos in ['right','top','bottom','left']:
    plt.gca().spines[pos].set_visible(False)
plt.savefig('matplotlib-table-verif.png', bbox_inches='tight', pad_inches=0.05)