import math
# from random import randrange as rnd
from random import randint as rnd

file_name = 'kargerMinCut.txt'

file = open(file_name)

graph = map(lambda l: map(lambda n: int(n), l.split(' ')), file.readlines())
graph = map(lambda a: [a[0], a[1:]], graph) # format: [vertex, [connections]]



def rca(g):
    if len(g) == 2:
        return len(g[0][1])
    else:
        def find(g, v):
            for i in range(len(g)):
                if g[i][0] == v:
                    return i
            print g, v, '!!!!!!!!!!!!!!'

        def filter(a, vs):
            return [i for i in a if i not in vs]
        
        rnd1 = rnd(0, len(g) - 1)
        rnd_vert1 = g[rnd1]
        edge = [rnd_vert1[0], rnd_vert1[1][rnd(0, len(rnd_vert1[1]) - 1)]]
        rnd2 = find(g, edge[1])
        rnd_vert2 = g[rnd2]
        g[rnd1][1] = filter((g[rnd1][1] + g[rnd2][1]), edge)
        del g[rnd2]
        g = map(lambda l: [l[0], map(lambda i: i if i != edge[1] else edge[0], l[1])], g)
        
        return rca(g)

print rca(graph)