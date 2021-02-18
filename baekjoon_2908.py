number_compare = map(str, input().split())
list_num = list(number_compare)
rev_list_num = [list_num[0][::-1], list_num[1][::-1]]
if rev_list_num[0] > rev_list_num[1]:
    print(rev_list_num[0])
elif rev_list_num[1] > rev_list_num[0]:
    print(rev_list_num[1])