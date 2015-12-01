#!/usr/bin/python

import yaml

names = {}

n = open('names.csv', 'r')

for name in n:
    key, val = name.strip().split(',',1)
    names[int(key)] = val


output = open('degrees_combined.csv', 'w+')

f = open('combined.json', 'r')

j = yaml.load(f.read())

print('Loaded the graph')

total = 0

for page in j:
    degrees = len(j[page])
    total += degrees
    output.write("{0},{1}\n".format(names[page], degrees))

print 'average: ', float(total)/len(j)

