def full_name(s):
    s = s.split()
    f_n = []
    for i in s:
        f_n.append(i.capitalize())
    f_n = ' '.join(f_n)
    return f_n


name = input("Enter your name: ")
print(full_name(name))

