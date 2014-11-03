import math

# file_name = 'test.txt'
file_name = 'QuickSort.txt'

file = open(file_name)

numbers = map(lambda n: int(n), file.readlines())
comparisons = 0

def get_pivot(a, type):
    if type == 'first':
        return (0, a[0])
    elif type == 'last':
        return (len(a) - 1, a[-1])
    elif type == 'median':
        points = [(0, a[0]), (int(math.floor((len(a) - 1)/2)), a[int(math.floor((len(a) - 1)/2))]), (len(a) - 1, a[-1])]
        return sorted(points, key=lambda x: x[1])[1]


def partition(a, p):
    a[0], a[p[0]] = a[p[0]], a[0]
    i = 1
    for j in range(1, len(a), 1):
        if a[j] < p[1]:
            a[i], a[j] = a[j], a[i]
            i += 1

    a[0], a[i - 1] = a[i - 1], a[0]
    return (a, i - 1)

def qs(a):
    global comparisons

    if len(a) == 1:
        return a
    p = get_pivot(a, 'median')
    (pa, pi) = partition(a, p)

    comparisons += len(a) - 1

    res = []
    if pi != 0:
        res += qs(a[:pi])

    res += [pa[pi]]

    if pi != len(pa) - 1:
        res += qs(a[(pi + 1):])

    return res


print qs(numbers), comparisons
