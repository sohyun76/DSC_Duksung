# 11729번
# 하노이 탑 이동 순서

# from_pos : A / to_pos : C / aux_pos : B


def Hanoi(n, from_pos, aux_pos, to_pos):
    if n == 1:
        print(from_pos, to_pos)
        # h_list.append([from_pos, to_pos])
    else:
        Hanoi(n-1, from_pos, to_pos, aux_pos)  # n-1개를 A->B로 이동.
        # 가장 큰 원반은 C로 이동.
        print(from_pos, to_pos) # n원반을 A->C로 이동.
        # h_list.append([from_pos, aux_pos])
        Hanoi(n-1, aux_pos, from_pos, to_pos) # n-1개를 B->C로 이동.


a = int(input())
print(2**a - 1)
Hanoi(a, 1, 2, 3)

