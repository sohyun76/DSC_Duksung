# 1629번
# 1회 실패: 시간 초과

"""
def function1(x, y, z):
    print((x**y) % z)

a, b, c = map(int, input().split())
function1(a, b, c)
"""

def function1(x, y, z):
    print(pow(x, y, z))

a, b, c = map(int, input().split())
function1(a, b, c)