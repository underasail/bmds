from matplotlib_venn import venn3
from matplotlib import pyplot as plt

plt.figure(figsize = (5, 5))
venn3(subsets = (69, 93, 43, 103, 25, 40, 24), 
      set_labels = ('$\it{M. persicae}$, current', 
                    '$\it{M. persicae}$, prior', 
                    '$\it{A. pisum}$, prior')
      )

#      Set1                      Set2
# +-------------+-----------+-------------+
# |             |           |             |
# |             |           |             |
# |     1       |     3     |      2      |
# |             |           |             |
# |       +-----------------------+       |
# |       |     |           |     |       |
# |       |  5  |     7     |  6  |       |
# |       |     |           |     |       |
# +-------------+-----------+-------------+
#         |                       |
#         |                       |
#         |           4           |
#         |                       |
#         |                       |
#         +-----------------------+
#                   Set3



plt.savefig('C:\\Users\Thompson\Documents\Figure_2_miRNA_Venn.svg', 
            bbox_inches = 'tight', format = 'svg')
plt.show()