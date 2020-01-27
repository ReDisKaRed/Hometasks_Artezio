def character_frequency(string):
    dictionary = {a: 0 for a in string}
    for i in string:
        if i in dictionary.keys():
            dictionary[i] += 1
    return dictionary


x = input("Enter the string: ")
print(character_frequency(x))
