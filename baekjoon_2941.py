# croatia_alpha = input()
# # print(croatia_alpha)
# default_alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
# alpha_count = []
# for alphabet in default_alpha:
#     if alphabet in croatia_alpha:
#         alpha_count.append(alphabet)
# print(len(alpha_count))

a = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
alpha = input()

for t in a:
    alpha = alpha.replace(t, "*")

print(len(alpha))

#이렇게 쉬운걸 뭘 그리 어렵게 풀려고 했나 