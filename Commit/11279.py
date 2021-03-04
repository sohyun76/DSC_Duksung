# 우선순위 큐
# 11279번
# heapq 모듈은 이진 트리(binary tree) 기반의 최소 힙(min heap) 자료구조를 제공
"""
시간초과.
def pops():
    b = max(list)
    list.remove(b)
    print(b)

list = []
num = int(input())
for i in range(num):
    a = int(input())
    list.append(a)
    if a==0:
        pops()
"""
import sys
import heapq
num = int(input())
list = []
for i in range(num):
    a = int(sys.stdin.readline())
    # int(input()) 하면 시간초과나옴.
    if a == 0:
        try:
            print(-1 * heapq.heappop(list))
        except:
            print(0)
    else:
        heapq.heappush(list, (-a))