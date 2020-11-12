# 10808번
# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오.
from string import ascii_lowercase
'''
# 맞지만 시간 초과 우려
n = 26
# list는 int형태.
list = [0 for i in range(n)]

# 알파벳 리스트 만드는 방법.
# 파이썬은 문자열을 인덱스로 접근 가능하다.
alpha_list = ascii_lowercase

num = input()

for i in range(len(num)):
    for k in range(len(alpha_list)):
        if (num[i] == alpha_list[k]):
            list[k] += 1

for j in range(len(list)):
    print(list[j], end=' ')
'''
# 2 번째 시도.
num = input()
alpha_list = ascii_lowercase

for i in range(len(ascii_lowercase)):
    a = num.count(alpha_list[i])
    print(a, end=' ')
