import numpy as np
from matplotlib import pyplot as plt

c = np.array([8.19336852829490, 18.23063814022410, 
              91.30003704732790, 143.44258590349200, 
              175.32458090210200, 339.95221820876200])
b = np.array([16.24345651569880, 17.89030286190610, 
              97.19055293136980, 103.68099472075600, 
              125.14237288135600, 233.47248309715700])
a = np.array([14.96148930258410, 15.76298045753450, 
              96.19055293136990, 98.19137723441700,
              120.69264610540000, 231.40199129387800])

a = a/20  # Per µg instead of 20µg
b = b/20
c = c/20

abc = (a + b + c)/3

std_1 = np.std([a[0], b[0], c[0]])
std_2 = np.std([a[1], b[1], c[1]])
std_3 = np.std([a[2], b[2], c[2]])
std_4 = np.std([a[3], b[3], c[3]])
std_5 = np.std([a[4], b[4], c[4]])
std_6 = np.std([a[5], b[5], c[5]])
sem = [std_1/3, std_2/3, std_3/3, std_4/3, std_5/3, std_6/3]

N = [(1/7), (2/7), (3/7), (4/7), (5/7), (6/7)]
M = [(1/7) + 0.05, (2/7) + 0.05, (3/7) + 0.05, 
     (4/7) + 0.05, (5/7) + 0.05, (6/7) + 0.05]


title_font = {'family': 'serif',
              'color':  'black',
              'weight': 'normal',
              'size': 16,
              }
              # Estabilshes font dictionary
other_font = {'family': 'serif',
              'color':  'black',
              'weight': 'normal',
              'size': 12,
              }
ax = plt.subplot(5, 1, (1, 4))

plt.bar(N, abc, yerr = sem, ecolor = 'black', 
        width = 0.1, color = ['white', 'lightgrey', 'lightgrey', 
        'lightgrey', 'lightgrey', 'darkgrey'], linewidth = 0.5
        )

# plt.title('Thapsigargin Dosage Curve\n', fontdict = title_font)

plt.xticks(M, ('Control', '0.01', '0.1', '1', '10', '1'), 
           rotation = 0, size = 12, family = 'serif'
           )
# Sets positioning and text properties for bar chart x-axis
plt.ylabel('Caspase-3 Activity\n(∆F/µg/min)', fontdict = other_font)
ax.spines['right'].set_visible(False)  # Removes right axis
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('none')  # Keeps horizontal ticks hidden
ax.yaxis.set_ticks_position('left')
ax.tick_params(axis = 'y', direction = 'out')  # Positions ticks outside the axis


ax = plt.subplot(6, 1, 6)

plt.text(0.108333334, 93, 'DMSO', horizontalalignment = 'center', 
      fontsize = 12, family = 'serif')
         
plt.axhline(100, color = 'black', xmin = 0.05, xmax = 0.1666666667)

plt.text(0.5, 93, '[TG] (µM)', horizontalalignment = 'center', 
      fontsize = 12, family = 'serif')
         
plt.axhline(100, color = 'black', xmin = 0.210714286, xmax = 0.789285714)

plt.text(0.8571428571428571 + 0.05, 93, '[STS] (µM)', horizontalalignment = 'center', 
      fontsize = 12, family = 'serif')
         
plt.axhline(100, color = 'black', xmin = 0.789285714 + 0.05, xmax = 0.789285714 + 0.05 + 0.12)

ax.spines['right'].set_visible(False)  # Removes right axis
ax.spines['top'].set_visible(False)  # Removes top axis
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.xaxis.set_ticks_position('none')  # Keeps horizontal ticks hidden
ax.yaxis.set_ticks_position('none')
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.savefig('C:\\Users\Thompson\Documents\Thapsigargin_Dosgae_Figure.svg', 
            bbox_inches = 'tight', format = 'svg')
plt.show()

