import math

# file_name = 'test.txt'
file_name = 'IntegerArray.txt'

file = open(file_name)

numbers = map(lambda n: int(n), file.readlines())

def merge(a1, a2):
    n = len(a1) + len(a2)
    (i, j) = (0, 0)
    merged = []
    inversions = 0 #Split inversions
    # print a1, a2

    for k in range(n):
        if i <= len(a1) - 1 and j <= len(a2) - 1:
            if a1[i] < a2[j]:
                merged += [a1[i]]
                i += 1
            elif a2[j] < a1[i]:
                merged += [a2[j]]
                inversions += len(a1) - i
                j += 1
        if i > len(a1) - 1 and j <= len(a2) - 1:
            merged += [a2[j]]
            j += 1
        if j > len(a2) - 1 and i <= len(a1) - 1:
            merged += [a1[i]]
            i += 1

        # print k, merged


    return (inversions, merged)

def count_inversions(a):
    if len(a) > 2:
        middle = int(math.ceil(len(a)/2))
        (n1, a1) = count_inversions(a[:middle])
        (n2, a2) = count_inversions(a[middle:])
        (n3, a3) = merge(a1, a2)
        return (n1 + n2 + n3, a3)
    elif len(a) == 2:
        return (1, a[::-1]) if a[0] > a[1] else (0, a)
    else:
        return (0, a)

# print count_inversions(numbers)
print count_inversions(numbers)[0]
