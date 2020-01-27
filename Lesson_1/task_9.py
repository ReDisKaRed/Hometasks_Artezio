def remove_duplicates(l):
    n_l = list(set(l))
    return n_l


x = ['qwe', '1', '1', 1, 'asdas', 'adferg', 'qwe']
print(remove_duplicates(x))