def dictionary_of_squares(n):
    dictionary = {a: a*a for a in range(1, n+1)}
    return dictionary


x = int(input('Inter the number: '))
print(dictionary_of_squares(x))