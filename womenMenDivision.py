#! /usr/bin/env python
# import numpy as np
# import matplotlib.pyplot as P
from numpy import linspace

from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import matplotlib.pyplot as plt

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

# # Men ratio chart
# n, bins, patches = P.hist(men_ratio, bins=linspace(0, 1.5, 60), color='g', alpha=0.5, label='Men')
# P.axvline(np.mean(men_ratio), color='r', linestyle='dashed', linewidth=2, label="Men average")
# # P.show()

# # Women ratio chart
# n, bins, patches = P.hist(women_ratio, bins=linspace(0, 1.5, 60), color='c', label='Women')
# P.axvline(np.mean(women_ratio), color='b', linestyle='dashed', linewidth=2, label="Women average")
# P.legend()
# P.show()

# # These are all ratios, visibility is really hard
# # Men ratio chart
# n, bins, patches = P.hist(men_ratio, bins=linspace(0, np.max(men_ratio), 60), color='g', alpha=0.5, label='Men')
# P.axvline(np.mean(men_ratio), color='r', linestyle='dashed', linewidth=2)
# # P.show()

# # Women ratio chart
# n, bins, patches = P.hist(women_ratio, bins=linspace(0, np.max(women_ratio), 60), color='c', label='Women')
# P.axvline(np.mean(women_ratio), color='b', linestyle='dashed', linewidth=2)
# P.legend()
# P.show()

# Women childrens mentions
# n, bins, patches = P.hist(women_children, bins=linspace(0, np.max(women_children), 60), color='c', label='Women')
# P.axvline(np.mean(women_children), color='b', linestyle='dashed', linewidth=2)
# P.show()

# Men childrens mentions
# n, bins, patches = P.hist(men_children, bins=linspace(0, np.max(women_children), 60), color='g', alpha=0.5, label='Men')
# P.axvline(np.mean(men_children), color='r', linestyle='dashed', linewidth=2)
# P.legend()
# P.show()



# Double Y axis
bucket_size = 40
buckets = linspace(0, 1.5, bucket_size)
bucket_men = [0] * bucket_size
bucket_women = [0] * bucket_size

for measurement in men_ratio:
  if measurement <= 1.5:
    for i in range(0,bucket_size - 1):
      if measurement >= buckets[i] and measurement < buckets[i+1]:
        bucket_men[i] += 1

for measurement in women_ratio:
  if measurement <= 1.5:
    for i in range(0,bucket_size - 1):
      if measurement >= buckets[i] and measurement < buckets[i+1]:
        bucket_women[i] += 1


host = host_subplot(111, axes_class=AA.Axes)
plt.subplots_adjust(right=0.75)

par1 = host.twinx()

# host.set_xlim(0, 2)
# host.set_ylim(0, 2)

host.set_xlabel("Ratio")
host.set_ylabel("Men")
par1.set_ylabel("Women")

p1, = host.plot(linspace(0, 1.5, bucket_size), bucket_men, label="Men")
p2, = par1.plot(linspace(0, 1.5, bucket_size), bucket_women, label="Women")

# par1.set_ylim(0, 4)

host.legend()

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())

plt.draw()
plt.show()



features.close()
