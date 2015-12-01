#!/usr/bin/python

import yaml


class Milgram:
    def __init__(self, graph, target):
        self.graph = graph
        self.target = target
        self.total_distance = 0
        self.made_it = 0

    def bfs(self, start):
        visited, queue = set(), [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                if vertex in self.graph:
                    queue.extend(set(self.graph[vertex]) - visited)
        return visited

    def create_matrix(self):
        return [[0 for y in range(len(self.graph))] for x in range(len(self.graph))]

    def bfs_paths(self, start, goal):
        queue = [(start, [start])]
        while queue:
            (vertex, path) = queue.pop(0)
            if vertex in self.graph:
                for next in set(self.graph[vertex]) - set(path):
                    if next == goal:
                        yield path + [next]
                    else:
                        queue.append((next, path + [next]))

    def shortest_path(self, start, goal):
        try:
            return next(self.bfs_paths(start, goal))
        except StopIteration:
            return None

    def run(self):
        for page in self.graph:
            print page
            distance = self.shortest_path(page, self.target)

            if distance is not None:
                self.total_distance += len(distance) - 1
                self.made_it += 1

        return float(self.total_distance) / float(self.made_it)


if __name__ == '__main__':
    # f = open('wiki.json', 'r')
    #
    # j = yaml.load(f.read())
    #
    # print('Loaded the graph')
    #
    # milgram = Milgram(j, 112875)  # USA
    #
    # print milgram.run()

     milgram = Milgram({1: [2, 3], 2: [4], 99: [55]}, 4)
     print milgram.create_matrix()
