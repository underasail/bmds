#! /usr/bin/python3

from sys import argv
import csv
import matplotlib.pyplot as plt

with open(argv[1], newline='') as f:
    csvreader = csv.reader(f, delimiter = '\t')
    next(csvreader)
    histlist = next(csvreader)

title = input('Title: ')

plt.hist(histlist, bins = range(0, 31), histtype = 'bar', color = 'red')
plt.title(title)
plt.savefig('%s.png' % argv[2], bbox_inches = 'tight')
plt.show()
