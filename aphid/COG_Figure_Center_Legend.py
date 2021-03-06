#! /usr/bin/python

import csv
import matplotlib as mpl
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import choice
import pylab
from scipy import stats
import statistics
import statsmodels.stats.multitest as smm
import scipy
import seaborn as sns
from mpl_toolkits.axes_grid1 import AxesGrid

# to center colormap closer to zero
def shiftedColorMap(cmap, start=0, midpoint=0.5, stop=1.0, name='shiftedcmap'):
    '''
    Function to offset the "center" of a colormap. Useful for
    data with a negative min and positive max and you want the
    middle of the colormap's dynamic range to be at zero.

    Input
    -----
      cmap : The matplotlib colormap to be altered
      start : Offset from lowest point in the colormap's range.
          Defaults to 0.0 (no lower offset). Should be between
          0.0 and `midpoint`.
      midpoint : The new center of the colormap. Defaults to 
          0.5 (no shift). Should be between 0.0 and 1.0. In
          general, this should be  1 - vmax / (vmax + abs(vmin))
          For example if your data range from -15.0 to +5.0 and
          you want the center of the colormap at 0.0, `midpoint`
          should be set to  1 - 5/(5 + 15)) or 0.75
      stop : Offset from highest point in the colormap's range.
          Defaults to 1.0 (no upper offset). Should be between
          `midpoint` and 1.0.
    '''
    cdict = {
        'red': [],
        'green': [],
        'blue': [],
        'alpha': []
    }

    # regular index to compute the colors
    reg_index = np.linspace(start, stop, 257)

    # shifted index to match the data
    shift_index = np.hstack([
        np.linspace(0.0, midpoint, 128, endpoint=False), 
        np.linspace(midpoint, 1.0, 129, endpoint=True)
    ])

    for ri, si in zip(reg_index, shift_index):
        r, g, b, a = cmap(ri)

        cdict['red'].append((si, r, r))
        cdict['green'].append((si, g, g))
        cdict['blue'].append((si, b, b))
        cdict['alpha'].append((si, a, a))

    newcmap = mpl.colors.LinearSegmentedColormap(name, cdict)
    plt.register_cmap(cmap=newcmap)

    return newcmap

cogs_dict_g = {}  # holds genome COGs; turns to percentages

cogs_dict = {}  # holds targets COGs; turns to percentages
cogs_per = []  # used for plotting target composition percentages in order

cogs_dict_final = {}  # holds target - genome percentages with labels
labels_final = []  # holds ordered labels
cogs_per_final = []   # used for plotting target - genome composition percentages in order

probs = []  # holds probability (weights) for each COG in genome
probs_dict = {}  # probability with label
pvals_raw = []
ci = []  # holds confidence intervals

filelist = ["myseq0.fa.emapper.annotations", "myseq27000.fa.emapper.annotations", 
            "myseq13500.fa.emapper.annotations", "myseq4500.fa.emapper.annotations", 
            "myseq18000.fa.emapper.annotations", "myseq9000.fa.emapper.annotations", 
            "myseq22500.fa.emapper.annotations"]
            # target COG files
total_g = 0
for file in filelist:
    with open(file) as f:
        csvreader = csv.reader(f, delimiter = '\t')
        header = next(csvreader)
        for row in csvreader:
            cog = row[11]
            name = row[0]
            if cog == "S":
                next(csvreader)
            else:
                total_g = total_g + 1
                # actual total number instead of total which includes proteins 
                # multiple times for each COG assigned
                if len(cog) > 1:
                    cogs_list_g = cog.split(', ')  # because entries can match to multiple COGs
                    for entry in cogs_list_g:
                        cogs_dict_g.setdefault(entry, []).append(name)
                else:
                    cogs_dict_g.setdefault(cog, []).append(name)
total_t = 0
with open('Myzus_persicae_Clone_G006b_scaffolds.gff.pep_targets.fa.emapper.annotations') as f:
    csvreader = csv.reader(f, delimiter = '\t')
    header = next(csvreader)
    for row in csvreader:
        cog = row[11]
        name = row[0]
        if cog == 'S':
            next(csvreader)
        else:
            total_t = total_t + 1
            if len(cog) > 1:
                cogs_list = cog.split(', ')
                for entry in cogs_list:
                    cogs_dict.setdefault(entry, []).append(name)
            else:
                cogs_dict.setdefault(cog, []).append(name)
# these create dictionaries with the COG letters as keys and proteins as values
            
# colors = ["#E50000", "#E32600", "#E14C00", "#E07100", "#DE9500", "#DCB900", 
#           "#D8DB00", "#B2D900", "#8CD700", "#67D600", "#43D400", "#1FD200", 
#           "#00D104", "#00CF27", "#00CD49", "#00CC6B", "#00CA8C", "#00C8AD", 
#           "#00C0C7", "#009DC5", "#007BC3", "#0059C2", "#0038C0", "#0018BF"]
#           # colors is from a color gradient producer
# colors_2 = []  # colors_2 creates new pattern
# for i in range(0, 6):
#     for j in range(0, 4):
#         colors_2.append(colors[i+(6*j)])
# colors_2 now created below cogs_per_final

labels = ["RNA processing and modification", "Chromatin structure and dynamics", 
          "Energy production and conversion", 
          "Cell cycle control, cell division,\nchromosome partitioning", 
          "Amino acid transport and metabolism", "Nucleotide transport and metabolism", 
          "Carbohydrate transport and metabolism", "Coenzyme transport and metabolism", 
          "Lipid transport and metabolism", 
          "Translation, ribosomal structure,\nand biogenesis", 
          "Transcription", "Replication, recombination, and repair", 
          "Cell wall/membrane/envelope biogenesis", "Cell motility", 
          "Posttranslational modification,\nprotein turnover, chaperones", 
          "Inorganic ion transport\nand metabolism", 
          "Secondary metabolites biosynthesis,\ntransport, and catabolism", 
          "Signal transduction mechanisms", 
          "Intracellular trafficking, secretion,\nand vesicular transport", 
          "Defense mechanisms", "Extracellular structures", 
          "Nuclear structure", "Cytoskeleton"]
          # COG long form labels over letters
# labels_norm = ["Intracellular trafficking, secretion,\nand vesicular transport", 
#               "Energy production and conversion", 
#               "Inorganic ion transport\nand metabolism", 
#               "Secondary metabolites biosynthesis,\ntransport and catabolism", 
#               "Translation, ribosomal structure\nand biogenesis", 
#               "Replication, recombination and repair", "Cytoskeleton", 
#               "Cell cycle control, cell division,\nchromosome partitioning", 
#               "Lipid transport and metabolism", "Transcription", 
#               "RNA processing and modification", "Carbohydrate transport and metabolism", 
#               "Amino acid transport and metabolism", 
#               "Posttranslational modification,\nprotein turnover, chaperones", 
#               "Signal transduction mechanisms"]
#               # labels for non-truncated normally distributed COGs from the genome simulations
labels_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", 
                  "P", "Q", "T", "U", "V", "W", "Y", "Z"]
                  # COG short form letters in the same order as labels
# total = 0
# for key in cogs_dict.keys():
#     total = total + len(cogs_dict[key])
    # counts up total target proteins; some counted multiple times because they had multiple 
    # COG assignments (look to i and j)
for (long_form, short_form) in zip(labels, labels_letters):
    try:
        cogs_dict[long_form] = cogs_dict.pop(short_form)  # exchanges letter COG for label
        cogs_dict[long_form] = len(cogs_dict[long_form])/(total_t/100)
        # creates percentage from number of values (proteins) over the total
    except KeyError:
        pass
not_in_targets = ["Defense mechanisms", "Coenzyme transport and metabolism", "Cell motility"]
                  # these entries show up in the genome proteins but not targets
                  # this sorts it out for the figure production
for entry in not_in_targets:
    cogs_dict[entry] = 0


# total = 0
# for key in cogs_dict_g.keys():
#     total = total + len(cogs_dict_g[key])
    # counts up total genome proteins; some counted multiple times because they had multiple 
    # COG assignments (look to i and j)
for (long_form, short_form) in zip(labels, labels_letters):
    try:
        cogs_dict_g[long_form] = cogs_dict_g.pop(short_form)
        cogs_dict_g[long_form] = len(cogs_dict_g[long_form])/(total_g/100)
        cogs_dict_final[long_form] = cogs_dict[long_form] - cogs_dict_g[long_form]
    except KeyError:
        pass

sorted_dict_list = sorted(cogs_dict.items(), key=lambda x: (abs(x[1]), abs(cogs_dict_final[x[0]])), reverse = True)
# sorted_dict_list = sorted(cogs_dict_final.items(), key=lambda x: ((x[1]), abs(cogs_dict_final[x[0]])), reverse = True)
# sorts the dictionary into a list to keep a consistent order
# second sorting key goes by magnitude of percent difference
# secondary sorting also assures the same order each time
for entry in sorted_dict_list:
    label = entry[0]
    percent = entry[1]
    labels_final.append(label)
    probs_dict[label] = []
    cogs_per.append(percent)
    cogs_per_final.append(cogs_dict_final[label])
    # cogs_per_final.append(percent)
    # cogs_per.append(cogs_dict[label])
    # this loop estabilishes many lists for the figure at once, keeping the order the same

for label in labels_final:
    probs.append(cogs_dict_g[label]/sum(cogs_dict_g.values()))
    # total percent is >100 but this needs a ratio, so it's divided by the total percent
    # this generates probabilities for the MC simulation

for i in range(1, 1001):  # takes just under seven minutes to run with 1,000,001
    choice_out = list(choice(labels_final, 173, p = probs))
    for label in probs_dict.keys():
        probs_dict[label].append((choice_out.count(label))/1.73)
        # stores percentages from each simulation
    # MC simulation
    # uses the probabilities from above to simulate 1 million random samplings from the 
    # genome that are 173 proteins like the miRNA target set

# import seaborn as sns
# sns.set(color_codes=True)
# for label in labels_final[18:]:
#     dist = probs_dict[label]
#     fig = plt.figure()
#     ax = fig.add_subplot(121)
#     stats.probplot(dist, dist="norm", plot=pylab)
#     ax.set_title(label + '\n')
#     fig.add_subplot(122)
#     sns.distplot(dist, kde = False, rug = True)
#     label2 = label.replace("\n","")
#     label2 = label2.replace('/', ' and ')
#     plt.savefig('C:\\Users\Thompson\Documents\%s_prob_dist.svg' % label2, 
#                 bbox_inches = 'tight', format = 'svg', dpi = 500)
#     plt.show()
# Creates QQ and histogram plots for each COG based on the MC simulated distributions

for label in labels_final:  # or labels_norm
    Z = (cogs_dict[label] - sum(probs_dict[label])/len(probs_dict[label]))/statistics.stdev(probs_dict[label])
    pvals_raw.append(scipy.stats.norm.sf(abs(Z))*2)
    # if Z > 0:
    #     ci.append(sum(probs_dict[label])/len(probs_dict[label]) + stats.norm.ppf(.975)*statistics.stdev(probs_dict[label]))
    # else:
    #     ci.append(sum(probs_dict[label])/len(probs_dict[label]) + stats.norm.ppf(.025)*statistics.stdev(probs_dict[label]))

reject, pvals_cor, alphacSidak, alphacBonf = smm.multipletests(pvals_raw, alpha = 0.05, method = 'fdr_bh')
with open('p-values.txt', 'w') as f:
    for label, p_cor, p_raw in zip(labels_final, pvals_cor, pvals_raw):
        if p_cor <= 0.05:
            f.write('%s (p-value > 0.05): %s (raw: %s)\n' % (label, p_cor, p_raw))
        else:
            f.write('%s (p-value): %s (raw: %s)\n' % (label, p_cor, p_raw))


sns.set_style('white')  # sets sns background styling to white
vmax = max(cogs_per_final)
vmin = min(cogs_per_final)
mid = 1 - vmax / (vmax + abs(vmin))
centered_cm = shiftedColorMap(sns.diverging_palette(250, 15, s=99, l=50, center="light", as_cmap = True), 
                              start = 0, midpoint = mid, stop = 1, name = 'centered_cm')
# makes a matplotlib colormap (cm) object (https://seaborn.pydata.org/tutorial/color_palettes.html)
# range is from ~-5 to ~7, so just adding 5 to all numbers doesn't center the cm
colors_2 = []
for entry in cogs_per_final:
    colors_2.append(centered_cm((entry - min(cogs_per_final))
                                / (float(max(cogs_per_final)) 
                                - min(cogs_per_final))))

# plot = plt.scatter(cogs_per_final, cogs_per_final, c = cogs_per_final, cmap = 'centered_cm')  # establishes colorbar in scatterplot
# plt.clf()  # clears scatterplot
 

#####################
# Figure Production #
#####################

fig = plt.figure(figsize = (15, 15))
ind = np.arange(len(labels_final))
ax = plt.subplot(1, 10, (5, 10))
barlist = plt.barh(ind, cogs_per, height = 1, align = 'edge')
for i, color in zip(range(0, len(barlist)), colors_2):
    barlist[i].set_color(color)
    if i%2 == 0:
        ax.axhspan(i, 1 + i, color = 'white', alpha = 0.15)
    else:
        ax.axhspan(i, 1 + i, color = 'lightgrey', alpha = 0.15)
ax.axvspan(0, -0.25, color = 'white')
ax.axvspan(-29.7, -29.95, color = 'white')
plt.yticks(ind, '')
plt.ylim([0, ind.size])  # Removes whitespace to right side
plt.xlim([-30, 25])
plt.xlabel('Percent Composition\n(Targets)', x = 0.77, fontsize = 12)
plt.xticks((0, 5, 10, 15, 20, 25), (0, 5, 10, 15, 20, 25), fontsize = 12)
ax.tick_params(direction = 'out')
ax.spines['right'].set_visible(False)  # Removes right axis
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)  # Removes top axis
ax.yaxis.set_ticks_position('none')  # Keeps vertical ticks hidden
ax.xaxis.set_ticks_position('bottom')  # Keeps horizontal ticks hidden on top
# plt.colorbar(plot)  # plots colorbar from earlier scatterplot

ind = np.arange(len(labels_final))
ax = plt.subplot(1, 10, (1, 4))
barlist = plt.barh(ind, cogs_per_final, height = 1, align = 'edge')
for i, color, label in zip(range(0, len(barlist)), colors_2, labels_final): # entry and ci missing now
    barlist[i].set_color(color)
    if i%2 == 0:
        ax.axhspan(i, 1 + i, color = 'white', alpha = 0.15)
    else:
        ax.axhspan(i, 1 + i, color = 'lightgrey', alpha = 0.15)
    # ax.axvline(entry - cogs_dict_g[label], color = 'darkgrey', 
    #           ymin = (i)/23, ymax = (1 + i)/23, linewidth = 1.5)
plt.yticks(ind + 0.5, labels_final, rotation = "horizontal", fontsize = 12, multialignment = 'center')
plt.ylim([0, ind.size])  # Removes whitespace to right side
plt.xlim([-8, 8])
plt.xlabel('Enrichment Over Genome (%)', fontsize = 12)
plt.xticks(fontsize = 12)
ax.yaxis.tick_right()
ax.tick_params(direction = 'out')
ax.spines['right'].set_visible(False)  # Removes right axis
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)  # Removes top axis
ax.yaxis.set_ticks_position('none')  # Keeps vertical ticks hidden
ax.xaxis.set_ticks_position('bottom')  # Keeps horizontal ticks hidden on top


plt.subplots_adjust(wspace = 0.00)
if len(probs_dict[label]) == 1000000:
    plt.savefig('C:\\Users\Thompson\Documents\Figure_COG_Center_Legend_1Mil.svg', 
                bbox_inches = 'tight', format = 'svg', dpi = 500)
else:
    plt.savefig('C:\\Users\Thompson\Documents\Figure_COG_Center_Legend.svg', 
                bbox_inches = 'tight', format = 'svg', dpi = 500)
plt.show()
