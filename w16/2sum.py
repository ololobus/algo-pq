file_name = '2sum.txt'

array = open(file_name).readlines()
array = map(lambda i: int(i), array)

length = len(array)

print 'Array loaded'

total = 0

for t in range(-10000, 10001, 1):
    hsh = {}
    for x in array:
        hsh[t - x] = x
    for y in array:
        if y in hsh and y != hsh[y]:
            total += 1
            print total, t, y, hsh[y]
            break

print total
