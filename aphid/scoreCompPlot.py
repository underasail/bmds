import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import gaussian_kde
import seaborn

data1 = []
data2 = []

with open('C:\\Users\Thompson\AppData\Local\Packages\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\LocalState\\rootfs\home\\underasail\\result_1_miranda_targets_0_scores2.out', newline = '') as f:
    csvreader = csv.reader(f, delimiter = '\t')
    for row in csvreader:
        data1.append(float(row[0]))
with open('C:\\Users\Thompson\AppData\Local\Packages\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\LocalState\\rootfs\home\\underasail\\result_1_miranda_targets_0_shuffled_scores2.out', newline = '') as f:
    csvreader = csv.reader(f, delimiter = '\t')
    for row in csvreader:
        data2.append(float(row[0]))

# density1 = gaussian_kde(data1)
# xs1 = numpy.linspace(80, 110, 22226)
# plt.plot(xs1,density1(xs1))
# plt.show()

data1.sort()
data2.sort()

ax1 = plt.subplot(2, 2, 1)
plt.hist(data1, bins = 43, color = 'gold')
plt.title('Standard\n')
plt.xlim(xmax = 110)
plt.ylim(ymax = 3000)
ax1.spines['right'].set_visible(False)  # Removes right axis
ax1.spines['top'].set_visible(False)  # Removes left axis
ax1.yaxis.set_ticks_position('left')  # Keeps vertical ticks left
ax1.xaxis.set_ticks_position('none')  # Keeps vertical ticks hidden
ax1.tick_params(direction = 'out')

ax2 = plt.subplot(2, 2, 2)
plt.hist(data2, bins = 44, color = 'goldenrod')
plt.title('Shuffled\n')
plt.xlim(xmax = 110)
plt.ylim(ymax = 3000)
ax2.spines['right'].set_visible(False)  # Removes right axis
ax2.spines['top'].set_visible(False)  # Removes left axis
ax2.yaxis.set_ticks_position('left')  # Keeps vertical ticks left
ax2.xaxis.set_ticks_position('none')  # Keeps vertical ticks hidden
ax2.tick_params(direction = 'out')

ax3 = plt.subplot(2, 2, 3)
seaborn.distplot(data1, hist=True, kde=True, 
                 bins=43, hist_kws={'color':'goldenrod', 
                                    'edgecolor':'black'},
                 kde_kws={'linewidth': 2, 'color':'darkblue'})
ax3.spines['right'].set_visible(False)  # Removes right axis
ax3.spines['top'].set_visible(False)  # Removes left axis
ax3.yaxis.set_ticks_position('left')  # Keeps vertical ticks left
ax3.xaxis.set_ticks_position('none')  # Keeps vertical ticks hidden
ax3.tick_params(direction = 'out')
plt.xlim(xmin = 77, xmax = 110)
plt.ylim(ymax = 0.12)

ax4 = plt.subplot(2, 2, 4)
seaborn.distplot(data2, hist=True, kde=True, 
                 bins=44, hist_kws={'color':'goldenrod', 
                                    'edgecolor':'black'},
                 kde_kws={'linewidth': 2, 'color':'darkblue'})
ax4.spines['right'].set_visible(False)  # Removes right axis
ax4.spines['top'].set_visible(False)  # Removes left axis
ax4.yaxis.set_ticks_position('left')  # Keeps vertical ticks left
ax4.xaxis.set_ticks_position('none')  # Keeps vertical ticks hidden
ax4.tick_params(direction = 'out')
plt.xlim(xmin = 77, xmax = 110)
plt.ylim(ymax = 0.12)

plt.subplots_adjust(wspace = 0.35, hspace = 0.35)
plt.savefig('C:\\Users\Thompson\Documents\shuffled_distrobution.svg', 
            bbox_inches = 'tight', format = 'svg')
plt.show()

# h = plt.hist(data1, bins = 43, color = 'gold')
# dist_names = [ 'alpha', 'anglit', 'arcsine', 'beta', 'betaprime', 'bradford', 'burr', 'cauchy', 'chi', 'chi2', 'cosine', 'dgamma', 'dweibull', 'erlang', 'expon', 'exponweib', 'exponpow', 'f', 'fatiguelife', 'fisk', 'foldcauchy', 'foldnorm', 'frechet_r', 'frechet_l', 'genlogistic', 'genpareto', 'genexpon', 'genextreme', 'gausshyper', 'gamma', 'gengamma', 'genhalflogistic', 'gilbrat', 'gompertz', 'gumbel_r', 'gumbel_l', 'halfcauchy', 'halflogistic', 'halfnorm', 'hypsecant', 'invgamma', 'invgauss', 'invweibull', 'johnsonsb', 'johnsonsu', 'ksone', 'kstwobign', 'laplace', 'logistic', 'loggamma', 'loglaplace', 'lognorm', 'lomax', 'maxwell', 'mielke', 'nakagami', 'ncx2', 'ncf', 'nct', 'norm', 'pareto', 'pearson3', 'powerlaw', 'powerlognorm', 'powernorm', 'rdist', 'reciprocal', 'rayleigh', 'rice', 'recipinvgauss', 'semicircular', 't', 'triang', 'truncexpon', 'truncnorm', 'tukeylambda', 'uniform', 'vonmises', 'wald', 'weibull_min', 'weibull_max', 'wrapcauchy']
# for dist_name in dist_names:
#     dist = getattr(scipy.stats, dist_name)
#     param = dist.fit(data1)
#     pdf_fitted = dist.pdf(xs1, *param[:-2], loc=param[-2], scale=param[-1]) * size
#     plt.plot(pdf_fitted, label=dist_name)
#     plt.ylim(ymax = 0.12)

# # plt.legend(loc='upper right')
# plt.show()