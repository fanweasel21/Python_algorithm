# word = input().upper()
# # print(word)
# freq = {}
# for i in word:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1
#
# print(str(freq))

# from collections import Counter
# word = input().upper()
# result = Counter(word)

word = input().upper()
word_list = list(set(word))  # word에 들어있는 알파벳 하나씩 빼내서 반복문 돌릴 리스트 만들기
cnt = []

for i in word_list:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(word_list[(cnt.index(cnt)))].upper())