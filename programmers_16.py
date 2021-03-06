# def solution(skill, skill_trees):
#     possible = []
#     for i in range(1, len(skill_trees)):
#         for j in range(2, len(skill)):
#             if skill_trees[i].find(skill[j]) < skill_trees[i].find(skill[j-1]):
#                 possible.append(skill_trees[i])
#     return len(possible)
# 왜 이것만으로는 안될까.......

def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer

solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])
