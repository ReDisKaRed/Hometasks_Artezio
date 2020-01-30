def func_range(stop):
    lt= []
    i = -1
    while len(lt) != stop:
        i += 1
        lt.append(i)
    return lt


print(func_range(10))
