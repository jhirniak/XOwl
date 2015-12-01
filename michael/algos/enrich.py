#!/usr/bin/python


from py2neo import Graph

f = open('lang_mapping.csv', 'r')

scot_en = {}
en_scot = {}
titles = []

names = {}

g = {}

n = open('names.csv', 'r')

for line in n:
    id, title = line.strip().split(',', 1)
    names[title] = int(id)

for line in f:
    if '","' in line:
        scot, en = line.strip().split('","', 1)
    else:
        scot, en = line.strip().split(',', 1)

    scot = scot.replace('_', ' ')[1:]
    en = en[:-1]
    scot_en[scot] = en
    en_scot[en] = scot

f.close()
d = open('degrees.csv', 'r')

for line in d:
    title, deg = line.strip().split(',', 1)
    titles.append(title)

graph = Graph()

for title in titles:
    try:
        if title in scot_en:
            g[names[title.replace(',', '')]] = []
            en_title = scot_en[title]

            links = graph.cypher.execute(
                'MATCH (p0:Page {title:"' + en_title + '"}) -[Link]- (p:Page) RETURN p.title as title')
            for link in links:
                try:
                    if link.title in en_scot:
                        g[names[title.replace(',', '')]].append(names[en_scot[link.title].replace(',', '')])
                except:
                    pass
            #print g[names[title.replace(',', '')]]
    except:
        pass

print g
