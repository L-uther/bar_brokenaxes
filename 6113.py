import matplotlib.pyplot as plt
import numpy as np
from brokenaxes import brokenaxes

categories = ['Celegans', 'Email', 'USAir', 'HEP']
lphn_values = [0.633, 0.779, 0.812, 0.779]
phln_values = [0.854, 0.913, 0.934, 0.857]
lphn_errors = [0.0021, 0.0025, 0.0033, 0.0038]
phln_errors = [0.007, 0.0055, 0.0049, 0.0086]


pos = np.arange(len(categories))
bar_width = 0.35

plt.figure
plt.bar(pos - bar_width/2, lphn_values, bar_width, yerr=lphn_errors, capsize=5, color='blue', label='LPHN')
plt.bar(pos + bar_width/2, phln_values, bar_width, yerr=phln_errors, capsize=5, color='orange', label='PHLN')
plt.axis('off')

bax = brokenaxes(ylims=((0.00, 0.20), (0.60, 1.15)), hspace=.2, despine=False,diag_color="r")

bax.bar(pos - bar_width/2, lphn_values, bar_width, yerr=lphn_errors, capsize=5, color='blue', label='LPHN')
bax.bar(pos + bar_width/2, phln_values, bar_width, yerr=phln_errors, capsize=5, color='orange', label='PHLN')

bax.legend()
bax.set_xlabel('Categories')
bax.set_ylabel('AUC')
bax.set_title('5:5 (Division Ratio)')
bax.set_xticks(pos,categories)
print(pos)


for i, (l, p) in enumerate(zip(lphn_values, phln_values)):
    bax.text(pos[i] - bar_width/2, l + 0.01, f'{l:.3f}', ha='center')
    bax.text(pos[i] + bar_width/2, p + 0.01, f'{p:.3f}', ha='center')


#plt.tight_layout()
plt.show()