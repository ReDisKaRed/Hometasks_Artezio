def divide_by_number(a, b, c):
    l = []
    for i in range(a+1, b):
        if i % c == 0:
            l.append(i)
    length = len(l)
    answer = str(length) + ' numbers are divided by ' + str(c)
    return answer


a1 = int(input('a = '))
b1 = int(input('b = '))
c1 = int(input('c = '))
print(divide_by_number(a1, b1, c1))
