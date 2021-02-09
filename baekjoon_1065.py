n = int(input())
lst = []
if n < 100:
    print(n)
elif 100 <= n <= 1000:
    for i in range(100, n + 1):
        hund = i//100
        ten = (i % 100)//10
        one = i % 10
        if hund - ten == ten - one:
            lst.append(i)
        else:
            pass
    print(len(lst) + 99)
