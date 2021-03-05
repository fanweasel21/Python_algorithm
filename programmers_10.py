def solution(n):
    cnt = 0
    while n > 0:
        q, r = divmod(n, 2)
        n = q
        if r != 0:
            cnt += 1
    return cnt

#아니 문제 이해를 못하겠어서 풀지를 못하겠네ㅋㅋ;;