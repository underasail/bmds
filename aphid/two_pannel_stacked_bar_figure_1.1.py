#! /usr/bin/python3


import numpy as np
from matplotlib import pyplot as plt


################
# Data Storage #
################

gut_data = {'aphid' : 1422715/26266.50, 'buchnera' : 7828/26266.50, 
            'both' : 3670/26266.50, 'unknown' : 1192437/26266.50}

gut_data_plant = {'aphid' : 1217185/26266.50, 'buchnera' : 6797/26266.50, 
                  'plant' : 802790/26266.50, 'ab': 725/26266.50, 
                  'ap' : 205530/26266.50, 'bp' : 1031/26266.50, 
                  'abp' : 2945/219608.73, 'unknown' : 389647/26266.50}

bac_data = {'aphid' : 1981277/219608.73, 'buchnera' : 15108223/219608.73, 
            'both' : 3832277/219608.73, 'unknown' : 1039096/219608.73}

bac_data_plant = {'aphid' : 1836976/219608.73, 'buchnera' : 13408949/219608.73, 
                  'plant' : 44379/219608.73, 'ab': 1356864/219608.73, 
                  'ap' : 144301/219608.73, 'bp' : 1699274/219608.73, 
                  'abp' : 2475413/219608.73, 'unknown' : 994717/219608.73}


###################
# Data Formatting #
###################

np_aphid = (gut_data['aphid'], bac_data['aphid'])
np_aphid = np.array(np_aphid)
np_buchnera = (gut_data['buchnera'], bac_data['buchnera'])
np_buchnera = np.array(np_buchnera)
np_both = (gut_data['both'], bac_data['both'])
np_both = np.array(np_both)
np_unknown = (gut_data['unknown'], bac_data['unknown'])
np_unknown = np.array(np_unknown)
# Without (not) plant data set-up

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
# With plant data set-up


##############################
# MatPlotLib Initializations #
##############################

N = (0, 0.75)  # Positioning of bar plots for panel b
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
sizes_gut = [gut_data['unknown'], 
             gut_data['both'] + gut_data['buchnera'] + gut_data['aphid']]
             # Sets up data for pie charts
sizes_bac = [bac_data['unknown'], 
             bac_data['both'] + bac_data['buchnera'] + bac_data['aphid']]
colors = ['m', 'r']  # Sets up colors for pie charts
labels = ['Unknown', 'Holobiont']  # Sets up labels for pie charts

#####################
# Subplot Structure #
#####################

     ###########
     # a1 # bb #
     ###### bb #
     # a2 # bb #
     ###########


#######################
# Panel A: Pie Charts #
#######################

plt.subplot(2, 2, 1) # Rows, Columns, Position
plt.pie(sizes_gut, colors = colors, autopct = '%1.1f%%',
        shadow = False, startangle = 90, wedgeprops = {'linewidth': 0}, 
        pctdistance=1.5)

plt.title('sRNA Source\n', fontdict = title_font) # Acts as panel title
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


plt.subplot(2, 2, 3)
plt.pie(sizes_bac, colors = colors, autopct = '%1.1f%%',
        shadow = False, startangle = 163.26, wedgeprops = {'linewidth': 0}, 
        pctdistance=1.5)

plt.legend(labels, loc = 'upper left', bbox_to_anchor = (-0.35, -0.21), 
           prop = {'family' : 'serif', 'size' : 12}, frameon = False)
plt.axis('equal')


#######################
# Panel B: Bar Charts #
#######################

ax = plt.subplot(1, 2, 2)  # Sets up ax for later proptery manipulations of ticks
p_aphid_plot = plt.bar(N, p_aphid, width = 0.5, color = 'r', linewidth = 0, 
                       edgecolor = 'w', hatch = '/')
p_buchnera_plot = plt.bar(N, p_buchnera, bottom = p_aphid, width = 0.5, 
                          color = 'darkorange', linewidth = 0, edgecolor = 'w', 
                          hatch = '/')
p_ab_plot = plt.bar(N, p_ab, bottom = p_aphid + p_buchnera, width = 0.5, 
                    color = 'gold', linewidth = 0, edgecolor = 'w', hatch = '/')
p_plant_plot = plt.bar(N, p_plant, bottom = p_aphid + p_buchnera + p_ab, 
                       width = 0.5, color = 'green', linewidth = 0, 
                       edgecolor = 'w', hatch = '\\')
p_ap_plot = plt.bar(N, p_ap, bottom = p_aphid + p_buchnera + p_ab + p_plant, 
                    width = 0.5, color = 'limegreen', linewidth = 0, 
                    edgecolor = 'w', hatch = '\\')
p_bp_plot = plt.bar(N, p_bp, bottom = p_aphid + p_buchnera + p_ab + p_plant + p_ap, 
                    width = 0.5, color = 'greenyellow', linewidth = 0, edgecolor = 'w', 
                    hatch = '\\')
p_abp_plot = plt.bar(N, p_abp, 
                     bottom = p_aphid + p_buchnera + p_ab + p_plant+ p_ap + p_bp, 
                     width = 0.5, color = 'mediumturquoise', linewidth = 0, 
                     edgecolor = 'w', hatch = 'x')
p_unknown_plot = plt.bar(N, p_unknown, bottom = 
                         p_aphid + p_buchnera + p_ab + p_plant + p_ap + p_bp + p_abp, 
                         width = 0.5, color = 'm', linewidth = 0)

plt.title('sRNA Mapping\n', fontdict = title_font)
plt.legend((p_unknown_plot[0], p_abp_plot[0], p_bp_plot[0], p_ap_plot[0], 
           p_plant_plot[0], p_ab_plot[0], p_buchnera_plot[0], p_aphid_plot[0]), 
           ('Unknown', 'All', '$\it{Buchnera}$ and Host Plant', 
           'Pea Aphid and Host Plant', 'Host Plant', 
           'Pea Aphid and $\it{Buchnera}$', '$\it{Buchnera}$', 'Pea Aphid'), 
           loc = 'upper left', bbox_to_anchor = (-0.35, -0.1), 
           prop = {'family' : 'serif', 'size' : 12}, frameon = False)
plt.ylabel('Percentage', fontdict = other_font)
plt.ylim(ymax = 100)
plt.xticks((0.25, 1.0), ('Gut', 'Bacteriocyte'), size = 12, family = 'serif')
# Sets positioning and text properties for bar chart x-axis

plt.text(-3.2, 113, 'a)', fontsize = 20, family = 'serif')
plt.text(-0.7, 113, 'b)', fontsize = 20, family = 'serif')
# Uses panel b bar chart axes to position text for panel labels
plt.text(-3.0, 100, 'Gut', fontsize = 14, family = 'serif')
plt.text(-3.0, 47, 'Bacteriocyte', fontsize = 14, family = 'serif')
# Uses panel b bar chart axes to position text for panel a pie chart subtitles

plt.margins(0.05, 0)  # Helps separate bar charts from y axis (x-margin, y-margin)
ax.spines['right'].set_visible(False)  # Removes right axis
ax.spines['top'].set_visible(False)  # Removes top axis
ax.yaxis.set_ticks_position('left')  # Keeps ticks to left side only horizontally
ax.xaxis.set_ticks_position('bottom')  # Keeps ticks to bottom side only vertically


######################
# Figure Adjustments #
######################

plt.subplots_adjust(top = 0.75, wspace = 0.8)
# plt.suptitle('Reads Aligned per Genome', fontsize = 18, family = 'serif', 
#              fontweight = 'bold')
plt.savefig('C:\\Users\Thompson\Documents\Figure_1.1_GvB_with_hatch.svg', 
            bbox_inches = 'tight', format = 'svg')
plt.show()
