# from math import gcd
# from functools import reduce
# def solution(arr):
#     return reduce(lambda a, b: a*b // gcd(a, b), arr)
#

from math import gcd

def nlcm(num):
    answer = num[0]
    for n in num:
        answer = n * answer / gcd(n, answer)
    return answer