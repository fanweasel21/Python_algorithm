# from itertools import combinations
# def solution(people, limit):
#     escape = list(combinations(people, 2))
#     # print(escape)
#     a = [sum(group) <= limit for group in escape]
#     print(a.count(True) + (len(people)-2))
#
# solution([70, 80, 50, 50], 100)


# 두 명만 들어가면 되기 때문에 가장 무거운 사람과 가장 가벼운 사람만 비교하면 되는것이라고....하

def solution(people, limit):
    people.sort(reverse=True)
    start, end = 0, len(people) - 1
    cnt = len(people)
    #보트의 개수를 사람 수만큼 잡아두고 두 명씩 타는 경우가 생기면 하나씩 빼주는 방법
    while start < end:
        if people[start] + people[end] <= limit:
            end -= 1
            cnt -= 1
        start += 1
    return cnt
