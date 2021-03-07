class Solution:
    def solution(self, code, message):

        if message.isalpha():  # message가 문자라면
            new_msg = [message[i: i + 1] for i in range(len(message))]  # 한 글자씩 분리

            num_new_msg = [str(code.find(new_msg[j]) + 1).zfill(2) if len(new_msg[j]) != 2
                           else find(code[j]) + 1 for j in range(len(new_msg))]
            # 한 글자씩 분리한 리스트의 항목들이 각각 code의 몇번 항목에 해당하는지 찾은 후 새로운 리스트에 입력

            return "".join(num_new_msg)


        elif message.isdigit():  # message가 숫자라면
            new_msg = [message[i: i + 2] for i in range(0, len(message), 2)]  # 두 글자씩 분리

            str_new_msg = [code[int(new_msg[j]) - 1] for j in range(len(new_msg))]
            # 두 글자씩 분리한 숫자들이 코드의 어떤 알파벳에 해당하는지 찾은 후 새로운 리스트에 입력