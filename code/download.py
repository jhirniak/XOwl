#!/opt/anaconda/bin/python3

import argparse

class Dataset(object):

    def __init__(self, url, size=None, extract=None):
        assert(url, "URL must be specified, otherwise data set will not be downloaded.")
        self.url = url
        self.size = size
        self.extract = extract

    def _download(self):
        pass

    def _extract(self):
        pass

    def get(self):
        self._download()
        self._extract()

if __name__ == "__main__":
    # argparser = argparse.ArgumentParser(prog='Download data sets specified in JSON file.')
    DATASETS = [
    'http://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2',
    'https://snap.stanford.edu/data/wikispeedia.html '
]