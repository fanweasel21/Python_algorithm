def solution(s):
    s_1 = list(map(int, s.split()))
    return " ".join((str(min(s_1)), str(max(s_1))))

print(solution("1 2 3 4"))


#아오 샹 대체 뭐가 문제냐고 왜 안뒈는데 하.,,,
#드디어 됐네 아......