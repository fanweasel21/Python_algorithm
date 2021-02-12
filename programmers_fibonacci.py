# def solution(n):
#     if n < 2:
#         return n % 1234567
#     else:
#         return solution(n-1)%1234567 + solution(n-2)%1234567
#런타임 에러....ㅠㅠㅜㅠ

def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a+b
    return a
