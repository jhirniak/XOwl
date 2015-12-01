#!/usr/bin/python3


import collections
import csv
import sys


CHUNKSIZE = 400000
PAGE_BEGIN = '<p>'
PAGE_END = '</p>'


def extractor(tag):
    BEGIN_TAG = '<{}>'.format(tag)
    END_TAG = '</{}>'.format(tag)
    END_TAG_LEN = len(END_TAG)

    def get_tag(str):
        start, end = str.index(BEGIN_TAG), str.index(END_TAG)
        content = str[start+len(PAGE_BEGIN):end]
        return content, end + END_TAG_LEN

    print("\033[1m\033[7m\033[34mGenerated extractor for <{}> tag.\033[0m".format(tag))

    return get_tag


def transform(f):
    print("\033[1m\033[7m\033[34mBeginning transformation...\033[0m")
    get_page = extractor('p')
    get_title = extractor('t')
    get_link = extractor('l')
    conmap = collections.defaultdict(list)
    indmap = {}
    i = 0
    fi = 0

    last_read = f.read(CHUNKSIZE)
    buf = last_read

    while last_read:
        while '</p>' in buf:

            # Get page and update buffer
            page, end = get_page(buf)
            buf = buf[end:]

            # Extract title and links
            title, _ = get_title(page)
            links = []

            if not (i % 1000):
                print("\033[32mProcessed {} pages. Current page: {} page.\033[0m".format(i, title))

            while '</l>' in page:
                link, link_end = get_link(page)
                links.append(link)
                page = page[link_end:]

            # Update indmap

            if title not in indmap:
                indmap[title] = i
                i += 1

            for link in links:
                if link not in indmap:
                    indmap[link] = i
                    i += 1

            # Update conmap
            for link in links:
                conmap[indmap[title]].append(indmap[link])

        # no more matching tags, read more chars
        last_read = f.read(CHUNKSIZE)
        buf += last_read

        fi += 1
        if not (fi % 20):
            fi = 0
            print("\033[1m\033[33mReading more from file...\033[0m")

    return conmap


def dump_conmap(conmap, f):
    # dump the map
    print("\033[1m\033[7m\033[34mDumping map to {}...\033[0m".format(f))
    df = csv.writer(f, delimiter=' ')

    for title_id, link_ids in conmap.items():
        row = [title_id] + link_ids
        df.writerow(row)


if __name__ == "__main__":
    print("\033[1m\033[7m\033[34mParsing {}...\033[0m".format(sys.argv[1]))

    with open(sys.argv[1], 'r') as fin, open(sys.argv[2], 'w') as fout:
        conmap = transform(fin)
        print("\033[1m\033[7m\033[34mFinished creating map.\033[0m")
        dump_conmap(conmap, fout)
