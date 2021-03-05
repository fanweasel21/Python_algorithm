def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][1] or words[p] in words[:p]:
            #만약 끝말잇기가 제대로 되지 않았거나 지금 말한 단어가 지금까지의 리스트에 있었다면
            return [(p%n)+1, (p//n)+1]
        else:
            return [0, 0]


solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])

