#! /usr/bin/python3


import numpy as np
from matplotlib import pyplot as plt


################
# Data Storage #
################

gut_data = {'aphid' : 1422715/26266.50, 'buchnera' : 7828/26266.50, 
            'both' : 3670/26266.50, 'unknown' : 1192437/26266.50}

# gut_data_plant = {'aphid' : 1217185/26266.50, 'buchnera' : 6797/26266.50, 
#                   'plant' : 802790/26266.50, 'ab': 725/26266.50, 
#                   'ap' : 205530/26266.50, 'bp' : 1031/26266.50, 
#                   'abp' : 2945/26266.50, 'unknown' : 389647/26266.50}
# Zeroed out to remove those less than 1%
gut_data_plant = {'aphid' : 1217185/26266.50, 'buchnera' : 0/26266.50, 
                  'plant' : 802790/26266.50, 'ab': 0/26266.50, 
                  'ap' : 205530/26266.50, 'bp' : 0/26266.50, 
                  'abp' : 0/26266.50, 'unknown' : 389647/26266.50}

bac_data = {'aphid' : 1981277/219608.73, 'buchnera' : 15108223/219608.73, 
            'both' : 3832277/219608.73, 'unknown' : 1039096/219608.73}

# bac_data_plant = {'aphid' : 1836976/219608.73, 'buchnera' : 13408949/219608.73, 
#                   'plant' : 44379/219608.73, 'ab': 1356864/219608.73, 
#                   'ap' : 144301/219608.73, 'bp' : 1699274/219608.73, 
#                   'abp' : 2475413/219608.73, 'unknown' : 994717/219608.73}
                  
bac_data_plant = {'aphid' : 1836976/219608.73, 'buchnera' : 13408949/219608.73, 
                  'plant' : 0/219608.73, 'ab': 1356864/219608.73, 
                  'ap' : 0/219608.73, 'bp' : 1699274/219608.73, 
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

N = (0.75, 0.05)  # Positioning of bar plots for panel b

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
sizes_gut.reverse()  # To allow legend to be in the correct order

sizes_bac = [bac_data['unknown'], 
             bac_data['both'] + bac_data['buchnera'] + bac_data['aphid']]
sizes_bac.reverse()

# colors = ['darkorange', 'steelblue']  # Sets up colors for pie charts
# labels = ['Non-holobiont', 'Holobiont']       #  "   "  labels  "   "    "   

colors = ['steelblue', 'darkorange']  # Sets up colors for pie charts
labels = ['Holobiont', 'Non-hlobiont']

data_list = [p_aphid, p_buchnera, p_ab, p_plant, p_ap, p_bp, p_abp, p_unknown]
string_list = ['p_aphid_plot', 'p_buchnera_plot', 'p_ab_plot', 'p_plant_plot', 'p_ap_plot', 
               'p_bp_plot', 'p_abp_plot', 'p_unknown_plot']
               # Keeps names the same as before for loop
               # Allows a dictionary to be created with these as the keys and then save 
               # bar chart characteristics under them for legend generation
string_dict = {}
color_list = ['maroon', 'red', 'salmon', 'darkgreen', 'goldenrod', 'gold', 'mediumturquoise', 'orchid']
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
        pctdistance=1.5)

plt.title('sRNA Source\n', fontdict = title_font) # Acts as panel title
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


plt.subplot(2, 3, 4)
plt.pie(sizes_bac, colors = colors, autopct = '%1.1f%%',
        shadow = False, startangle = 16.74, wedgeprops = {'linewidth': 0}, 
        pctdistance=1.5)
        

plt.legend(labels, loc = 'upper left', bbox_to_anchor = (-0.35, -0.445), 
           prop = {'family' : 'serif', 'size' : 12}, frameon = False)
plt.axis('equal')


#######################
# Panel B: Bar Charts #
#######################

ax = plt.subplot(1, 3, (2, 3))  # Sets up ax for later proptery manipulations of ticks

for data, string, color in zip(data_list, string_list, color_list):
    string_dict[string] = ax.barh(N, data, color = color, left = left, height = 0.55, 
                                  linewidth = 0)
    left += data
    
plt.title('sRNA Mapping\n', fontdict = title_font)
plt.legend((string_dict['p_aphid_plot'][0], string_dict['p_buchnera_plot'][0], 
            string_dict['p_ab_plot'][0], string_dict['p_unknown_plot'][0], 
            string_dict['p_plant_plot'][0], string_dict['p_ap_plot'][0], 
            string_dict['p_bp_plot'][0], string_dict['p_abp_plot'][0]),
           ('Aphid', 'Symbiont', 'Aphid and Symbiont', 'Unknown', 'Host plant', 
            'Aphid and Host plant', 'Symbiont and Host plant', 
            'Aphid, Symbiont, and Host plant'),
           loc = 'upper left', bbox_to_anchor = (-0.1, -0.2), 
           prop = {'family' : 'serif', 'size' : 12}, frameon = False, ncol = 2)
plt.xlabel('Percentage', fontdict = other_font)
plt.xlim(xmax = 100)
plt.ylim(ymax = 1.35)
plt.yticks((0.25, 1.0), ('', ''), size = 12, family = 'serif')
# Sets positioning and text properties for bar chart x-axis

plt.text(-80, 1.67, 'a)', fontsize = 20, family = 'serif')
plt.text(-5, 1.67, 'b)', fontsize = 20, family = 'serif')
# Uses panel b bar chart axes to position text for panel labels
plt.text(-9, 1.06, 'Gut', fontsize = 16, family = 'serif', rotation = 90)
plt.text(-9, 0.56, 'Bacteriocyte', fontsize = 16, family = 'serif', rotation = 90)
# Uses panel b bar chart axes to position text for panel a pie chart subtitles

ax.spines['right'].set_visible(False)  # Removes right axis
ax.spines['left'].set_visible(False)  # Removes left axis
# ax.spines['top'].set_visible(False)  # Removes top axis
ax.yaxis.set_ticks_position('none')  # Keeps vertical ticks hidden


######################
# Figure Adjustments #
######################

plt.subplots_adjust(top = 0.75, wspace = 0.5)
# plt.suptitle('Reads Aligned per Genome', fontsize = 18, family = 'serif', 
#              fontweight = 'bold')
plt.savefig('C:\\Users\Thompson\Documents\Figure_1.1_horizontal_GvB.svg', 
            bbox_inches = 'tight', format = 'svg')
plt.show()
