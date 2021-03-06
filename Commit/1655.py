# 1655
# 최대,최소힙으로 나눠서 풀기.
'''
list = []
n = int(input())

for i in range(n):
    a = int(sys.stdin.readline())
    list.append(a)
    list.sort()
    if len(list) == 1:
        print(a)
    else:
        if len(list) % 2 == 0:
            b = int(len(list) // 2) - 1
            print(list[b])
        else:
            b = int(len(list) // 2)
            print(list[b])
'''
from bisect import bisect_left
import sys

num = int(input())
array = []
length = 0
for i in range(num):
    a = int(sys.stdin.readline())
    index = bisect_left(array, a)
    array.insert(index, a)
    length += 1

    if length % 2 == 0:
        print(array[(length//2)-1])
    else:
        print(array[length//2])
