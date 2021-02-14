# import random
# def solution(A, B):
#     num_list = []
#     for i in A:
#
#         num_list.append(a)
#     return min(num_list)
#
# print(solution([1, 4, 2], [5, 4, 4]))

#랜덤이 아니라 가장 작은 수랑 가장 큰 수 더하는 거였음,,,,,하아

def solution(A, B):
    answer = 0
    A = sorted(A)
    B = sorted(B, reverse=True)

    answer = sum([a*b for a, b in zip(A, B)])
    return answer