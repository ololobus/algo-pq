import sys

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


# progress = 0
#
# for i in range(length):
#     for j in range(length)[(i + 1):]:
#         if -10000 <= int(array[i]) + int(array[j]) <= 10000:
#             total += 1
#     if i % 100000 == 0:
#         progress += 10
#         sys.stdout.write(str(progress) + '% ')
#
# print 'Stupid 2sum result: ', total
#
# total = 0
