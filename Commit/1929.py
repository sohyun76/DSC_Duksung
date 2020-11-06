# 1929번
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 첫 번째 시도 : 시간초과
# 2부터 i까지 검사해서 시간 초과 발생.
# 해결법:
# 2부터 i의 제곱근까지만 검사하면, i의 제곱근이후의 수는 검사하나 마나이기 때문에
# sqrt()를 사용해 i의 제곱근까지만 검사하기.
'''
M, N = map(int, input().split())


for i in range(M, N+1):
    result = True
    for j in range(2, i):
        if i % j == 0:
            result = False
            break
    if (result == True):
        print(i, end="\n")
'''
import math
def myFunction(a):
    if a == 1:
        return False
    else:
        num = int(math.sqrt(a))
        for i in range(2, num+1):
            if a%i == 0:
                return False

        return True

M, N = map(int, input().split())
for j in range(M, N+1):
    if(myFunction(j)):
        print(j)

