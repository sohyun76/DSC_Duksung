# 1712번


# a, b, c = int(input().split())
# a = int(a) / b = int(b)
# 대신 쉽게 사용하는 방법.
# map 사용하기. 한 번에  a,b,c가 int형으로 바뀐다.
a, b, c = map(int, input().split())
x = 0

# 손익분기점이 존재하지 않는 경우는 b >= c 일 때이다.
if b >= c:
    print(-1)
else:
    x = (a/(c-b)) + 1
    print(int(x))
