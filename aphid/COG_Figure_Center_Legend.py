#! /usr/bin/python

import csv
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import choice
# import seaborn as sns

cogs_dict_g = {}

cogs_dict = {}
cogs_per = []

cogs_dict_final = {}
labels_final = []
cogs_per_final = []
colors_final = []

probs = []
probs_dict = {}

filelist = ["myseq0.fa.emapper.annotations", "myseq27000.fa.emapper.annotations", 
            "myseq13500.fa.emapper.annotations", "myseq4500.fa.emapper.annotations", 
            "myseq18000.fa.emapper.annotations", "myseq9000.fa.emapper.annotations", 
            "myseq22500.fa.emapper.annotations"]
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
                if len(cog) > 1:
                    cogs_list_g = cog.split(', ')
                    for entry in cogs_list_g:
                        cogs_dict_g.setdefault(entry, []).append(name)
                else:
                    cogs_dict_g.setdefault(cog, []).append(name)

with open('Myzus_persicae_Clone_G006b_scaffolds.gff.pep_targets.fa.emapper.annotations') as f:
    csvreader = csv.reader(f, delimiter = '\t')
    header = next(csvreader)
    for row in csvreader:
        cog = row[11]
        name = row[0]
        if cog == 'S':
            next(csvreader)
        else:
            if len(cog) > 1:
                cogs_list = cog.split(', ')
                for entry in cogs_list:
                    cogs.append(entry)
                    cogs_dict.setdefault(entry, []).append(name)
            else:
                cogs.append(cog)
                cogs_dict.setdefault(cog, []).append(name)
            
colors = ["#E50000", "#E32600", "#E14C00", "#E07100", "#DE9500", "#DCB900", 
          "#D8DB00", "#B2D900", "#8CD700", "#67D600", "#43D400", "#1FD200", 
          "#00D104", "#00CF27", "#00CD49", "#00CC6B", "#00CA8C", "#00C8AD", 
          "#00C0C7", "#009DC5", "#007BC3", "#0059C2", "#0038C0", "#0018BF"]
colors_2 = []
for i in range(0, 6):
    for j in range(0, 4):
        # print((6*j)+i)
        colors_2.append(colors[i+(6*j)])

labels = ["RNA processing and modification", "Chromatin structure and dynamics", 
          "Energy production and conversion", "Cell cycle control, cell division,\nchromosome partitioning", 
          "Amino acid transport and metabolism", "Nucleotide transport and metabolism", 
          "Carbohydrate transport and metabolism", "Coenzyme transport and metabolism", 
          "Lipid transport and metabolism", "Translation, ribosomal structure\nand biogenesis", 
          "Transcription", "Replication, recombination and repair", 
          "Cell wall/membrane/envelope biogenesis", "Cell motility", 
          "Posttranslational modification,\nprotein turnover, chaperones", "Inorganic ion transport\nand metabolism", 
          "Secondary metabolites biosynthesis,\ntransport and catabolism", 
          "Signal transduction mechanisms", "Intracellular trafficking, secretion,\nand vesicular transport", 
          "Defense mechanisms", "Extracellular structures", 
          "Nuclear structure", "Cytoskeleton"]
labels_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", 
                  "K", "L", "M", "N", "O", "P", "Q", "T", "U", 
                  "V", "W", "Y", "Z"]
total = 0
for key in cogs_dict.keys():
    total = total + len(cogs_dict[key])
for (long_form, short_form) in zip(labels, labels_letters):
    try:
        cogs_dict[long_form] = cogs_dict.pop(short_form)
        cogs_dict[long_form] = len(cogs_dict[long_form])/(total/100)
    except KeyError:
        pass
not_in_targets = ["Defense mechanisms", "Coenzyme transport and metabolism", "Cell motility"]
for entry in not_in_targets:
    cogs_dict[entry] = 0


total = 0
for key in cogs_dict_g.keys():
    total = total + len(cogs_dict_g[key])
for (long_form, short_form) in zip(labels, labels_letters):
    try:
        cogs_dict_g[long_form] = cogs_dict_g.pop(short_form)
        cogs_dict_g[long_form] = len(cogs_dict_g[long_form])/(total/100)
        cogs_dict_final[long_form] = cogs_dict[long_form] - cogs_dict_g[long_form]
    except KeyError:
        pass

sorted_dict_list = sorted(cogs_dict.items(), key=lambda x: abs(x[1]), reverse = True)
for entry in sorted_dict_list:
    label = entry[0]
    percent = entry[1]
    labels_final.append(label)
    cogs_per.append(percent)
    cogs_per_final.append(cogs_dict_final[label])
    probs.append(percent/100)
    probs_dict[label] = []

for i in range(1, 10001):
    choice_out = list(choice(labels_final, 173, p = probs))
    for label in probs_dict.keys():
        probs_dict[label].append((choice_out.count(label))/1.73)
# sns.set(color_codes=True)
# for label in probs_dict.keys():
#     sns.distplot(probs_dict[label], kde = False, rug = True)

        

fig = plt.figure(figsize = (15, 15))
ind = np.arange(len(labels_final))
ax = plt.subplot(1, 10, (5, 10))
barlist = plt.barh(ind + 0.03, cogs_per, height = 0.96, align = 'edge')
for i, color in zip(range(0, len(barlist)), colors_2):
    barlist[i].set_color(color)
    ax.axhspan(0.03 + i, 0.99 + i, color = color, alpha = 0.20)
plt.yticks(ind, '')
plt.ylim([0, ind.size])  # Removes whitespace to right side
plt.xlim([-30, 22])
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
for i, color in zip(range(0, len(barlist)), colors_2):
    if i%2 == 0:
        barlist[i].set_color(color)
    else:
        barlist[i].set_color(color)
    ax.axhspan(0.03 + i, 0.99 + i, color = color, alpha = 0.20)
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

