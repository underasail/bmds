#! /usr/bin/python

import csv
import matplotlib.pyplot as plt
import numpy as np

cogs_g = []
cogs_dict_g = {}
cogs_values_g = []
cogs_per_g = []
labels_ordered_g = []

cogs = []
cogs_dict = {}
cogs_values = []
cogs_per = []
labels_ordered = []

cogs_dict_final = {}
labels_final = []
cogs_per_final = []
colors_final = []

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
                        cogs_g.append(entry)
                        cogs_dict_g.setdefault(entry, []).append(name)
                else:
                    cogs_g.append(cog)
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

# sorted_dict_list = sorted(cogs_dict.items(), key=lambda x: x[1], reverse = True)
# for entry in sorted_dict_list:
#     label = entry[0]
#     percent = entry[1]
#     labels_ordered.append(label)
#     cogs_per.append(percent)
# labels_ordered.append("Defense mechanisms")
# cogs_per.append(0)
# labels_ordered.append("Coenzyme transport and metabolism")
# cogs_per.append(0)
# labels_ordered.append("Cell motility")
# cogs_per.append(0)

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

sorted_dict_list = sorted(cogs_dict_final.items(), key=lambda x: abs(x[1]), reverse = True)
for entry in sorted_dict_list:
    label = entry[0]
    percent = entry[1]
    labels_final.append(label)
    cogs_per_final.append(percent)
    cogs_per.append(cogs_dict[label])
    

# for label in labels_ordered:
#     labels_ordered_g.append(label)
#     percent = cogs_dict_g[label]
#     cogs_per_g.append(percent)
    

# for (cog, cog_g, label, label_g) in zip(cogs_per, cogs_per_g, labels_ordered, labels_ordered_g):
#     # labels_final.append('')
#     # labels_final.append(label)
#     # cogs_per_final.append(cog_g)
#     # cogs_per_final.append(cog)
#     labels_final.append(label)
#     cogs_per_final.append(cog - cog_g)
# cogs_per_final
# for entry in colors_2:
#     colors_final.append(entry)
#     colors_final.append(entry)

ind = np.arange(len(labels_final))
fig = plt.figure(figsize = (15, 15))
ax = plt.subplot(1, 10, (1, 4))
barlist = plt.barh(ind + 0.03, cogs_per_final, height = 0.96, align = 'edge')
for i, color in zip(range(0, len(barlist)), colors_2):
    if i%2 == 0:
        barlist[i].set_color(color)
        # barlist[i].set_edgecolor('black')
        # barlist[i].set_facecolor(color)
        # barlist[i].set_hatch("/")
    else:
        barlist[i].set_color(color)
        # barlist[i].set_edgecolor('black')
        # barlist[i].set_facecolor(color)
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
# ax.axvline(x = 0, color = 'black', linewidth = 1)
# plt.text(-10.1, 23.25, 'COGs', fontsize = 12, family = 'sansserif', weight = 'bold')

# ind = np.arange(2)
# ax = fig.add_subplot(4,5,4)
# barlist = plt.barh([0.01, 0.11], (2, 2.3), height = 0.05, align = 'edge')
# for i, color in zip(range(0, len(barlist)), ["darkgrey", "lightgrey"]):
#     if i%2 == 0:
#         barlist[i].set_edgecolor('black')
#         barlist[i].set_facecolor(color)
#         barlist[i].set_hatch("/")
#     else:
#         # barlist[i].set_color(color)
#         barlist[i].set_edgecolor('black')
#         barlist[i].set_facecolor(color)
# plt.ylim(0, 0.9)
# plt.yticks([0.033, 0.133], ["Genome", "Targets"], rotation = "horizontal", fontsize = 12)
# plt.xticks(ind, '')
# ax.spines['right'].set_visible(False)  # Removes right axis
# ax.spines['top'].set_visible(False)  # Removes top axis
# ax.spines['left'].set_visible(False)  # Removes right axis
# ax.spines['bottom'].set_visible(False)  # Removes top axis
# ax.yaxis.set_ticks_position('none')  # Keeps vertical ticks hidden
# ax.xaxis.set_ticks_position('none')  # Keeps horizontal ticks hidden

ind = np.arange(len(labels_final))
ax = plt.subplot(1, 10, (8, 10))
barlist = plt.barh(ind + 0.03, cogs_per, height = 0.96, align = 'edge')
for i, color in zip(range(0, len(barlist)), colors_2):
    barlist[i].set_color(color)
    ax.axhspan(0.03 + i, 0.99 + i, color = color, alpha = 0.20)
plt.yticks(ind, '')
plt.ylim([0, ind.size])  # Removes whitespace to right side
plt.xlim([0, 22])
plt.xlabel('Percent Composition\n(Targets)', fontsize = 12)
plt.xticks([0, 10, 20], [0, 10, 20], fontsize = 12)
ax.tick_params(direction = 'out')
ax.spines['right'].set_visible(False)  # Removes right axis
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)  # Removes top axis
ax.yaxis.set_ticks_position('none')  # Keeps vertical ticks hidden
ax.xaxis.set_ticks_position('bottom')  # Keeps horizontal ticks hidden on top
# ax.axvline(x = 0, color = 'black', linewidth = 2)

plt.savefig('C:\\Users\Thompson\Documents\Figure_COG.svg', 
            bbox_inches = 'tight', format = 'svg', dpi = 500)
plt.show()
