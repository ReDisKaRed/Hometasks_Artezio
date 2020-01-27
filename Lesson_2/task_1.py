def squares_of_numbers(x):
    l = []
    for i in range(x+1):
        if i%2 == 0:
            i = i*i
            l.append(i)
    length = 'Amount of numbers: ' + str(len(l))
    return l, length


number = int(input("Number = "))
print(squares_of_numbers(number))
