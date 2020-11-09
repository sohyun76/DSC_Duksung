# 10828번
import sys


def push(X):
    list.append(X)
    return(X)
def pop():
    if(size()==0):
        return -1
    else:
        return list.pop()

def size():
    return len(list)
def empty():
    if(size() == 0):
        print(1)
    else:
        print(0)
def top():
    if(size()==0):
        return -1
    else:
        return list[-1]

num = int(sys.stdin.readline().rstrip())
list = []
for _ in range(num):
    a = sys.stdin.readline().rstrip().split()
    if a[0] == 'push':
        push(a[1])
    elif a[0] == 'top':
        print(top())
    elif a[0] == 'empty':
        empty()
    elif a[0] == 'size':
        print(size())
    elif a[0] == 'pop':
        print(pop())