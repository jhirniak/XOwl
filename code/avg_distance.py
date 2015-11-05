__author__ = 'Jaroslaw Hirniak'

DISTANCE_MATRIX_FILE = '/home/ravanave/Repos/stn/datasets/Wikispeedia/wikispeedia_paths-and-graph/shortest-path-distance-matrix.txt'

from collections import defaultdict

with open(DISTANCE_MATRIX_FILE) as fh:

    print("Started. Please, wait it will take up to a minute.")

    for line in fh:
        if len(line) and line[0] != '#':
            break

    avg_dist = 0.0
    n = 0
    row = -1
    connected, total = 0, 0
    not_connected = []  # (x, y) means x is not connected to y

    not_connected_to_some_article = set()
    not_connected_count = defaultdict(lambda: 0)

    for line in fh:
        row += 1
        col = -1
        not_con = 0
        for d in line:
            col += 1
            is_connected = 1 if d in "1234567890" else 0
            connected += is_connected
            total += 1

            di = int(d) if d in "1234567890" else 0
            avg_dist = (avg_dist * n + di) / (n+1)
            n += 1

            if not is_connected:
                not_connected.append((row, col))
                not_con += 1

        not_connected_count[row] += not_con

    print("Finished. Checked {} articles.".format(row + 1))
    print("Avg distance: {}".format(avg_dist))
    print("Total distances counted: {}".format(avg_dist, n))
    print("{} out of {} articles were connected, i.e. {}%.".format(connected, total, connected/total))
    # print("Not connected articles:")
    # print(not_connected)

    T = row + 1

    print("Articles not connected to at least one article: {}".format(not_connected_to_some_article))
    print("{} out of {} articles were not connected to at least one article, i.e. {}%.".format(
        len(not_connected_to_some_article), T, len(not_connected_to_some_article) / T))

    print("Count of number of articles not being connected to:")
    for aid in range(T):
        print("{} is not connected to {} articles, i.e. {}%.s".format(
            aid, not_connected_count[aid], not_connected_count[aid] / T))
