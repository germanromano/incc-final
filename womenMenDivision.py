#! /usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
# import matplotlib.pyplot as P
from numpy import linspace

from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import matplotlib.pyplot as plt

features = open('joined2.txt', 'r')

women_ratio = []
women_children = []
women_color = []
men_ratio = []
men_children = []
men_color = []

for line in features:
  if line[0] != '#':
    split = line.split(',')
    gender = int(split[0])
    if gender == 0:
      women_ratio.append(float(split[12])) # 12 Female pronoun ratio
      women_children.append(float(split[13])) #13 Children mentions
      women_color.append(float(split[17])) #17 Color mentions
    elif gender == 1:
      men_ratio.append(float(split[12]))
      men_children.append(float(split[13]))
      men_color.append(float(split[17]))

# # Men ratio chart
# n, bins, patches = P.hist(men_ratio, bins=linspace(0, 1.5, 60), color='g', alpha=0.5, label='Men')
# P.axvline(np.median(men_ratio), color='r', linestyle='dashed', linewidth=2, label="Men median")
# # P.show()

# # Women ratio chart
# n, bins, patches = P.hist(women_ratio, bins=linspace(0, 1.5, 60), color='c', label='Women')
# P.axvline(np.median(women_ratio), color='b', linestyle='dashed', linewidth=2, label="Women median")
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

# # Men color mentions
# n, bins, patches = P.hist(men_color, bins=linspace(0, np.max(men_color), 60), color='g', alpha=0.5, label='Men')
# P.axvline(np.mean(men_children), color='r', linestyle='dashed', linewidth=2)

# # Women color mentions
# n, bins, patches = P.hist(women_color, bins=linspace(0, np.max(men_color), 60), color='c', label='Women')
# P.axvline(np.mean(women_children), color='b', linestyle='dashed', linewidth=2)
# P.legend()
# P.show()




# Double Y axis
# Config:
men = men_ratio
women = women_ratio
bucket_size = 25
buckets = linspace(0, 1.5, bucket_size)
bucket_men = [0] * bucket_size
bucket_women = [0] * bucket_size
title_text = "Pronombres femeninos / pronombres masculinos"
# --

for measurement in men:
  if measurement <= 1.5:
    for i in range(0,bucket_size - 1):
      if measurement >= buckets[i] and measurement < buckets[i+1]:
        bucket_men[i] += 1

for measurement in women:
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
host.set_ylabel("Libros (hombres)")
par1.set_ylabel("Libros (mujeres)")
plt.title(title_text)

p1, = host.plot(buckets, bucket_men, label="Hombres", color="darkgoldenrod")
plt.axvline(np.mean(men), color='darkgoldenrod', linestyle='dashed', linewidth=1, label="Promedio (hombres)")
p2, = par1.plot(buckets, bucket_women, label="Mujeres", color='g')
plt.axvline(np.mean(women), color='g', linestyle='dashed', linewidth=1, label="Promedio (mujeres)")

# par1.set_ylim(0, 4)

host.legend()

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())

plt.draw()
plt.show()



features.close()
