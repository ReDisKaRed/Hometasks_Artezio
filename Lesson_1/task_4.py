def number_of_strings(strings):
    list_strings = []
    for string in strings:
        if len(string) >= 2 and string[0] == string[-1]:
            list_strings.append(string)
    return len(list_strings)


print(number_of_strings(['aba', 'xyz', 'aa', 'x', 'bbb']))
