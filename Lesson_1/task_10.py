def difference_for_a(a, b):
    new_a = []
    for i in a:
        if i not in b:
            new_a.append(i)
    return new_a


print(difference_for_a(['a', 'a', 'b', 45, 'Hello', 'Name'], ['a', 67, 'Hello', 45]))