def factorial(x):
    i = 1
    for y in range(1, x+1):
        i = y*i
    return i


x1 = int(input('Number = '))
print(factorial(x1))
