#! /usr/bin/env python

features = open('datasetWithFeeling.txt', 'r')
featuresDict = {}
book = ""
for line in features:
  if line[1] == "C":
    # First line. Messy but to the point
    continue
  if line[0] == '#':
    book = line[1:-1]
  else:
    featuresDict[book] = line[:-1]
features.close()

postagged = open('postagger_results2.txt', 'r')
postaggedDict = {}
book = ""
for line in postagged:
  if line[0] == '#':
    book = line[1:-1]
  else:
    postaggedDict[book] = line[:-1]
postagged.close()

joined = open('joined2.txt', 'w')
for k,v in featuresDict.items():
  if k in postaggedDict:
    joined.write('#' + k + '\n')
    joined.write(v[-1] + ',' + v[:-1] + postaggedDict[k] + '\n')

joined.close()
