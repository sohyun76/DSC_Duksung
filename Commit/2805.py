# 2805번
a, b = map(int, input().split())
list_tree = list(map(int, input().split()))
left = 0
right = max(list_tree)
ans = 0

while left <= right:
    mid = (left+right)//2
    tree = 0
    for i in range(a):
        if list_tree[i] > mid:
            tree += list_tree[i] - mid
    if tree >= b:
        ans = mid
        left = mid + 1
    elif tree < b:
        right = mid - 1
print(ans)
