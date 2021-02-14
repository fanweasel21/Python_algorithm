def solution(brown, yellow):
    for i in range(1, yellow+1):
        if yellow % i == 0:
            length = yellow//i
            if (((i+2)*(i+2))-(i*length)) == brown:
                return [max(i+2, length+2), min(i+2, length+2)]


