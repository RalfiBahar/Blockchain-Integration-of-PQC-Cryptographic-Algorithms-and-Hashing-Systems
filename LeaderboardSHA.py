import matplotlib.pyplot as plt
from platform import python_version as pythonversion

fig = plt.figure()
ax = fig.add_subplot(111)
col_labels = ['General Leaderboard', 'Cryptocurrency', 'Medical Records', 'E-Voting']
row_labels = ['1st Place', '2nd Place']
table_vals = [['SHA3-512', 'SHA3-512', 'SHA3-512', 'SHA3-512'], ['SHA2-256', 'SHA2-256', 'SHA2-256', 'SHA2-256']]

the_table = plt.table(cellText=table_vals,
                      colWidths=[0.08] * 4,
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
plt.savefig('matplotlib-table-leaderboard-sha.png', bbox_inches='tight', pad_inches=0.05)