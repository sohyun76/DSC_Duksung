# 7568번

num = int(input())
list_a = []

for i in range(num):
    a, b = map(int, input().split())
    list_a.append((a, b))

for i in list_a:
    rank = 1
    for j in list_a:
        if i[0]< j[0] and i[1]< j[1]:
            rank += 1
    print(rank, end=" ")