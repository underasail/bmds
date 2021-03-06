#! /usr/bin/python3

import csv
import numpy as np
from matplotlib import pyplot as plt

gut_data_plant = {}
bac_data_plant = {}

with open('other-bacteria_percents.txt', 'r') as f:
    csvreader = csv.reader(f, delimiter = '\t')
    for row in csvreader:
        if len(row) == 1:
            dataset = row[0]
            total = float(next(csvreader)[2])
            abp = float(next(csvreader)[2])
            ap = float(next(csvreader)[2])
            ab = float(next(csvreader)[2])
            bp = float(next(csvreader)[2])
            aphid = float(next(csvreader)[2])
            buchnera = float(next(csvreader)[2])
            plant = float(next(csvreader)[2])
            ob_ex = float(next(csvreader)[2])
            Ps_ex = float(next(csvreader)[2])
            CRi_ex = float(next(csvreader)[2])
            Cn_ex = float(next(csvreader)[2])
            Pd_ex = float(next(csvreader)[2])
            Hd_ex = float(next(csvreader)[2])
            Ss_ex = float(next(csvreader)[2])
            Ph_ex = float(next(csvreader)[2])
            Al_ex = float(next(csvreader)[2])
            Pa_ex = float(next(csvreader)[2])
            Ea_ex = float(next(csvreader)[2])
            other_bacteria = ob_ex + Ps_ex + Cn_ex + Pd_ex + Hd_ex + Ss_ex + Ph_ex + Al_ex + Pa_ex + Ea_ex
            if dataset == 'G002 Gut':
                gut_data_plant['abp'] = abp/90321.98
                gut_data_plant['ap'] = ap/90321.98
                gut_data_plant['ab'] = ab/90321.98
                gut_data_plant['bp'] = bp/90321.98
                gut_data_plant['aphid'] = aphid/90321.98
                gut_data_plant['buchnera'] = buchnera/90321.98
                gut_data_plant['plant'] = plant/90321.98
                gut_data_plant['other_bacteria'] = other_bacteria/90321.98
                gut_data_plant['CRi'] = CRi_ex/90321.98
                gut_data_plant['unknown'] = (9032198 - abp - ap - ab - bp - aphid - buchnera - plant - other_bacteria - CRi_ex)/90321.98
            elif dataset == 'G002 Bacteriome':
                bac_data_plant['abp'] = abp/120857.42
                bac_data_plant['ap'] = ap/120857.42
                bac_data_plant['ab'] = ab/120857.42
                bac_data_plant['bp'] = bp/120857.42
                bac_data_plant['aphid'] = aphid/120857.42
                bac_data_plant['buchnera'] = buchnera/120857.42
                bac_data_plant['plant'] = plant/120857.42
                bac_data_plant['other_bacteria'] = other_bacteria/120857.42
                bac_data_plant['CRi'] = CRi_ex/120857.42
                bac_data_plant['unknown'] = (12085742 - abp - ap - ab - bp - aphid - buchnera - plant - other_bacteria - CRi_ex)/120857.42
            else:
                pass
        else:
            pass

for key in gut_data_plant.keys():
    if gut_data_plant[key] < 1:
        gut_data_plant[key] = 0
    else:
        pass
    if bac_data_plant[key] < 1:
        bac_data_plant[key] = 0
    else:
        pass
    
#%%
################
# Data Storage #
################

gut_data = {}
gut_data['nonholobiont'] = (gut_data_plant['unknown'] + gut_data_plant['plant'] + gut_data_plant['other_bacteria'] + gut_data_plant['CRi'])
gut_data['holobiont'] = 100 - gut_data['nonholobiont']

bac_data = {}
bac_data['nonholobiont'] = (bac_data_plant['unknown'] + bac_data_plant['plant'] + bac_data_plant['other_bacteria'] + bac_data_plant['CRi'])
bac_data['holobiont'] = 100 - bac_data['nonholobiont']



###################
# Data Formatting #
###################

p_aphid = (gut_data_plant['aphid'], bac_data_plant['aphid'])
p_aphid = np.array(p_aphid)
p_buchnera = (gut_data_plant['buchnera'], bac_data_plant['buchnera'])
p_buchnera = np.array(p_buchnera)
p_plant = (gut_data_plant['plant'], bac_data_plant['plant'])
p_plant = np.array(p_plant)
p_unknown = (gut_data_plant['unknown'], bac_data_plant['unknown'])
p_unknown = np.array(p_unknown)
p_ab = (gut_data_plant['ab'], bac_data_plant['ab'])
p_ab = np.array(p_ab)
p_ap = (gut_data_plant['ap'], bac_data_plant['ap'])
p_ap = np.array(p_ap)
p_bp = (gut_data_plant['bp'], bac_data_plant['bp'])
p_bp = np.array(p_bp)
p_abp = (gut_data_plant['abp'], bac_data_plant['abp'])
p_abp = np.array(p_abp)
p_other_bacteria = (gut_data_plant['other_bacteria'], bac_data_plant['other_bacteria'])
p_other_bacteria = np.array(p_other_bacteria)
p_CRi = (gut_data_plant['CRi'], bac_data_plant['CRi'])
p_CRi = np.array(p_CRi)
# With plant data set-up


##############################
# MatPlotLib Initializations #
##############################

N = (0.75, 0.05)  # Positioning of bar plots for panel b

title_font = {'family': 'sans-serif',
              'color':  'black',
              'weight': 'normal',
              'size': 16,
              }
              # Estabilshes font dictionary
other_font = {'family': 'sans-serif',
              'color':  'black',
              'weight': 'normal',
              'size': 14,
              }
              
sizes_gut = [gut_data['nonholobiont'], 
             gut_data['holobiont']]
             # Sets up data for pie charts
sizes_gut.reverse()  # To allow legend to be in the correct order

sizes_bac = [bac_data['nonholobiont'], 
             bac_data['holobiont']]
sizes_bac.reverse()

colors = ['steelblue', 'darkorange']  # Sets up colors for pie charts
labels = ['Mapped', 'Not Mapped']

data_list = [p_aphid, p_buchnera, p_ab, p_plant, p_ap, p_bp, p_abp, p_CRi, p_other_bacteria, p_unknown]
string_list = ['p_aphid_plot', 'p_buchnera_plot', 'p_ab_plot', 'p_plant_plot', 
               'p_ap_plot', 'p_bp_plot', 'p_abp_plot', 'p_CRi', 'p_other_bacteria', 'p_unknown_plot']
               # Keeps names the same as before for loop
               # Allows a dictionary to be created with these as the keys 
               # and then save bar chart characteristics under them for legend 
               # generation
string_dict = {}
color_list = ['maroon', 'red', 'lightsalmon', 
              'darkgreen', 'darkgoldenrod', 
              'gold', 'c', 'mediumvioletred', 
              'violet', 'darkorchid']
left = 0

#####################
# Subplot Structure #
#####################

     ###########
     # a1 # bb #
     ###### bb #
     # a2 # bb #
     ###########
     
plt.subplots(2, 2, figsize = (10, 5))

#######################
# Panel A: Pie Charts #
#######################

plt.subplot(2, 3, 1) # Rows, Columns, Position
plt.pie(sizes_gut, colors = colors, autopct = '%1.1f%%',
        shadow = False, startangle = 90, wedgeprops = {'linewidth': 0}, 
        pctdistance=0.50)

plt.title('Holobiont Mapping\n', fontdict = title_font) # Acts as panel title
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


plt.subplot(2, 3, 4)
plt.pie(sizes_bac, colors = colors, autopct = '%1.1f%%',
        shadow = False, startangle = 16.74, wedgeprops = {'linewidth': 0}, 
        pctdistance=0.50)
        

plt.legend(labels, loc = 'upper left', bbox_to_anchor = (-0.35, -0.445), 
           prop = {'family' : 'sans-serif', 'size' : 12}, frameon = False)
plt.axis('equal')


#######################
# Panel B: Bar Charts #
#######################

ax = plt.subplot(1, 3, (2, 3))
# Sets up ax for later proptery manipulations of ticks

for data, string, color in zip(data_list, string_list, color_list):
    string_dict[string] = ax.barh(N, data, color = color, left = left, 
                                  height = 0.55, linewidth = 0)
    left += data
    
plt.title('Extra-holobiont Mapping\n', fontdict = title_font)
plt.legend((string_dict['p_aphid_plot'][0], string_dict['p_buchnera_plot'][0], 
            string_dict['p_ab_plot'][0], 
            string_dict['p_CRi'][0], string_dict['p_other_bacteria'][0],
            string_dict['p_plant_plot'][0], string_dict['p_ap_plot'][0], 
            string_dict['p_bp_plot'][0], string_dict['p_abp_plot'][0], 
            string_dict['p_unknown_plot'][0]),
           ('Aphid', 'Symbiont', 'Aphid & Symbiont', 'Regiella insecticola', 
            'Other bacteria', 'Host plant', 
            'Aphid & Host plant', 'Symbiont & Host plant', 
            'Aphid, Symbiont, & Host plant', 'Unknown'),
           loc = 'upper left', bbox_to_anchor = (-0.1, -0.2), 
           prop = {'family' : 'sans-serif', 'size' : 12}, frameon = False, 
           ncol = 2)
plt.xlabel('Percentage', fontdict = other_font)
plt.xlim(right = 100)
plt.yticks((0.25, 0.75), ('', ''), size = 12, family = 'sans-serif')
# Sets positioning and text properties for bar chart x-axis

plt.text(-80, 1.67, 'a)', fontsize = 20, family = 'sans-serif')
plt.text(-5, 1.67, 'b)', fontsize = 20, family = 'sans-serif')
# Uses panel b bar chart axes to position text for panel labels
plt.text(-70, 0.75, 'Gut', fontsize = 16, family = 'sans-serif', rotation = 90)
plt.text(-70, 0.25, 'Bacteriome', fontsize = 16, family = 'sans-serif', rotation = 90)
# Uses panel b bar chart axes to position text for panel a pie chart subtitles

ax.spines['right'].set_visible(False)  # Removes right axis
ax.spines['left'].set_visible(False)  # Removes left axis
ax.yaxis.set_ticks_position('none')  # Keeps vertical ticks hidden
ax.xaxis.set_ticks_position('both')  # Shows x-axis ticks
ax.tick_params(axis = 'x', direction = 'in')  # Directs the x-axis ticks inward


######################
# Figure Adjustments #
######################

plt.subplots_adjust(top = 0.75, wspace = 0.5)
# plt.suptitle('Reads Aligned per Genome', fontsize = 18, family = 'sansserif', 
#              fontweight = 'bold')
plt.savefig('C:\\Users\Thompson\Documents\Figure_1_G002.svg', 
            bbox_inches = 'tight', format = 'svg', dpi = 500)
plt.show()