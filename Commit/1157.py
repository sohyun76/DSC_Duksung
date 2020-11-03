# 1157번
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

"""
# 첫 번째 시도.
# input()보다는 readline()이 적게 걸려.
import sys
a = sys.stdin.readline().rstrip().upper()
max = 0
max_index = 0
count = 0
results = True
a_len = len(a)

for i in range(a_len):
    count = a.count(a[i],i,a_len)
    if max < count:
        max = count
        max_index = i
    elif max == count:
        results = False
    count = 0

if results == True :
    print(a[max_index])
elif len(a) == 1:
    print(a)
elif results == False:
    print("?")

a = input().lower()
print(a.count(a[0],0,len(a)))

# 두 번째 시도.
import sys
a = sys.stdin.readline().rstrip().upper()
t = []
for i in range(len(a)):
    t.append(a.count(a[i], i, len(a)))
num = max(t)
if t.count(num) == 1 :
    print(a[t.index(num)])
else:
    print("?")

"""

import sys

a = input().rstrip().upper()
b = list(set(a))
c = list()
for i in b:
    c.append(a.count(i))
num = max(c)
if c.count(num) >= 2:
    print("?")
else:
    print(b[c.index(num)])
