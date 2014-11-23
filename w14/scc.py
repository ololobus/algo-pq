import math
import sys

sys.setrecursionlimit(100000)

file_name = 'SCC.txt'
file_name = 'test3.txt'


file = open(file_name)

raw_graph = sorted(map(lambda l: map(lambda n: int(n), l.split(' ')[:-1]), file.readlines()), key=lambda k: k[0])
graph = []
n = 0

print 'Initial map finished'

for r in raw_graph:
    if r[0] - n - 1 < 2:
        if len(graph) != r[0]:
            n += 1
            graph.append([n, [r[1]]])
        else:
            graph[n - 1][1].append(r[1])
    else:
        for j in range(r[0] - n - 1):
            n += 1
            graph.append([n, []])

print 'Graph restructuring finished'

print graph

rev_graph = []
visited = []
visited_rev = []

for i in range(len(graph)):
    rev_graph.append([i + 1, []])
    visited.append(False)
    visited_rev.append(False)

for r in graph:
    for v in r[1]:
        rev_graph[v - 1][1].append(r[0])

print 'Reversed graph ready'

def dfs1(g, n):
    global t, visited_rev
    visited_rev[n - 1] = True
    for j in g[n - 1][1]:
        if not visited_rev[j - 1]:
            dfs1(g, j)
    t += 1
    graph[n - 1].append(t)

t = 0

for i in range(len(graph), 0, -1):
    if not visited_rev[i - 1]:
        dfs1(rev_graph, i)

sort_graph = sorted(graph, key=lambda k: k[2]) 

print 'Sort finished'

def dfs2(g, n, l):
    global visited, s
    s[l][0] += 1
    s[l][1].append(n)
    visited[n - 1] = True
    for j in g[n - 1][1]:
        if not visited[j - 1]:
            dfs2(g, j, l)

s = {}
sizes = []

for i in range(len(graph), 0, -1):
    if not visited[i - 1]:
        s[i] = [0, []]
        dfs2(rev_graph, i, i)
        sizes.append(s[i][0])

print sorted(sizes)[-7:]
print sum(sizes)
print len(sizes)
print s
# print sort_graph
# print graph[-100:]
# print graph
# print rev_graph
