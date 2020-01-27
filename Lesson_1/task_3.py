def new_string(string):
    if len(string) < 2:
        new_str = ''
    else:
        new_str = string[0:2] + string[-2:]
    return new_str


x = input("Enter the string: ")
print(new_string(x))