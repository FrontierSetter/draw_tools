import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(9,6))
plt.grid(True, linestyle='-.', axis='y')

bar_width = 0.3
curP = plt.bar([0,1], [1.56, 1], bar_width, color='#1F497D')

plt.ylabel('normalized average\ndefective product risk', fontsize=28)

# plt.yticks(range(0, 26, 5), range(0, 26, 5), fontsize=22)
plt.yticks(fontsize=26)
plt.xticks([0,1], ['7 fixed loop', '15 fixed loop'], fontsize=26)
# plt.xlabel('time cost', fontsize=26)

plt.text(0, 1.61, "1.56", fontsize=24, ha = 'center',va = 'bottom')
plt.text(1, 1.05, "1", fontsize=24, ha = 'center',va = 'bottom')

plt.xlim(-0.5, 1.5)
plt.ylim(0, 2.05)
plt.subplots_adjust(left=0.195, right=0.99, top=0.975, bottom=0.095)

plt.savefig('defective_2.pdf')
plt.show()