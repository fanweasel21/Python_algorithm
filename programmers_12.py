# def solution(n, a, b):
#     cnt = 0
#     if a < b:
#         while b != 2:
#             if b // 2 == 0:
#                 b = b//2
#                 cnt += 1
#             elif b // 2 != 0:
#                 b = (b+1) // 2
#                 cnt += 1
#         if b == 2:
#         return cnt
#
# solution(8, 4, 7)

def solution(n, a, b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2
    return answer

solution(8, 4, 7)