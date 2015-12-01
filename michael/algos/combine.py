#!/usr/bin/python

from tarjan import tarjan
import yaml

f = open('wiki.json', 'r')

vanilla = yaml.load(f.read())

g = open('new_graph.json', 'r')

enriched = yaml.load(g.read())

combined = vanilla

for page in enriched:
    if page in combined:
        combined[page] = list(set(combined[page] + enriched[page]))



print combined

# t = tarjan(combined)
# sorted_t = sorted(t, key=len)
#
# print 'SCC size: ', len(sorted_t[len(sorted_t)-1])
