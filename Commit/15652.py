# 15652 번

n,m = map(int, input().split())
out = []

def solve(depth,idx,n,m):
    if depth == m:
        print(' '.join(map(str,out)))
        return
    for i in range(idx,n):
        out.append(i+1)
        solve(depth+1,i,n,m)
        out.pop()

solve(0,0,n,m)