def merge_dictionaries(dict1, dict2):
    d = {}
    d.update(dict1)
    d.update(dict2)
    return d


x1 = {1: 'dfsdw', 'asdsd': '1234'}
x2 = {1: 'e2', 2: '21'}
print(merge_dictionaries(x1, x2))