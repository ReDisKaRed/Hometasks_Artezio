def subset(x, y, z):
    lt = []
    for i in z:
        if i in x and i in y:
            b = True
            lt.append(b)
        elif i not in x and i not in y:
            b = False
            lt.append(b)
        else:
            b = False
            lt.append(b)

    if False in lt:
        return False
    else:
        return True


print(subset([1, 2], [2, 3], [1]))
print(subset([1, 2], [2, 3], [2]))
print(subset([1, 2], [2, 3], [7]))
print(subset([1, 2], [2, 3], [2, 5]))
print(subset([5, 2, 7], [2, 3, 5], [2, 5]))
print(subset([1, 2], [2, 3], [4, 2]))
