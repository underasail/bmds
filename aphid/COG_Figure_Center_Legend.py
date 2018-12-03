#! /usr/bin/python

import csv
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import choice
import pylab
from scipy import stats
import statistics
import scipy

cogs_dict_g = {}  # holds genome COGs; turns to percentages

cogs_dict = {}  # holds targets COGs; turns to percentages
cogs_per = []  # used for plotting target composition percentages in order

cogs_dict_final = {}  # holds target - genome percentages with labels
labels_final = []  # holds ordered labels
cogs_per_final = []   # used for plotting target - genome composition percentages in order

probs = []  # holds probability (weights) for each COG in genome
probs_dict = {}  # probability with label
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
            
colors = ["#E50000", "#E32600", "#E14C00", "#E07100", "#DE9500", "#DCB900", 
          "#D8DB00", "#B2D900", "#8CD700", "#67D600", "#43D400", "#1FD200", 
          "#00D104", "#00CF27", "#00CD49", "#00CC6B", "#00CA8C", "#00C8AD", 
          "#00C0C7", "#009DC5", "#007BC3", "#0059C2", "#0038C0", "#0018BF"]
          # colors is from a color gradient producer
colors_2 = []  # colors_2 creates new pattern
for i in range(0, 6):
    for j in range(0, 4):
        colors_2.append(colors[i+(6*j)])

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

sorted_dict_list = sorted(cogs_dict.items(), key=lambda x: (abs(x[1]), len(x[0])), reverse = True)
# sorts the dictionary into a list to keep a consistent order
# second sorting key goes by length of label to sort upper three 
# (and all others with the same percent composition)

for entry in sorted_dict_list:
    label = entry[0]
    percent = entry[1]
    labels_final.append(label)
    cogs_per.append(percent)
    cogs_per_final.append(cogs_dict_final[label])
    probs_dict[label] = []
    # this loop estabilishes many lists for the figure at once, keeping the order the same

for label in labels_final:
    probs.append(cogs_dict_g[label]/sum(cogs_dict_g.values()))
    # total percent is >100 but this needs a ratio, so it's divided by the total percent
    # this generates probabilities for the MC simulation

for i in range(1, 1000001):  # takes just under seven minutes to run with 1,000,001
    choice_out = list(choice(labels_final, 173, p = probs))
    for label in probs_dict.keys():
        probs_dict[label].append((choice_out.count(label))/1.73)
        # stores percentages from each simulation
    # MC simulation
    # uses the probabilities from above to simulate 1 million random samplings from the 
    # genome that are 173 proteins like the miRNA target set
# 1,000,000 p-values:
# Signal transduction mechanisms (p-value): 0.0332617619909262
# Amino acid transport and metabolism (p-value): 2.373465927931561e-06
# Carbohydrate transport and metabolism (p-value): 0.040418554927025896
# RNA processing and modification (p-value): 0.015324280023618563
# Intracellular trafficking, secretion, and vesicular transport (p-value): 0.005366584953262637

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
    p = scipy.stats.norm.sf(abs(Z))*2
    if p <= 0.05:
        print('%s (p-value): %s' % (label, p))
    ci.append(sum(probs_dict[label])/len(probs_dict[label]) + stats.norm.ppf(.975)*statistics.stdev(probs_dict[label]))


#####################
# Figure Production #
#####################

fig = plt.figure(figsize = (15, 15))
ind = np.arange(len(labels_final))
ax = plt.subplot(1, 10, (5, 10))
barlist = plt.barh(ind + 0.03, cogs_per, height = 0.96, align = 'edge')
for i, color in zip(range(0, len(barlist)), colors_2):
    barlist[i].set_color(color)
    ax.axhspan(0.03 + i, 0.99 + i, color = color, alpha = 0.20)
plt.yticks(ind, '')
plt.ylim([0, ind.size])  # Removes whitespace to right side
plt.xlim([-30, 25])
plt.xlabel('Percent Composition\n(Targets)', x = 0.77, fontsize = 12)
plt.xticks((0, 10, 20), (0, 10, 20), fontsize = 12)
ax.tick_params(direction = 'out')
ax.spines['right'].set_visible(False)  # Removes right axis
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)  # Removes top axis
ax.yaxis.set_ticks_position('none')  # Keeps vertical ticks hidden
ax.xaxis.set_ticks_position('bottom')  # Keeps horizontal ticks hidden on top

ind = np.arange(len(labels_final))
ax = plt.subplot(1, 10, (1, 4))
barlist = plt.barh(ind + 0.03, cogs_per_final, height = 0.96, align = 'edge')
for i, color, entry, label in zip(range(0, len(barlist)), colors_2, ci, labels_final):
    barlist[i].set_color(color)
    ax.axhspan(0.03 + i, 0.99 + i, color = color, alpha = 0.20)
    if cogs_per_final[i] > 0:
        ax.axvline(entry - cogs_dict_g[label], color = 'black', 
                   ymin = (0.03 + i)/23, ymax = (0.99 + i)/23)
    else:
        ax.axvline(-(entry - cogs_dict_g[label]), color = 'black', 
                   ymin = (0.03 + i)/23, ymax = (0.99 + i)/23)
plt.yticks(ind + 0.5, labels_final, rotation = "horizontal", fontsize = 12, multialignment = 'center')
plt.ylim([0, ind.size])  # Removes whitespace to right side
plt.xlim([-7, 7])
plt.xlabel('Percent Difference\n(Targets - Genome)', fontsize = 12)
plt.xticks(fontsize = 12)
ax.yaxis.tick_right()
ax.tick_params(direction = 'out')
ax.spines['right'].set_visible(False)  # Removes right axis
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)  # Removes top axis
ax.yaxis.set_ticks_position('none')  # Keeps vertical ticks hidden
ax.xaxis.set_ticks_position('bottom')  # Keeps horizontal ticks hidden on top


plt.subplots_adjust(wspace = 0.00)
plt.savefig('C:\\Users\Thompson\Documents\Figure_COG_Center_Legend.svg', 
            bbox_inches = 'tight', format = 'svg', dpi = 500)
plt.show()
