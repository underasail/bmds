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

abc = (a + b + c)/3

std_1 = np.std([a[0], b[0], c[0]])
std_2 = np.std([a[1], b[1], c[1]])
std_3 = np.std([a[2], b[2], c[2]])
std_4 = np.std([a[3], b[3], c[3]])
std_5 = np.std([a[4], b[4], c[4]])
std_6 = np.std([a[5], b[5], c[5]])
sem = [std_1/3, std_2/3, std_3/3, std_4/3, std_5/3, std_6/3]

N = ((1/7), (2/7), (3/7), (4/7), (5/7), (6/7))

title_font = {'family': 'serif',
              'color':  'black',
              'weight': 'normal',
              'size': 16,
              }
              # Estabilshes font dictionary
other_font = {'family': 'serif',
              'color':  'black',
              'weight': 'normal',
              'size': 14,
              }
ax = plt.gca()

plt.bar(N, abc, yerr = sem, ecolor = 'black', 
        width = 0.1, color = 'white', 
        linewidth = 0.5
        )

plt.title('Thapsigargin Dosage Curve\n', fontdict = title_font)

plt.xticks(N, ('DMSO', '10 nM TG', '100 nM TG', 
               '1 µM TG', '10 µM TG', '1 µM STS'
               ), 
           rotation = 45, size = 12, family = 'serif'
           )
# Sets positioning and text properties for bar chart x-axis
plt.ylabel('Fluorescence Intensity/Minute\n', fontdict = other_font)
ax.spines['right'].set_visible(False)  # Removes right axis
ax.spines['top'].set_visible(False)  # Removes top axis
ax.xaxis.set_ticks_position('none')  # Keeps horizontal ticks hidden
ax.yaxis.set_ticks_position('left')
ax.tick_params(axis = 'y', direction = 'out')  # Positions ticks outside the axis


plt.savefig('C:\\Users\Thompson\Documents\Thapsigargin_Dosgae_Figure.svg', 
            bbox_inches = 'tight', format = 'svg')
plt.show()

