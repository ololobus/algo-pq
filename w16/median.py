file_name = 'Median.txt'
file_name = 'test.txt'

array = open(file_name).readlines()
array = map(lambda i: int(i), array)

length = len(array)
summ = 0

for k in range(1, length + 1, 1):
    a = sorted(array[:k])
    if k % 2 == 0:
        summ += a[k/2 - 1]
    else:
        summ += a[(k + 1)/2 - 1]
    if k % 100 == 0:
        print str(k) + ' elems processed'

print summ % 10000