#!/usr/bin/python

from tarjan import tarjan
import yaml

f = open('combined.json', 'r')

j =yaml.load(f.read())

print('Loaded the graph')

t = tarjan(j)
sorted_t = sorted(t, key=len)

print 'SCC size: ', len(sorted_t[len(sorted_t)-1])