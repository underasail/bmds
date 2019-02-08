# import matplotlib as mpl
# mpl.use('SVG')


import time
start_time = time.time()

#import csv
#from numpy.random import choice
#import statistics
#import statsmodels.stats.multitest as smm
#import scipy
#from scipy import stats
#import pylab
#from joblib import Parallel, delayed 
#import multiprocessing
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pickle


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
cogs_dict_utr_g = {}

cogs_dict = {}  # holds targets COGs; turns to percentages
cogs_dict_utr = {}
cogs_per = []  # used for plotting target composition percentages in order

cogs_dict_final = {}  # holds target - genome percentages with labels
labels_final = []  # holds ordered labels
cogs_per_final = []   # used for plotting target - genome composition percentages in order

probs = []  # holds probability (weights) for each COG in genome
probs_dict = {}  # probability with label
probs_dict_bc = {}  # for boxcox transformation
pvals_raw = []
pvals_dict = {}
ci = {}  # holds confidence intervals
#
#filelist = ["corrected_myseq0.fa.emapper.annotations", 
#            "corrected_myseq4500.fa.emapper.annotations", 
#            "corrected_myseq9000.fa.emapper.annotations", 
#            "corrected_myseq13500.fa.emapper.annotations", 
#            "corrected_myseq18000.fa.emapper.annotations", 
#            "corrected_myseq22500.fa.emapper.annotations", 
#            "corrected_myseq27000.fa.emapper.annotations"]
#            # target COG files
##total_g = 0
#for file in filelist:
#    with open(file) as f:
#        csvreader = csv.reader(f, delimiter = '\t')
##        header = next(csvreader)
#        for row in csvreader:
#            cog = row[11]
#            name = '_'.join(row[0].split('_')[0:4])
#            utr = '_'.join(row[0].split('_')[4:6])
#            if cog == "S":
#                pass
#            else:
##                total_g = total_g + 1
#                # actual total number instead of total which includes proteins 
#                # multiple times for each COG assigned
#                if len(cog) > 1:
#                    cogs_list_g = cog.split(', ')  # because entries can match to multiple COGs
#                    for entry in cogs_list_g:
#                        # entry is cog
#                        cogs_dict_g.setdefault(entry, []).append(name)
##                        cogs_dict_utr_g.append([entry, name, utr])
##                        cogs_dict_utr_g.setdefault('{0}_{1}'.format(entry, utr), []).append(name)
#                        cogs_dict_utr_g.setdefault(utr, []).append('{0}_{1}'.format(entry, name))
##                        cogs_dict_g.setdefault(entry, []).append(scaffold_name_list[parent_list.index(name)])
#                else:
#                    cogs_dict_g.setdefault(cog, []).append(name)
##                    cogs_dict_utr_g.append([cog, name, utr])
##                    cogs_dict_utr_g.setdefault('{0}_{1}'.format(cog, utr), []).append(name)
#                    cogs_dict_utr_g.setdefault(utr, []).append('{0}_{1}'.format(cog, name))
##                    cogs_dict_g.setdefault(cog, []).append(scaffold_name_list[parent_list.index(name)])
#total_g = 0
#for key in cogs_dict_g:
##    cogs_dict_g[key] = set(cogs_dict_g[key])
##    total_g = total_g + len(set(cogs_dict_g[key]))
#    total_g = total_g + len(cogs_dict_g[key])
##total_t = 0
#with open('Myzus_persicae_Clone_G006b_scaffolds.gff.pep_targets_2.fa.emapper.annotations') as f:
#    csvreader = csv.reader(f, delimiter = '\t')
#    header = next(csvreader)
#    for row in csvreader:
#        cog = row[11]
##        name = row[0]
#        name = '_'.join(row[0].split('_')[0:4])
#        utr = '_'.join(row[0].split('_')[4:6])
##        name = name.split('.')[1]
#        if cog == 'S':
#            pass
#        else:
##            total_t = total_t + 1
#            if len(cog) > 1:
#                cogs_list = cog.split(', ')
#                for entry in cogs_list:
#                    cogs_dict.setdefault(entry, []).append(name)
#                    cogs_dict_utr.setdefault(utr, []).append('{0}_{1}'.format(entry, name))
##                    cogs_dict.setdefault(entry, []).append(scaffold_name_list[parent_list.index(name)])
##                    cogs_dict_utr.append([entry, name, utr])
##                    cogs_dict_utr.setdefault('{0}_{1}'.format(entry, utr), []).append(name)
#                    
#            elif len(cog) == 1:
#                cogs_dict.setdefault(cog, []).append(name)
##                cogs_dict.setdefault(cog, []).append(scaffold_name_list[parent_list.index(name)])
##                cogs_dict_utr.append([cog, name, utr])
##                cogs_dict_utr.setdefault('{0}_{1}'.format(cog, utr), []).append(name)
#                cogs_dict_utr.setdefault(utr, []).append('{0}_{1}'.format(cog, name))
#            else:
#                pass
#total_t = 0
#for key in cogs_dict:
##    cogs_dict[key] = set(cogs_dict[key])
##    total_t = total_t + len(set(cogs_dict[key]))
#    total_t = total_t + len(cogs_dict[key])
## these create dictionaries with the COG letters as keys and proteins as values
#
#labels = ["RNA processing and modification", 
#          "Chromatin structure and dynamics", 
#          "Energy production and conversion", 
#          "Cell cycle control, cell division,\nchromosome partitioning", 
#          "Amino acid transport and metabolism", 
#          "Nucleotide transport and metabolism", 
#          "Carbohydrate transport and metabolism", 
#          "Coenzyme transport and metabolism", 
#          "Lipid transport and metabolism", 
#          "Translation, ribosomal structure,\nand biogenesis", 
#          "Transcription", 
#          "Replication, recombination, and repair", 
#          "Cell wall/membrane/envelope biogenesis", 
#          "Cell motility", 
#          "Posttranslational modification,\nprotein turnover, chaperones", 
#          "Inorganic ion transport\nand metabolism", 
#          "Secondary metabolites biosynthesis,\ntransport, and catabolism", 
#          "Signal transduction mechanisms", 
#          "Intracellular trafficking, secretion,\nand vesicular transport", 
#          "Defense mechanisms", 
#          "Extracellular structures", 
#          "Nuclear structure", 
#          "Cytoskeleton"]
#          # COG long form labels over letters
#
#labels_letters = ["A", "B", "C", "D", "E", "F", "G", "H", 
#                  "I", "J", "K", "L", "M", "N", "O", "P", 
#                  "Q", "T", "U", "V", "W", "Y", "Z"]
#                  # COG short form letters in the same order as labels
#
#for (long_form, short_form) in zip(labels, labels_letters):
#    try:
#        cogs_dict[long_form] = cogs_dict.pop(short_form)  
#        # exchanges letter COG for label
#        cogs_dict[long_form] = len(cogs_dict[long_form])/(total_t/100)
#        # creates percentage from number of values (proteins) over the total
#    except KeyError:
#        pass
#not_in_targets = ["Defense mechanisms", 
#                  "Coenzyme transport and metabolism", 
#                  "Cell motility"]
#                  # these entries show up in the genome proteins but not targets
#                  # this sorts it out for the figure production
#for entry in not_in_targets:
#    cogs_dict[entry] = 0
#
#
#for (long_form, short_form) in zip(labels, labels_letters):
#    try:
#        cogs_dict_g[long_form] = cogs_dict_g.pop(short_form)
#        cogs_dict_g[long_form] = len(cogs_dict_g[long_form])/(total_g/100)
#        cogs_dict_final[long_form] = cogs_dict[long_form] - cogs_dict_g[long_form]
#    except KeyError:
#        pass
#
#with open('cogs_dict.pkl', 'wb') as dict_file:
#    pickle.dump(cogs_dict, dict_file, protocol = pickle.HIGHEST_PROTOCOL)
#with open('cogs_dict_g.pkl', 'wb') as dict_file:
#    pickle.dump(cogs_dict_g, dict_file, protocol = pickle.HIGHEST_PROTOCOL)
#with open('cogs_dict_final.pkl', 'wb') as dict_file:
#    pickle.dump(cogs_dict_final, dict_file, protocol = pickle.HIGHEST_PROTOCOL)

#%%
        
#mid_time = time.time()
#print(round(mid_time - start_time, 2))
#
#def choices_list(i):
#    choices = []
#    counted_dict = {}
#    for i in range(0, 173):
##        choice_out = list(choice(sorted(cogs_dict_utr_g.keys()), 1))
##        cog = choice_out[0].split('_')[0]
##        length = len(cogs_dict_utr_g[choice_out[0]])
##        choices.extend(list(cog)*length)
#        utr = list(choice(sorted(cogs_dict_utr_g.keys()), 1))[0]
#        for entry in cogs_dict_utr_g[utr]:
#            cog = entry.split('_')[0]
##            name = '_'.join(entry.split('_')[1:])
#            choices.append(cog)
#    for label in labels:
#        percent = (choices.count(labels_letters[labels.index(label)]))/(len(choices)/100)
#        counted_dict.setdefault(label, []).append(percent)
#
#    return counted_dict
#
##num_cores = multiprocessing.cpu_count()
#num_cores = 4
#counted_dicts = Parallel(n_jobs=num_cores)(delayed(choices_list)(i) for i in range(1, 10001))
#
#for counted_dict in counted_dicts:
#    for label in counted_dict.keys():
#        probs_dict.setdefault(label, []).extend(counted_dict[label])
#
#
#with open('probs_dict.pkl', 'wb') as dict_file:
#    pickle.dump(probs_dict, dict_file, protocol = pickle.HIGHEST_PROTOCOL)
#
## Old methods
#        # grabs the short form label from the matching index of the long form
#        # list and checks the count of that in the cog output (choices) then
#        # divdes to make a percentage using a matching length
#        
#        # stores percentages from each simulation
#    # MC simulation
#    # uses the probabilities from above to simulate 1 million random samplings from the 
#    # genome that are 173 proteins like the miRNA target set
#mid_time_2 = time.time()
#print(round(mid_time_2 - mid_time, 2))
#%%

#time_3 = time.time()
#
#with open('probs_dict_300000.pkl', 'rb') as dict_file:
#    probs_dict = pickle.load(dict_file)
#
#
#sns.set(color_codes=True)
#sns.set_style('white')
#for label in probs_dict.keys():
#    probs_dict_bc[label] = [x + 1 for x in probs_dict[label]]
#    # establishes a distribution shifted right by 1 for coxbox transform
#    
#    dist = probs_dict[label]
#    fig = plt.figure(figsize = (8, 8))
#    ax = fig.add_subplot(221)
#    stats.probplot(dist, dist="norm", plot=pylab)
#    ax.set_title('')
#    ax2 = fig.add_subplot(222)
#    sns.distplot(dist, kde = False, rug = False)
#    ax2.set_xlabel('COG Composition in Simulation Run (%)')
#    ax2.set_ylabel('\n')
#    label2 = label.replace("\n","")
#    label2 = label2.replace('/', ' and ')
#    # Plots the non-transformed distribution in a QQ and histogram
#    
#    dist_bc = stats.boxcox(probs_dict_bc[label])[0]
#    ax3 = fig.add_subplot(223)
#    stats.probplot(dist_bc, dist="norm", plot=pylab)
#    ax3.set_title('')
#    ax4 = fig.add_subplot(224)
#    sns.distplot(dist_bc, kde = False, rug = False)
#    ax4.set_xlabel('COG Composition in Simulation Run (%)')
#    ax4.set_ylabel('\n')
#    fig.suptitle(label, fontsize = 18)
#    plt.savefig('%s_prob_dist_boxcox_comp_300000.png' % label2, 
#                bbox_inches = 'tight', format = 'png', dpi = 300)
##    plt.show()
#    plt.close()
#    # Plots the transformed version
## Creates QQ and histogram plots for each COG based on the MC simulated distributions
#for label in probs_dict.keys():
#    print('{0}: \nShapiro-Wilk (test-statistic, p-value): {1}\nNormaltest: {2}'.format(label, stats.shapiro(probs_dict[label]), stats.normaltest(probs_dict[label])))
#for label in probs_dict_bc.keys():
#    print('[Box Cox] - {0}: \nShapiro-Wilk (test-statistic, p-value): {1}\nNormaltest: {2}'.format(label, stats.shapiro(stats.boxcox(probs_dict_bc[label])[0]), stats.normaltest(stats.boxcox(probs_dict_bc[label])[0])))
## Runs Shapiro-Wilk test to determine if the distrobutions are normal (p < 0.05 means not normal)
#
#time_4 = time.time()
#print(time_4 - time_3)
#%%
    
##for label in labels_final:  # or labels_norm
#for label in labels:
#    Z = (cogs_dict[label] - sum(probs_dict[label])/len(probs_dict[label]))/statistics.stdev(probs_dict[label])
#    pvals_raw.append(scipy.stats.norm.sf(abs(Z))*2)
#    print(label, scipy.stats.norm.sf(abs(Z))*2)
#    if Z > 0:
#        ci.setdefault(label, []).append(sum(probs_dict[label])/len(probs_dict[label]) + stats.norm.ppf(.975)*statistics.stdev(probs_dict[label]))
#    else:
#        ci.setdefault(label, []).append(sum(probs_dict[label])/len(probs_dict[label]) + stats.norm.ppf(.025)*statistics.stdev(probs_dict[label]))
#print(ci)
#reject, pvals_cor, alphacSidak, alphacBonf = smm.multipletests(pvals_raw, alpha = 0.05, method = 'fdr_bh')
#with open('p-values.txt', 'w') as f:
#    for label, p_cor, p_raw in zip(labels_final, pvals_cor, pvals_raw):
#        if p_cor <= 0.05:
#            f.write('%s (p-value > 0.05): %s (raw: %s)\n' % (label, p_cor, p_raw))
#            print('%s (p-value > 0.05): %s (raw: %s)\n' % (label, p_cor, p_raw))
#        else:
#            f.write('%s (p-value): %s (raw: %s)\n' % (label, p_cor, p_raw))
#            print('%s (p-value): %s (raw: %s)\n' % (label, p_cor, p_raw))
with open('cogs_dict.pkl', 'rb') as dict_file:
    cogs_dict = pickle.load(dict_file)
with open('cogs_dict_g.pkl', 'rb') as dict_file:
    cogs_dict_g = pickle.load(dict_file)
with open('cogs_dict_final.pkl', 'rb') as dict_file:
    cogs_dict_final = pickle.load(dict_file)

with open('probs_dict_300000.pkl', 'rb') as dict_file:
    probs_dict = pickle.load(dict_file)

for label in probs_dict.keys():
    target_per = cogs_dict[label]
    total_sims = len(probs_dict[label])
    if cogs_dict_final[label] < 0:
        lesser_pval = len([i for i in probs_dict[label] if i < target_per])/total_sims
        lesser_ci = sorted(probs_dict[label])[int(0.025*total_sims)]
        ci.setdefault(label, []).append(lesser_ci)
        if lesser_pval < 0.05 and lesser_pval != 0:
            print('{0} (Lesser): {1}\nConfidence interval: {2}\n'.format(label, lesser_pval, lesser_ci))
        else:
            pass
    elif cogs_dict_final[label] > 0:
        greater_pval = len([i for i in probs_dict[label] if i > target_per])/total_sims
        greater_ci = sorted(probs_dict[label])[int(0.975*total_sims)]
        ci.setdefault(label, []).append(greater_ci)
        if greater_pval < 0.05 and lesser_pval != 0:
            print('{0} (Greater): {1}\nConfidence interval: {2}\n'.format(label, greater_pval, greater_ci))
        else:
            pass
    else:
        pass

    

#%%

sorted_dict_list = sorted(cogs_dict.items(), key=lambda x: (abs(x[1]), abs(cogs_dict_final[x[0]])), reverse = True)
# sorted_dict_list = sorted(cogs_dict_final.items(), key=lambda x: ((x[1]), abs(cogs_dict_final[x[0]])), reverse = True)
# sorts the dictionary into a list to keep a consistent order
# second sorting key goes by magnitude of percent difference
# secondary sorting also assures the same order each time
for entry in sorted_dict_list:
    label = entry[0]
    percent = entry[1]
    labels_final.append(label)
#    probs_dict[label] = []
    cogs_per.append(percent)
    cogs_per_final.append(cogs_dict_final[label])
    # cogs_per_final.append(percent)
    # cogs_per.append(cogs_dict[label])
    # this loop estabilishes many lists for the figure at once, keeping the order the same

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
# plt.close()  # clears scatterplot
 

#####################
# Figure Production #
#####################

fig = plt.figure(figsize = (14, 15))
ind = np.arange(len(labels_final))
ax = plt.subplot(1, 10, (5, 10))
barlist = plt.barh(ind[:-3], cogs_per[:-3], height = 1, align = 'edge')
for i, color in zip(range(0, len(barlist)), colors_2[:-3]):
    barlist[i].set_color(color)
    if i%2 == 0:
        ax.axhspan(i, 1 + i, color = 'white', alpha = 0.15)
    else:
        ax.axhspan(i, 1 + i, color = 'lightgrey', alpha = 0.15)
ax.axvspan(0, -0.25, color = 'white')
ax.axvspan(-29.7, -29.95, color = 'white')
plt.yticks(ind[:-3], '')
plt.ylim([0, ind[:-3].size])  # Removes whitespace to right side
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
barlist = plt.barh(ind[:-3], cogs_per_final[:-3], height = 1, align = 'edge')
for i, color, label in zip(range(0, len(barlist)), colors_2[:-3], labels_final[:-3]): # entry and ci missing now
    barlist[i].set_color(color)
    if i%2 == 0:
        ax.axhspan(i, 1 + i, color = 'white', alpha = 0.15)
    else:
        ax.axhspan(i, 1 + i, color = 'lightgrey', alpha = 0.15)
    ax.axvline(ci[label][0] - cogs_dict_g[label], color = 'darkgrey', 
              ymin = (i)/20, ymax = (1 + i)/20, linewidth = 1.5)
plt.yticks(ind[:-3] + 0.5, labels_final[:-3], rotation = "horizontal", fontsize = 12, multialignment = 'center')
plt.ylim([0, ind[:-3].size])  # Removes whitespace to right side
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
    plt.savefig('Figure_COG_Center_Legend_1Mil.svg', 
                bbox_inches = 'tight', format = 'svg', dpi = 300)
else:
    plt.savefig('Figure_COG_Center_Legend.svg', 
                bbox_inches = 'tight', format = 'svg', dpi = 300)
# plt.show()
plt.close()


#end_time = time.time()
#print(round(end_time - start_time, 2))
