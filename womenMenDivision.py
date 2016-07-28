#! /usr/bin/env python
import numpy as np
import matplotlib.pyplot as P
from numpy import linspace

features = open('datasetWithFeeling.txt', 'r')

women_ratio = []
women_children = []
men_ratio = []
men_children = []

for line in features:
  if line[0] != '#':
    split = line.split(',')
    gender = int(split[-1])
    if gender == 0:
      women_ratio.append(float(split[11])) # 12
      women_children.append(float(split[12])) #13
    elif gender == 1:
      men_ratio.append(float(split[11]))
      men_children.append(float(split[12]))

# Men ratio chart
n, bins, patches = P.hist(men_ratio, bins=linspace(0, 1.5, 60), color='g', alpha=0.5, label='Men')
P.axvline(np.mean(men_ratio), color='r', linestyle='dashed', linewidth=2)
# P.show()

# Women ratio chart
n, bins, patches = P.hist(women_ratio, bins=linspace(0, 1.5, 60), color='c', label='Women')
P.axvline(np.mean(women_ratio), color='b', linestyle='dashed', linewidth=2)
P.legend()
P.show()

# Women childrens mentions
# n, bins, patches = P.hist(women_children, bins=linspace(0, np.max(women_children), 60), color='c', label='Women')
# P.axvline(np.mean(women_children), color='b', linestyle='dashed', linewidth=2)
# P.show()

# Men childrens mentions
# n, bins, patches = P.hist(men_children, bins=linspace(0, np.max(women_children), 60), color='g', alpha=0.5, label='Men')
# P.axvline(np.mean(men_children), color='r', linestyle='dashed', linewidth=2)
# P.legend()
# P.show()


features.close()
