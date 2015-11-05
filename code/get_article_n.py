__author__ = 'Jaroslaw Hirniak'

ARTICLE_NAMES_FILE = '/home/ravanave/Repos/stn/datasets/Wikispeedia/wikispeedia_paths-and-graph/articles.tsv'

import argparse
import html


argparser = argparse.ArgumentParser(prog='Get article name for n in the distance matrix')
argparser.add_argument(dest='n', type=int)

args = argparser.parse_args()
n = args.n

with open(ARTICLE_NAMES_FILE) as fh:
    for line in fh:
        if len(line) and line[0] != '#':
            break

    while n:
        fh.readline()
        n -= 1

    article_name = html.unescape(fh.readline())
    print("Article {} is {}".format(args.n, article_name))
