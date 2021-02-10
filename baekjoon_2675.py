s = list(input().split())
print(s)
print(''.join(char*int(s[0]) for char in s[1]))
# 런타임 에러나네...대체 왜
#
# s = list(input().split())
# for i in s:
