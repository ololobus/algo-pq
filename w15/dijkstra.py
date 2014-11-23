import math

file_name = 'dijkstraData.txt'

file = open(file_name)
# graph = [[0, 7, 9, -1, -1, 14], [7, 0, 10, 15, -1, -1], [9, 10, 0, 11, -1, 2], [-1, 15, 11, 0, 6, -1], [-1, -1, -1, 6, 0, 9], [14, -1, 2, -1, 9, 0]]

graph = [[-1 for j in range(200)] for i in range(200)]
start = 0

for i in range(200):
    graph[i][i] = 0

for r in file.readlines():
    r = r.split(' ')
    for v in r[1:]:
        v = v.split(',')
        graph[int(r[0]) - 1][int(v[0]) - 1] = int(v[1])
        graph[int(v[0]) - 1][int(r[0]) - 1] = int(v[1])


rng = range(len(graph[0]))

results = []
work_results = []
visited = []
path = []

for i in rng:
     results.append(float("inf"))
     work_results.append(float("inf"))
     visited.append(False)
     path.append([start])

results[start] = 0
work_results[start] = 0

all_visited = False

while not all_visited:
    current = work_results.index(min(work_results))

    for i in rng:
        if (graph[current][i] >= 0) and not visited[i] and ((results[current] + graph[current][i]) < results[i]):
            results[i] = results[current] + graph[current][i]
            path[i] = path[current] + [i]
            work_results[i] = results[current] + graph[current][i]

    work_results[current] = float("inf")
    visited[current] = True
    check = True
    for point in visited:
        check = check and point

    all_visited = check
    current = False


print list( results[i - 1] for i in [7,37,59,82,99,115,133,165,188,197] )
