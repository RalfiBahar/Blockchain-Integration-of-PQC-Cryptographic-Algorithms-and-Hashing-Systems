import matplotlib.pyplot as plt
from platform import python_version as pythonversion

fig = plt.figure()
ax = fig.add_subplot(111)
y = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1]    
col_labels = ['Key Signing Time (ms)']
row_labels = ['ECDSA-SECP256k1', 'ECDSA-NIST521p', 'Falcon512', 'Falcon1024', 'Dilithium2', 'Dilithium3', 'Dilithium5', 'Rainbow-I-Classic', 'Rainbow-III-Classic', 'Rainbow-V-Classic', 'Rainbow-I-Circumstential', 'Rainbow-III-Circumstential', 'Rainbow-V-Circumstential', 'Rainbow-I-Compressed', 'Rainbow-III-Compressed', 'Rainbow-V-Compressed']
table_vals = [[1.6486860000000103], [4.57809000000009], [7.644203000000017], [20.097521999999927], [1.397686000000121], [0.984400999999858], [1.095541999999952], burdan[300.51123069999994], [2266.7080882], [6665.577128700001], [224.44366619999983], [2357.816755499999], [7536.788909699999], [221.7048319000014], [2347.0908902999977], [7512.408633299998]]

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
plt.savefig('matplotlib-table-keygen.png', bbox_inches='tight', pad_inches=0.05)